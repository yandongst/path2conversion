import sys
import re



# event = share/click -> share
# event = pview, ref_query = google


def normalize(q):
  q=q.lower().replace('+',' ')
  return q

for l in sys.stdin:
  l = l.rstrip()
  fs = l.split('\t')
  #for x in range(len(fs)):
    #print x,fs[x]
  date = fs[0]
  event = fs[2]
  ref_domain = fs[10].lower()
  pview_channel = fs[11].lower()

  #print ref_domain
  #print pview_channel
  #print fs[1]

  if re.search('(google|bing|msn|ask|aol|altavista|excite)\.', ref_domain) and pview_channel.find('q=')!=-1:
    m = re.search('q=([^&]+)',pview_channel)
    query=''
    if m:
      query = m.group(1).strip()
      query = normalize(query)
    print fs[1]
    print '%s\t4\t%s\t%s'%(date,ref_domain,query)

  if re.search('(yahoo)\.', ref_domain) and pview_channel.find('p=')!=-1:
    m = re.search('p=([^&]+)',pview_channel)
    query=''
    if m:
      query = m.group(1).strip()
      query = normalize(query)
    print fs[1]
    print '%s\t4\t%s\t%s'%(date,ref_domain,query)

  if re.search('(lycos|netscape|cnn)\.', ref_domain) and pview_channel.find('query=')!=-1:
    m = re.search('query=([^&]+)',pview_channel)
    query=''
    if m:
      query = m.group(1).strip()
    print '%s\t4\t%s\t%s'%(date,ref_domain,query)

  if re.search('(yandex)\.', ref_domain) and pview_channel.find('text=')!=-1:
    m = re.search('text=([^&]+)',pview_channel)
    query=''
    if m:
      query = m.group(1).strip()
    print '%s\t4\t%s\t%s'%(date,ref_domain,query)

  if re.search('(baidu)\.', ref_domain) and pview_channel.find('wd=')!=-1:
    m = re.search('wd=([^&]+)',pview_channel)
    query=''
    if m:
      query = m.group(1).strip()
    print '%s\t4\t%s\t%s'%(date,ref_domain,query)
  
  #if ref_domain.find('google.')!=-1 and pview_channel.find('q=')!=-1:
    #m = re.search('q=([^&]+)',pview_channel)
    #query=''
    #if m:
      #query = m.group(1)
    #print '%s\t4\t%s\t%s'%(date,ref_domain,query)
