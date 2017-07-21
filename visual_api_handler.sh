#API_KEY="e91e544b63aca2f6717c428c7dc20b8af601cd2a"
API_KEY="22aefab9b5c2799737321b2c723a1488a7229aab"
URL="https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify"
# IMG="visual_recognition_demo/Raising-a-Rukus.jpg"
VERSION="2016-05-20"

IMG=$1


curl -sS -X POST \
    -F "images_file=@"$IMG \
    $URL"?api_key="$API_KEY"&version="$VERSION
