#!/usr/bin/env python3
from difflib import SequenceMatcher
import filecmp
import os


def text_content_diff(a, b):
    """check for actual line by line differences, returns float [0,1]"""
    checker = SequenceMatcher(None, a, b)
    return checker.ratio()


def file_direct_compare(a, b):
    """diffing binary files is a pain, so this just checks equality"""
    return filecmp.cmp(a, b)


def filter_by_extension(files: list, extensions):
    """in my case I only care about .s and .txt files
    binary files break the normal diff tool"""
    cleaned_files = list()
    for item in files:
        extension = item.split(".")[-1]
        if extension in extensions:
            cleaned_files.append(item)
    return cleaned_files


def is_comparison_duplicate(a, b, seen):
    """my scheme is name, name, ratio
    files can appear in either position, check"""
    for comparison in seen:
        if (comparison[0] == a and comparison[1] == b) or (
            comparison[0] == b and comparison[1] == a
        ):
            return True
    return False


def is_same_submitter(a, b):
    """canvas names in all submissions download are appended to front before _"""
    aname = a.split("_")[0]
    bname = b.split("_")[0]
    return aname == bname


def is_useful_comparison(a, b, seen):
    if a == b:
        return False  # comparison a to a
    if is_comparison_duplicate(a, b, seen):
        return False  # seen a,b or b,a
    if is_same_submitter(a, b):
        return False  # files by same user
    return True


def diff_files_in_dir(path, extensions={"s", "txt"}, differ=text_content_diff):
    similar_files = list()

    files = filter_by_extension(os.listdir(path), extensions)

    for first in files:
        ftext = open(first, "r").readlines()
        for second in files:
            if not is_useful_comparison(first, second, similar_files):
                continue

            stext = open(second, "r").readlines()
            result = differ(ftext, stext)

            if result > 0.7:
                similar_files.append((first, second, result))
    return similar_files


def diff_objs_in_dir(path, differ=file_direct_compare):
    similar_files = list()

    files = os.listdir(path)

    for first in files:
        for second in files:
            if first == second or is_comparison_duplicate(first, second, similar_files):
                continue

            result = differ(first, second)
            if result:
                similar_files.append((first, second, result))
    return similar_files


def main():
    cwd = os.getcwd()
    similar_files = diff_files_in_dir(cwd)

    for item in similar_files:
        print(f"Files \t{item[0]} and \t{item[1]} are {item[2]*100}% similar.")


if __name__ == "__main__":
    main()
