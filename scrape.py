import praw
from os import utime
import os.path
import errno

def make_sure_path_exists(path): # Courtesy of http://stackoverflow.com/a/5032238/34910
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

if __name__ == '__main__':
    d = 'comments'
    make_sure_path_exists(d)
    r = praw.Reddit(user_agent='natep_bot')
    dh = r.get_redditor('danharmon')
    for c in dh.get_comments(limit=None):
        id = c.id
        body = c.body
        t = c.created_utc
        if c.link_id != u't3_yne9x': # Will break as soon as he comments on a different post, I know
            print 'done!'
            break
        path = os.path.join(d, id)
        with open(path, 'wb') as f:
            print "Writing comment", id
            f.write(body.encode("UTF-8"))
            utime(path, (t, t))
    
