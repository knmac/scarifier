# IMG="frames/frame001.jpg"
IMG=$1

#echo $IMG

curl -sS -F "image=@"$IMG -XPOST http://smithgpu07.pok.ibm.com:6600/tag_face_mood
