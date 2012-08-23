import os, os.path, re
from datetime import datetime, timedelta

linkbase = u'<a href="http://reddit.com/r/IAmA/comments/yne9x/i_am_dan_harmon_creator_of_community_writer_of/%s?context=1">Permalink</a>'

def get_t(path):
    """Apparently os.utime() only sets the st_atime on my system. Workaround"""
    statinf = os.stat(path)
    return min(statinf.st_atime, statinf.st_mtime, statinf.st_ctime)
    
def td_secs(td):
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

if __name__ == '__main__':
    lastt = datetime.utcfromtimestamp(1345659401.0)
    for (root, dirs, fnames) in os.walk('comments'):
        paths = (os.path.join(root, t_id) for t_id in fnames)
        for p in sorted(paths, key=get_t):
            t_id = os.path.basename(p)
            thist = datetime.utcfromtimestamp(get_t(p))
            dt_mins = td_secs(thist - lastt) / 60.0
            text = linkbase % t_id
            words = 0.0
            with open(p) as f:
                body = f.read().decode('utf-8')
                words += len(re.findall('[A-Za-z0-9]+', body))
            wpm = words / dt_mins
            print "[new Date(%s), %d, '%s', '%s', %f, %s, %s]," % \
                (thist.strftime('%Y, %m, %d, %H, %M, %S'), \
                     words, \
                     t_id, \
                     text, \
                     wpm, \
                     'undefined', 'undefined')
            lastt = thist
                
