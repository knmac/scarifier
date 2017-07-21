import glob
import time
import shutil
import random
from subprocess import Popen, PIPE
import ipdb


TAG_DIR = 'frames_tag'

# VID_IN = 'vids/movie_scarrier.mp4'
# SFX_LST = glob.glob('sfx/scary*')
# VID_OUT = 'vids/movie_scarrier_autosfx.mp4'

VID_IN = 'vids/movie_lighter.mp4'
SFX_LST = glob.glob('sfx/funny*')
VID_OUT = 'vids/movie_lighter_autosfx.mp4'


if __name__ == '__main__':
    tag_list = glob.glob(TAG_DIR + '/*.txt')
    N = len(tag_list)

    # filter out 'has golf'
    has_golf = []
    for i in range(N):
        fn = tag_list[i]
        content = open(fn).read()

        if '"class": "golf"' in content:
            has_golf.append(1)
        else:
            has_golf.append(0)
    
    exit()
    shutil.copy(VID_IN, 'dummy_0.mp4')
    cnt = 0
    for i in range(1, N):
        if has_golf[i] and not has_golf[i-1]:
            fin = 'dummy_' + str(cnt) + '.mp4'
            cnt += 1
            fout = 'dummy_' + str(cnt) + '.mp4'
            offset = time.strftime('%H:%M:%S', time.gmtime(i))
            sfx = random.choice(SFX_LST)
            print offset

            cmd = ['ffmpeg', '-i', fin, '-itsoffset', offset, '-i', sfx,
                    '-map', '0:v', '-map', '1:a', '-c', 'copy',
                    '-async', '1', fout]
            ipdb.set_trace()
            sp = Popen(cmd, stdout=PIPE)
            out, err = sp.communicate()

    print 'Done'
