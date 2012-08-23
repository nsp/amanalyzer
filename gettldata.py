import os, os.path
from datetime import datetime, timedelta

linkbase = u'<a href="http://reddit.com/r/IAmA/comments/yne9x/i_am_dan_harmon_creator_of_community_writer_of/%s?context=1">Permalink</a>'

def get_t(path):
    """Apparently os.utime() only sets the st_atime on my system. Workaround"""
    min(statinf.st_atime, statinf.st_mtime, statinf.st_ctime)
    
def td_secs(td):
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

if __name__ == '__main__':
    lastt = datetime(2012, 8, 22, 18, 16, 41)
    for (root, dirs, fnames) in os.walk('comments'):
        paths = (os.path.join(root, id) for fname in fnames)
        for p in sorted(paths, key=get_t):
            thist = datetime.fromtimestamp(get_t(p))
            text = linkbase % id
            words = 0
            with open(p) as f:
                body = p.read().decode('utf-8')
                words += len(re.findall('[A-Za-z0-9]+'))
            print "[new Date(%s), %d, %s, %s, %f, %s, %s]," % \
                thist.strftime('%Y, %m, %d, %H, %M, %S'), \
                words, \
                id, \
                text, \
                words / td_secs(thist - lastt), \
                'undefined', 'undefined'
            lastt = thist
                
