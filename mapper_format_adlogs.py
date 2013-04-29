import sys
import re

sample=False

if len(sys.argv)>1:
  #print sys.argv
  if sys.argv[1]=='sample':sample=True

#print sample

for l in sys.stdin:
  l = l.rstrip()
  fs = l.split('\t')
  #print len(fs)
  #if len(fs) != 2:
    #continue
  camp = fs[11]
  campid = fs[13]
  adgroupid = fs[14]
  event_no=13
  if fs[25] == '1':
    event_no=14
  domain = fs[16]
  cookie = fs[20]
  ts = long(fs[10])/1000
  if sample:
    if not cookie.endswith('A'):
      continue
  print '%s\t%d,%d,%s,%s,%s,%s'%(cookie,event_no,ts,camp,campid,adgroupid,domain)

