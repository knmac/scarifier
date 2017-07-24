import os
import glob
from subprocess import Popen, STDOUT, PIPE
import json
import cv2
import time
import ipdb


TO_EXTRACT = True  # FIXME: turn on or off
VIDS_DIR = 'vids'
FRAMES_DIR = 'frames'
FACIAL_FRAMES_DIR = 'facial_frames'
FPS = '1'
DURATION = 5


osa_cmd_m = """
osascript -e 'tell application "System Events" to keystroke "m" using {command down}'
"""
osa_d = """
osascript -e 'tell application "System Events" to keystroke "d"'
"""
osa_s = """
osascript -e 'tell application "System Events" to keystroke "s"'
"""
osa_a = """
osascript -e 'tell application "System Events" to keystroke "a"'
"""

def extract_frames(input_fn, output_dir, fps):
    """ Extract frames from a given video file. Output is stored in output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cmd = 'ffmpeg ' + \
            '-i ' + input_fn + \
            ' -vf fps=' + fps + \
            ' ' + output_dir + '/frame%05d.jpg'
    sp = Popen(cmd.split(' '), stdout=PIPE)
    sp.communicate()
    return


def recog_visual_img(img_fn):
    """ Recognize visual information from an image
    """
    sp = Popen('./visual_api_handler.sh ' + img_fn,
            shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
    out, err = sp.communicate()
    return out 


def recog_facial_img(img_fn):
    """ Recognize facial expression from a given image file.
    Return:
        positive_sc: score of positive mood
        neutral_sc: score of neutral mood
        negative_sc: score of negative mood
    """
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
    """ Recognize facial expression of multiple images insisde input_dir.
    This calls recog_facial_img() for each image
    """
    img_lst = glob.glob(os.path.join(input_dir, '*.jpg'))
    for img_fn in img_lst:
        positive_sc, neutral_sc, negative_sc = recog_facial_img(img_fn)
        print img_fn
        print '\tpositive: %f\n\tneutral: %f\n\tnegative: %f' % (positive_sc, neutral_sc, negative_sc)
    return


def main_show_cv():
    """ Demo using open cv
    """
    cap = cv2.VideoCapture(0)
    # cap.set(3, 320)
    # cap.set(4, 240)
    prev_time = time.time()
    
    vid1 = cv2.VideoCapture('vids/movie_lighter.mp4')
    vid2 = cv2.VideoCapture('vids/movie_original.mp4')
    vid3 = cv2.VideoCapture('vids/movie_scarrier.mp4')

    status = 0

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        ret1, frame1 = vid1.read()
        ret2, frame2 = vid2.read()
        ret3, frame3 = vid3.read()

        # break event
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # recognizen facial expression after a duration
        if time.time() - prev_time >= DURATION:
            prev_time = time.time()
            img_fn = os.path.join(FACIAL_FRAMES_DIR, str(prev_time)+'.jpg')
            cv2.imwrite(img_fn, frame)

            positive_sc, neutral_sc, negative_sc = recog_facial_img(img_fn)
            print img_fn
            print '\tpositive: %f\n\tneutral: %f\n\tnegative: %f' % (positive_sc, neutral_sc, negative_sc)

            if positive_sc > negative_sc:
                status = min(status+1, 1)
                os.system(osa_s)
            else:
                status = max(status-1, -1)
                os.system(osa_d)
        
        # Display the resulting frame
        if status == -1:
            cv2.imshow('frame', frame1)
        elif status == 0:
            cv2.imshow('frame', frame2)
        elif status == 1:
            cv2.imshow('frame', frame3)
        # cv2.imshow('frame', frame)

    cap.release()
    cv2.destroyAllWindows()


def main_send_event():
    """ Send osascript as controlling event to movie player
    """
    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)
    prev_time = time.time()
    
    status = 0
    msg = ''

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # break event
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # recognizen facial expression after a duration
        if time.time() - prev_time >= DURATION:
            prev_time = time.time()
            img_fn = os.path.join(FACIAL_FRAMES_DIR, str(prev_time)+'.jpg')
            cv2.imwrite(img_fn, frame)

            positive_sc, neutral_sc, negative_sc = recog_facial_img(img_fn)
            print img_fn
            print '\tpositive: %f\n\tneutral: %f\n\tnegative: %f' % (positive_sc, neutral_sc, negative_sc)
            
            msc = max(positive_sc, neutral_sc, negative_sc)
            if positive_sc == msc:
                status = 1
                os.system(osa_s)
            elif negative_sc == msc:
                status = -1
                os.system(osa_d)
            else:
                status = 0
                os.system(osa_a)

            msg = img_fn + \
                '\n  Current scaryness level: ' + str(status) + \
                '\n  positive: ' + str(positive_sc) + \
                '\n  neutral: ' + str(neutral_sc) + \
                '\n  negative: ' + str(negative_sc)
        
        # Display the resulting frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        y0, dy = 20, 14
        for i, line in enumerate(msg.split('\n')):
            y = y0 + i*dy
            cv2.putText(frame, line, (350, y), font, 0.5, (255, 255, 255), 1)
        cv2.imshow('frame', frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # main_show_cv()
    main_send_event()
    print 'Done'
