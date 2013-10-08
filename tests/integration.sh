DATA=$(cat integration.json)

curl -i \
    -H "Content-Type: application/json" \
    -H "X-Github-Event: pull_request" \
    -X POST -d "$DATA" \
    http://localhost:8000

