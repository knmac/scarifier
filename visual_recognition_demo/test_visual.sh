API_KEY="e91e544b63aca2f6717c428c7dc20b8af601cd2a"
#URL="https://watson-api-explorer.mybluemix.net/apis/visual-recognition-v3#!/visual45recognition/classify"
URL="https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify"
IMG="Raising-a-Rukus.jpg"


curl -X POST \
    -F "images_file=@"$IMG \
    $URL"?api_key="$API_KEY"&version=2016-05-20"
