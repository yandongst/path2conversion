import sys

delimit='-;,'


def print_event(event, start_s, end_s):
  if start_s != end_s:
    sys.stdout.write( '%s,%s%s%s,%s'%(start_s,event,delimit, end_s,event))
  else:
    sys.stdout.write( '%s,%s'%(start_s,event))

def print_events(l_events):
  l=[]
  for event,ts in l_events:
    l.append(ts+','+event)
  sys.stdout.write(delimit.join(l))
  print

def add_event(l_events,event, start_s, end_s):
  if start_s != end_s:
    l_events.append((event,start_s))
    l_events.append((event,end_s))
  else:
    l_events.append((event,start_s))

for l in sys.stdin:
  l = l.strip()
  c,r = l.split('\t')
  current_event = None
  start_ts = 0
  end_ts = 0
  if len(r.split(delimit)) == 1:
    continue
  #print 'org:'+l
  #print
  sys.stdout.write(c+'\t')
  l_events=[]
  for rr in r.split(delimit):
    try:
      date,event=rr.split(',')[0:2]
      if current_event == None:
        current_event = event
        start_ts = date
        end_ts = date
        #not_finished=True
      elif event == current_event:#keep updating ending event
        end_ts = date
        #not_finished=True
    
      elif event != current_event:
        #print_event(current_event, start_ts,end_ts)
        add_event(l_events,current_event, start_ts,end_ts)
        start_ts = date
        end_ts = date
        current_event = event
        #not_finished=True

    #if not_finished:
    
    except Exception,ex:
      sys.stderr.write(l+'\n'+str(ex)+'\n')
      sys.stderr.write(rr+'\n')
      sys.stderr.write( '---Error:'+rr+'\n') 

  #print_event(current_event, start_ts,end_ts)
  add_event(l_events,current_event, start_ts,end_ts)
  print_events(l_events)
