import os
import glob
from subprocess import Popen, STDOUT, PIPE
from main_handler import extract_frames, recog_visual_img

VIDS_DIR = 'vids'
FRAMES_DIR = 'frames'
FRAMES_TAG_DIR = 'frames_tag'
FPS = '1'

VID = os.path.join(VIDS_DIR, 'movie_original.mp4')


if __name__ == '__main__':
    # extract frames
    extract_frames(VID, FRAMES_DIR, FPS)

    # visual recognition
    frame_lst = glob.glob(os.path.join(FRAMES_DIR, '*.jpg'))
    for fn in frame_lst:
        print fn
        out = recog_visual_img(fn)
        tag_fn = fn.replace(FRAMES_DIR, FRAMES_TAG_DIR).replace('.jpg', '.txt')
        with open(tag_fn, 'w') as f:
            f.write(out)
    print 'Done'
