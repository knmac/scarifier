# API handler for emotion recognition
# Usage: ./emo_api_handler.sh <img_fn>
IMG=$1

curl -sS -F "image=@"$IMG -XPOST http://smithgpu07.pok.ibm.com:6600/tag_face_mood
