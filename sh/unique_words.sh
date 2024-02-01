bat pages/lipu/tomo-pi-walo-loje.md | sed -e 's/<!--.*-->//g' -e 's/^%.*//g' | grep -oE '\w+' | tr '[:upper:]' '[:lower:]' | sort | uniq | wc -l

# TODO: toki pona version that removes consecutive duplicates
