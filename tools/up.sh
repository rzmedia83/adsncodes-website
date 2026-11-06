#!/bin/bash
# usage: up.sh <localfile> <remote relative path>
. "$(dirname "$0")/hkeys.sh"
F="$1"; R="$2"; S=$(stat -c%s "$F")
c=$(curl -sS -o /dev/null -w '%{http_code}' -X POST "$HURL/$R?override=true" -H "X-Auth: $HAUTH" -H "X-Auth-Rest: $HREST" -H "Tus-Resumable: 1.0.0" -H "Upload-Length: $S" -H "Upload-Offset: 0")
[ "$c" = 201 ] || { echo "FAIL-POST $c $R"; exit 1; }
o=$(curl -sS -D - -o /dev/null -X PATCH "$HURL/$R?override=true" -H "X-Auth: $HAUTH" -H "X-Auth-Rest: $HREST" -H "Tus-Resumable: 1.0.0" -H "Content-Type: application/offset+octet-stream" -H "Upload-Offset: 0" --data-binary "@$F" | grep -i '^upload-offset' | tr -d '\r' | awk '{print $2}')
[ "$o" = "$S" ] && echo "OK $R" || { echo "FAIL-PATCH $o/$S $R"; exit 1; }
