import sys

delimit='-;,'
#key_list=['ad','no_ad','so','no_so']
l_event=set()
l_channels=set([])
l_campaigns=set([])
l_adgroups=set([])
cnt={}

# product of
# (no_)CAMP,RTB(s), ADGROUP(s)
#   and 
# (no_)SOCIAL, channel(s)
#


for l in sys.stdin: 
  l = l.strip()
  k,v=l.split('\t')
  #adlift-3 = ((#3-ad) - (#3-no_ad))/(#2-no_ad)
  kk=k.split(delimit)
  l_event.add(kk[0])
  for vv in kk:
    if vv.startswith('r.'):
      l_campaigns.add(vv)
    elif vv.startswith('c.'):
      l_channels.add(vv)
    elif vv.startswith('a.'):
      l_adgroups.add(vv)
    elif vv.startswith('no_'):
      pass
  cnt[k]=float(v)

#print l_event
#print l_campaigns
#print l_adgroups
#print l_channels

#for k in cnt:
  #print k,cnt[k]

ll_camp=[]
ll_camp.append('CAMP')
ll_camp.extend(l_campaigns)
ll_camp.extend(l_adgroups)
ll_social=[]
ll_social.append('SOCIAL')
ll_social.extend(l_channels)


for e in l_event:
  k_ad=delimit.join([e,'CAMP'])
  k_noad=delimit.join([e,'no_CAMP'])
  c_ad=0
  c_noad=0
  if k_ad in cnt: c_ad=cnt[k_ad]
  if k_noad in cnt: c_noad=cnt[k_noad]
  cnt_ad=float(c_ad)
  cnt_noad=float(c_noad)
  if cnt_noad==0:
    print e,'N/A',cnt_ad,cnt_noad,'CAMP'
  else:
    adlift=(cnt_ad-cnt_noad)/cnt_noad
    print e,str(round(adlift,2)*100.0)+'%',cnt_ad,cnt_noad,'CAMP'

for e in l_event:
  for adg in l_adgroups:
    k_ad=delimit.join([e,adg])
    k_noad=delimit.join([e,'no_'+adg])
    c_ad=0
    c_noad=0
    if k_ad in cnt: c_ad=cnt[k_ad]
    if k_noad in cnt: c_noad=cnt[k_noad]
    cnt_ad=float(c_ad)
    cnt_noad=float(c_noad)
    if cnt_noad==0:
      print e,'N/A',cnt_ad,cnt_noad,adg
    else:
      adlift=(cnt_ad-cnt_noad)/cnt_noad
      print e,str(round(adlift,2)*100.0)+'%',cnt_ad,cnt_noad,adg 
