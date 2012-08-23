import os, os.path, re

if __name__ == '__main__':
    wordcounts = [] # Counts per post
    wordhist = [0] * 16 # counts per bin, max of 800 words, 16 bins -> range of 50/bin
    for (root, dirs, fnames) in os.walk('comments'):
        for p in (os.path.join(root, t_id) for t_id in fnames):
            t_id = os.path.basename(p)
            words = 0
            with open(p) as f:
                body = f.read().decode('utf-8')
                words += len(re.findall('[A-Za-z0-9]+', body))
            wordcounts.append(words)
            wordhist[words // 50]+=1
    print "Total:", sum(wordcounts)
    print "Max:", max(wordcounts)
    print "Mean:", sum(wordcounts)/float(len(wordcounts))
    print "Median:", sorted(wordcounts)[len(wordcounts)/2]
    print "Hist:", wordhist
                
