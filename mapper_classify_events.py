import sys
import re
import simplejson as json

def print_search(date,ref_domain,query):
    print '%s\t4\t%s\t%s'%(date,ref_domain,query)

def find_search(ref_domain, ref_query):
  query=''
  if re.search('(google|bing|msn|ask|aol|altavista|excite)\.', ref_domain) and ref_query.find('q=')!=-1:
    m = re.search('q=([^&]+)',ref_query)
    if m:
      query = m.group(1).strip()
      return query

  if re.search('(yahoo)\.', ref_domain) and ref_query.find('p=')!=-1:
    m = re.search('p=([^&]+)',ref_query)
    if m:
      query = m.group(1).strip()
      return query

  if re.search('(lycos|netscape|cnn)\.', ref_domain) and ref_query.find('query=')!=-1:
    m = re.search('query=([^&]+)',ref_query)
    if m:
      query = m.group(1).strip()
      return query

  if re.search('(yandex)\.', ref_domain) and ref_query.find('text=')!=-1:
    m = re.search('text=([^&]+)',ref_query)
    if m:
      query = m.group(1).strip()
      return query

  if re.search('(baidu)\.', ref_domain) and ref_query.find('wd=')!=-1:
    m = re.search('wd=([^&]+)',ref_query)
    if m:
      query = m.group(1).strip()
      return query

  return ''

x_cate=set([])

def read_cate(fn):
  for l in open(fn,'r'):
    l = l.rstrip()
    if not l.startswith('#'):
      x_cate.add(l)

def in_cate(cates):
  for c in cates.split(','):
    if c in x_cate:
      return True
  return False


for l in sys.stdin:
  l = l.rstrip()
  fs = l.split('\t')
  date = fs[0]
  event = fs[1]
  domain = fs[3]
  cookie = fs[8]
  js = fs[13]
  refdomain = fs[10]
  refurl = fs[11]
  channel = fs[12]

  cates=[]
  kws=[]
  lang=''
  location=fs[9].replace(',','_')
  try:
    j=json.loads(js)
    if 'l99' in j:
      cates= j['l99']
    if 'l0' in j:
      kws= j['l0']
    if 'lang' in j:
      lang= j['lang']
      if lang != 'english':continue
  except Exception as inst:
    sys.stderr.write(str(inst)+'\n')
  #if not cookie.endswith('A'):
    #continue

  search_queries=''

  ### SHARE
  if event=='share':
    print '%s\t1,%s,%s,%s,%s,%s,%s,%s'%(cookie,date,domain,'-'.join(cates),channel,'-'.join(kws),search_queries,location)

  elif event=='click':
    print '%s\t2,%s,%s,%s,%s,%s,%s,%s'%(cookie,date,domain,'-'.join(cates),channel,'-'.join(kws),search_queries,location)

  elif event=='search':
    search_queries=find_search(refdomain,refurl)
    search_queries=search_queries.replace('+',' ').strip()
    #print 'search:', search_queries
    print '%s\t4,%s,%s,%s,%s,%s,%s,%s'%(cookie,date,domain,'-'.join(cates),channel,'-'.join(kws),search_queries,location)

  #elif event=='pview':
    #print '%s\t3,%s,%s,%s,%s,%s'%(cookie,date,domain,'-'.join(cates),channel,'-'.join(kws))

  else:
    pass
    #sys.stderr.write('Wrong'+l)
    #sys.exit(1)
