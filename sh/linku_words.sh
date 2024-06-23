curl "https://api.linku.la/v1/words?lang=en" | jq 'to_entries | map(.value.word)'
curl "https://api.linku.la/v1/sandbox?lang=en" | jq 'to_entries | map(.value.word)'
