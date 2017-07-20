import os
import glob
from subprocess import Popen, STDOUT, PIPE
import json
import ipdb


TO_EXTRACT = True  # FIXME: turn on or off
VIDS_DIR = 'vids'
FRAMES_DIR = 'frames'
FPS = '1'


def extract_frames(input_fn, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cmd = 'ffmpeg ' + \
            '-i ' + input_fn + \
            ' -vf fps=' + FPS + \
            ' ' + output_dir + '/frame%03d.jpg'
    sp = Popen(cmd.split(' '), stdout=PIPE)
    sp.communicate()
    return


def recog_facial_img(img_fn):
    sp = Popen('./emo_api_handler.sh ' + img_fn,
            shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
    out, err = sp.communicate()
    
    # parse json results
    foo = json.loads(out)[0]
    res = foo[1]['Image']
    # timing = res['Timing']['$']
    # name = res['Name']['$']
    att = res['Attribute']
    positive_sc = -1
    neutral_sc = -1
    negative_sc = -1
    for item in att:
        lbl = item['Label']['$']
        sc = item['Score']['$']
        if lbl == 'PositiveMood':
            positive_sc = sc
        elif lbl == 'NeutralMood':
            neutral_sc = sc
        elif lbl == 'NegativeMood':
            negative_sc = sc
    return positive_sc, neutral_sc, negative_sc


def recog_facial_seq(input_dir):
    img_lst = glob.glob(os.path.join(input_dir, '*.jpg'))
    for img_fn in img_lst:
        positive_sc, neutral_sc, negative_sc = recog_facial_img(img_fn)
        print img_fn
        print '\tpositive: %f\n\tneutral: %f\n\tnegative: %f' % (positive_sc, neutral_sc, negative_sc)
    return


def scarify():
    # TODO: implement
    return


if __name__ == '__main__':
    # demo pipeline
    face_input = os.path.join(VIDS_DIR, 'face.mp4')
    if TO_EXTRACT:
        extract_frames(face_input, FRAMES_DIR)  # NOTE: this can be replaced by stream monitoring
    recog_facial_seq(FRAMES_DIR)
    scarify()

    print 'Done'
