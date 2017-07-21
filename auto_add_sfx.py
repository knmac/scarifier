import glob
import json
import ipdb


TAG_DIR = 'frames_tag'


if __name__ == '__main__':
    tag_list = glob.glob(TAG_DIR + '/*.txt')
    N = len(tag_list)

    # filter out 'has golf'
    has_golf = []
    for i in range(N):
        fn = tag_list[i]
        content = open(fn).read()

        if '"class": "golf"' in content:
            has_golf.append('1')
        else:?!?jedi=0, ?!?              (*_*param object*_*) ?!?jedi?!?
            has_golf.append('0')

    print 'Done'
