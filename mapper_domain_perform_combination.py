
import sys

delimit='-;,'

s_retarg=set([])#11
s_conv=set([])#11
s_impr_pixel=set([])#13
s_click_pixel=set([])#14
s_cates=set([])
s_adgroups=set([])
start_date=''
end_date=''
time_diff=3600*24*14#14days

def read_pixels(fn):
  global s_retarg
  global s_conv
  global s_impr_pixel
  global s_click_pixel
  global s_cate
  global s_adgroups
  for l in open(fn,'r'):
    l = l.rstrip()
    if l.startswith('#'):
      continue
    type,pixel = l.split(':')
    if type == 'retarg':
      s_retarg.add(pixel)
    elif type == 'conv':
      s_conv.add(pixel)
    elif type == 'impr':
      s_impr_pixel.add(pixel)
    elif type == 'click':
      s_click_pixel.add(pixel)
    elif type == 'cate':
      s_cates.add(pixel)
    elif type == 'adgroup':
      s_adgroups.add(pixel)
    else:
      sys.stderr.write('Error: unrecognized type:'+type)
      sys.exit(1)

def filter_seq(events):
  rc=[]
  for e in events:
    rrr=e.split(',')
    if len(rrr)<3:
      #print >>sys.stderr,e
      continue
    event=rrr[1]
    if event=='13':#impr
      if rrr[2] in s_impr_pixel:
        rc.append(e)
    if event=='14':#click
      if rrr[2] in s_click_pixel:
        rc.append(e)
    if event=='11':#retarg/conv
      if rrr[2] in s_retarg:
        rc.append(e)
      if rrr[2] in s_conv: 
        rc.append(rrr[0]+',12,'+','.join(rrr[2:]))
    if event=='12': 
      if rrr[2] in s_conv:
        rc.append(e)
  return rc


'''
ts1: timestamp of 1st event
ts2: timestamp of 2nd event
'''
def within_tw(ts1, ts2):
  #print ts1,ts2
  if ts1==-1:return False
  if (ts2-ts1)<time_diff: return True
  return False

read_pixels(sys.argv[1])

for l in sys.stdin:
  l = l.strip()
  c,r = l.split('\t')
  events=r.split(delimit)
  cur_camp=''
  cur_camp_ts=-1
  cur_camp_domain=''
  cur_click=''
  cur_click_ts=-1
  cur_click_domain=''
  #print events
  f_events=filter_seq(events)
  #print 'filtered:',f_events
 
  for rr in f_events:
    #print 'event:',rr
    rrr=rr.split(',')
    event=rrr[1]
    if event=='13':
      cur_camp=rrr[2]
      cur_camp_ts=int(rrr[0])
      cur_camp_domain=rrr[4]
    if event=='14':
      cur_click=rrr[2]
      cur_click_ts=int(rrr[0])
      cur_click_domain=rrr[4]
    if event=='11':#retarg
      if within_tw(cur_click_ts, int(rrr[0])):
        print cur_click+'--'+cur_click_domain+'--'+'ctr\t1'#click-thru-retarg
      elif within_tw(cur_camp_ts, int(rrr[0])):
        print cur_camp+'--'+cur_camp_domain+'--'+'vtr\t1'#view-thru-retarg
    if event=='12':#/conv
      if(within_tw(cur_click_ts, int(rrr[0]))):
        print cur_click+'--'+cur_click_domain+'--'+'ctc\t1'#click-thru-conv
      elif(within_tw(cur_camp_ts, int(rrr[0]))):
        print cur_camp+'--'+cur_camp_domain+'--'+'vtc\t1'#view-thru-conv
