import re
import Mykytea
import sys
def uk(opt=''):
    mk = Mykytea.Mykytea(opt)
    return mk
def ukt(mk, txt):
    ts= mk.getTagsToString(txt)
    p = re.compile('\s\s/none')
    ts = re.sub(p, '', ts)
    return ts
if __name__ == '__main__':
    if len(sys.argv) != 1:
        mk = uk(' '.join(sys.argv[1:]))
    else:
        mk = uk()
    while True:
        try:
            txt = input()
        except -1:
            break
        ts = ukt(mk, txt)
        print(ts)
