import sys
import re


for l in sys.stdin:
  l = l.rstrip()
  fs = l.split('\t')
  #print len(fs)
  if len(fs) != 21:
    continue
  camp = fs[0]
  campid = fs[1]
  adgroupid = fs[17]
  event = fs[9]
  domain = fs[7]
  cookie = fs[8]
  ts = int(fs[20])/1000
  if not cookie.endswith('A'):
    continue
  ### IMPR
  if event=='impr':
    event_no=13
  if event=='click':
    event_no=14
  print '%s\t%d,%d,%s,%s,%s'%(cookie,event_no,ts,camp,campid,adgroupid)

