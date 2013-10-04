DATA=$(cat integration.json)
echo $DATA



curl -i \
    -H "Content-Type: application/json" \
    -H "X-Github-Event: pull_request" \
    -X POST -d "$DATA" \
    http://relayr



