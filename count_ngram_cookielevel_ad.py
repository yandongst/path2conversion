import sys
import operator
import optparse

delimit=';'
delimit='-;,'
sum_all=0
#cnt_s=0
#cnt_se=0

x_pairs=[]
x_pairs_ad=[]
x_pair_cnt={}
x_pair_ad_cnt={}
x_starts_cnt={}
x_starts_ad_cnt={}




def output(x_pair_cnt, x_starts_cnt):
  for pair in x_pair_cnt:
    start_s = pair[0]
    end_s = pair[1]
    cnt_se = x_pair_cnt[pair]
    cnt_s = x_starts_cnt[start_s]

    if cnt_s == 0:
      pass
      #print '%d cnt is 0'%start_s 
    else:
      #pass
      print '%s,%s\t%d,%d,%f'%(start_s,end_s,cnt_s,cnt_se,float(cnt_se)/cnt_s)

def get_all_pairs(l_events):
  for i in l_events:
    x_starts_cnt[i]=0
    x_starts_ad_cnt[i]=0
    for j in l_events:
      x_pairs.append((i,j))
      x_pair_cnt[(i,j)]=0
      x_pairs_ad.append((i,j))
      x_pair_ad_cnt[(i,j)]=0


def get_ngrams_tw(events, n, sw,bw, ad_events, s_ignoreevents):
  x_cookie_pairs=set([])
  x_cookie_pairs_ad=set([])
  l = len(events)
  for i in range(l-n+1):
    has_ad = False
    e_1 = events[i]
    #DEBUG
    if e_1[1] in ad_events or e_1[1] in s_ignoreevents:
    #if e_1[1] in s_ignoreevents:
      continue
    for j in range(i+1,l-n+2): 
      e_2 = events[j]

      pair = (e_1[1],e_2[1])

      if pair in x_cookie_pairs_ad and pair in x_cookie_pairs:
        continue

      if e_2[1] in s_ignoreevents:
        continue

      start_date = e_1[0]
      end_date = e_2[0]
      delta = e_2[0]-e_1[0]
      if delta>bw or delta<sw:
        #print 'break due to tw'
        break

      if e_2[1] in ad_events:
        has_ad = True
        continue

      #for k in range(i+1,j):
        #if events[k][1] in ad_events:
          #has_ad = True
          #break

      if has_ad:
        if pair not in x_cookie_pairs_ad:
          x_cookie_pairs_ad.add(pair)
      else:
        if pair not in x_cookie_pairs:
          x_cookie_pairs.add(pair)

  #print 'no ad:',x_cookie_pairs
  #print 'ad:',x_cookie_pairs_ad
  for pair in x_cookie_pairs:
    x_starts_cnt[pair[0]]+=1
    x_pair_cnt[pair]+=1
  for pair in x_cookie_pairs_ad:
    x_starts_ad_cnt[pair[0]]+=1
    x_pair_ad_cnt[pair]+=1

def main(): 
  parser = optparse.OptionParser("usage: %prog [options] arg1 arg2") 
  parser.add_option("-s", "--small_window", dest="small_window", default=0, type="int", help="small time window") 
  parser.add_option("-b", "--big_window", dest="big_window", default=3600*24*7, type="int", help="big time window") 
  parser.add_option("-a", "--adlift", dest="ad_lift", default=False, action="store_true", help="ad lift") 
  parser.add_option("-o", "--sociallift", dest="social_lift", default=False, action='store_true', help="social lift") 
  (options, args) = parser.parse_args()
  small_window = options.small_window
  big_window = options.big_window
  adlift = options.ad_lift
  sociallift = options.social_lift

  if adlift and sociallift:
    sys.stderr.write('Can only compute one lift one time.\n')
    sys.exit(1)
  if not adlift and not sociallift:
    sys.stderr.write('Have to compute one lift one time.\n')
    sys.exit(1)

  #adlift
  l_events = [1,2,3,4,11,12,14]
  s_adevents=set([13])
  s_ignoreevents=set([])
  metric_cmp='ad'
  if adlift:
    #for ad life
    sys.stderr.write('compute ad lift.\n')
  if sociallift:
    #for social life
    sys.stderr.write('compute social lift.\n')
    l_events = [1,2,3,4,11,12,14]
    s_adevents=set([1,2])
    s_ignoreevents=set([13])
    metric_cmp='social'

  sys.stderr.write('small time window:'+str(small_window)+'\n')
  sys.stderr.write('big time window:'+str(big_window)+'\n')

  get_all_pairs(l_events)

  cnt=0 

  for l in sys.stdin:
    l = l.rstrip()
    c,r = l.split('\t')
    events = []
    for rr in r.split(delimit):
      try:
        date,event=rr.split(',')[0:2]
        events.append((int(date),int(event)))
      except Exception,ex:
        sys.stderr.write(l+'\n'+str(ex)+'\n')
        sys.stderr.write(rr+'\n')
        sys.stderr.write( '---Error:'+rr+'\n') 

    if len(events) <=1: continue
    #print 'org:'+l
    get_ngrams_tw(events,2,small_window, big_window,s_adevents, s_ignoreevents)

    cnt+=1
    if cnt%10000==0:
      sys.stderr.write('line:'+`cnt`+'\n')

  #print 'pair cnt:'
  #print x_pair_cnt
  #print 'single cnt:'
  #print x_starts_cnt

  #print x_pair_cnt
  print 'without '+metric_cmp+ ':'
  output(x_pair_cnt, x_starts_cnt)
  print 'with '+metric_cmp+':'
  output(x_pair_ad_cnt, x_starts_ad_cnt)



if __name__=='__main__':
  main()
