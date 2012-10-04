import sys

e = sys.argv[1]

for l in sys.stdin:
  #print l.rstrip().split('\t')[18]
  s=l.rstrip().split('\t')
  if s[8].endswith(e):
    print l.rstrip()
