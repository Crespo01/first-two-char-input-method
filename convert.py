from os import path
import re
from sys import stderr
def load(filepath):
    with open(filepath) as f:
        data = f.readlines()
    return data
def containsAny(str, set):
    return 1 in [c in str for c in set]
def cw(str, set):
    return [c for c in set if c in str]


def indexize(word):
    if len(word) < 2:
        return "{0}/{0}".format(word)
    index = word[:2]
    return "{}/{}".format(index, word)


def mc(data):
    n_data = []
    p = re.compile('[^,.\w\s]')
    wrongline = 0
    sumline = 0
    for line in data:
        sumline += 1
        error_flag = False
        if p.search(line):
            wrongline += 1
            continue
        words = line.split()
        c_w = []
        for word in words:
            num_word = indexize(word)
            ss = cw(num_word, set([',', '.', '"', '..', ',,']))
            if ss:
                if len(ss) > 1:
                    error_flag = True
                    break
                if len(word) == 1:
                    c_w.append(num_word)
                else:
                    num_word = num_word.replace(ss[0], '')
                    c_w.append(num_word)
                    c_w.append('{0}/{0}'.format(ss[0]))
            else:
                c_w.append(num_word)
        if error_flag:
            continue
        n_data.append(' '.join(c_w))
    print('sumline = {}, wrongline= {}.'.format(sumline, wrongline),file=stderr)
    return n_data


def save(name, data):
    with open('libs/{}.txt'.format(name), 'a') as f:
        for d in data:
            f.write('{}\n'.format(d))


if __name__ == '__main__':
        filepath='text.txt'
#	for filepath in filepaths[1:]: 
         
        data = load(filepath)
        n_data = mc(data)
        base = path.basename(filepath)
        name = path.splitext(base)[0]
        save(name, n_data)
