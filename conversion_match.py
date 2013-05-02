import sys
import datetime
from datetime import datetime,timedelta
import time

delimit='-;,'

s_retarg=set([])#11
s_conv=set([])#11
s_impr_pixel=set([])#13
s_click_pixel=set([])#14
s_cates=set([])
s_adgroups=set([])
s_kw=set([])

lookback=60*60*24*7

def read_pixels(fn):
  global s_retarg
  global s_conv
  global s_impr_pixel
  global s_click_pixel
  global s_cate
  global s_adgroups
  global s_kw
  for l in open(fn,'r'):
    l = l.rstrip()
    if l.startswith('#'):
      continue
    type,pixel = l.split(':')
    type=type.strip()
    if type == 'retarg':
      s_retarg.add(pixel)
    elif type == 'conv':
      s_conv.add(pixel)
    elif type == 'impr':
      s_impr_pixel.add(pixel)
    elif type == 'click':
      s_click_pixel.add(pixel)
    #elif type == 'cate':
      #s_cates.add(pixel)
    elif type == 'adgroup':
      s_adgroups.add(pixel)
    elif type == 'keyword':
      s_kw = set([x.strip().lower() for x in pixel.split(',')])
      #print s_kw
    else:
      sys.stderr.write('Error: unrecognized type:'+type)
      #sys.exit(1)

def filter_events(events, ts1, ts2):
  l_events=[]
  has_conv=False
  has_click=False
  has_impr=False
  events.reverse()
  for ev in events:
    fields=ev.split(',')
    if len(fields)<3:continue
    try:
      ts=long(fields[0])
      event=fields[1]
      if(ts<(ts1-lookback)):break
      if event=='11' and fields[2] in s_conv:
        if(ts>=ts1 and ts<ts2): 
          has_conv=True
          l_events.append(ev);
      elif event=='13':#impr
        if fields[2] in s_impr_pixel:
          has_impr=True
          l_events.append(ev);
      elif event=='14':#click
        if fields[2] in s_click_pixel:
          has_click=True
          l_events.append(ev);
    except:
      #print>>sys.stderr, 'ERROR:',ev
      pass
  if has_conv: return has_impr,has_click,l_events
  else: return has_impr,has_click,[] 

def find_match(events, has_impr,has_click):
  converted=False
  conv_ts=''
  viewthrumatch=0
  viewthrurt=0
  clickthrumatch=0
  cnt_unmatch=0
  lastmatch=False
  if not has_impr and not has_click:
    print 'N/A\tunmatch'
    return
  for e in events:
    fields=e.split(',')
    #if len(fields)<3:continue
    evno=fields[1]
    evname=fields[2]
    evts=long(fields[0])
    #if converted and (conv_ts-evts)>lookback:break
    if evno == '11' and evname in s_conv:
      converted=True
      conv_ts=evts
    elif evno == '14' and evname in s_click_pixel and converted:
    #this is intended to print multiple clicks
      adg=fields[3]
      print adg+'\tclick-conversion'
    elif evno == '13' and evname in s_impr_pixel and converted: 
      adg=fields[3]
      if has_click:
        print adg+'\tnonlastmatch'
      elif not lastmatch:
        lastmatch=True
        cnt_lastmatch=1
        print adg+'\tlastmatch'
      else:
        cnt_match=1
        print adg+'\tnonlastmatch'
    elif evno == '13' and not converted:
      pass 

read_pixels(sys.argv[1])
lastday=sys.argv[2]
st = datetime.strptime(lastday, "%Y%m%d")
st1 =st + timedelta(days=1)
import calendar
ts1 = calendar.timegm(st.utctimetuple())
ts2 = calendar.timegm(st1.utctimetuple())


def debug(events):
  if len(events)==1:return
  hasothers=False
  for e in events:
    fields=e.split(',')
    if fields[1]!='11':
      hasothers=True
  if hasothers:print events

for l in sys.stdin:
  l = l.strip()
  c,r = l.split('\t')
  events=r.split(delimit)
  has_impr,has_click,f_events=filter_events(events,ts1,ts2)
  if not f_events: continue
  find_match(f_events,has_impr,has_click)
