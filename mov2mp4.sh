# Convert mov to mp4 file using ffmpeg

#TODO: make input and output more flexible
INPUT="vids/face.mov"
OUTPUT="vids/face.mp4"

ffmpeg -i $INPUT -vcodec copy -acodec copy $OUTPUT
