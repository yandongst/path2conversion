import sys

for l in sys.stdin:
  s= l.strip().split('\t')
  #if len(s)!=4:
    #sys.stderr.write(l+'\n')
    #continue
  dt=s[0]
  pixel=s[1]
  camp=s[2]
  cookie=s[7]
  #dt,pixel,camp,co = l.rstrip().split('\t')
  if cookie.endswith('A'):
    print cookie+'\t11,'+dt+','+pixel+','+camp
