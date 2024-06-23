import json

from more_itertools import random_permutation


def permute(s: str) -> str:
    return "".join(random_permutation(s))


output = dict()

output["channel"] = dict()
output["guild"] = dict()
output["messages"] = list()

with open("temp.json", "r") as f:
    d = json.loads(f.read())

    container_id = d["channel"]["id"]
    community_id = d["guild"]["id"]
    community_name = d["guild"]["name"]

    output["channel"]["id"] = permute(container_id)
    output["guild"]["id"] = permute(community_id)
    output["guild"]["name"] = permute(community_name)

    for m in d.get("messages", []):
        message = dict()
        message["author"] = dict()

        _id = m["id"]
        author_id = m["author"]["id"]
        author_name = m["author"]["name"]
        postdate_str = m["timestamp"]
        content = m["content"]

        message["id"] = permute(_id)
        message["author"]["id"] = permute(author_id)
        message["author"]["name"] = permute(author_name)
        message["timestamp"] = postdate_str
        message["content"] = content

        output["messages"].append(message)

print(json.dumps(output))
