import re,glob,json,html,collections,os
pages=sorted(f for f in glob.glob('*.html') if not f.startswith('_'))
titles=collections.Counter();descs=collections.Counter();rows=[]
allfiles=set(pages)
for f in pages:
    t=open(f).read()
    ti=html.unescape((re.search(r'<title>(.*?)</title>',t) or [None,''])[1])
    de=html.unescape((re.search(r'<meta name="description" content="([^"]*)"',t) or [None,''])[1])
    h1=re.findall(r'<h1',t);can=re.search(r'rel="canonical" href="([^"]+)"',t)
    og=len(re.findall(r'property="og:',t));tw=len(re.findall(r'name="twitter:',t))
    ld=[]
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,re.S):
        try:
            j=json.loads(m);g=j.get('@graph',[j]) if isinstance(j,dict) else j
            for x in g: ld.append(x.get('@type'))
        except Exception as e: ld.append('ERR')
    imgs=re.findall(r'<img\b[^>]*>',t);noalt=[i for i in imgs if 'alt=' not in i]
    links=set(re.findall(r'href="([a-z0-9-]+\.html)(?:#[^"]*)?"',t));broken=[l for l in links if l not in allfiles]
    body=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);words=len(re.sub(r'<[^>]+>',' ',body).split())
    titles[ti]+=1;descs[de]+=1
    issues=[]
    if not 30<=len(ti)<=65: issues.append(f'title {len(ti)}')
    if not 110<=len(de)<=160: issues.append(f'desc {len(de)}')
    if len(h1)!=1: issues.append(f'h1 x{len(h1)}')
    if not can: issues.append('no canonical')
    if og<4: issues.append(f'og {og}')
    if noalt: issues.append(f'noalt {len(noalt)}')
    if broken: issues.append(f'broken {broken}')
    rows.append((f,len(ti),len(de),words,ld,issues))
for r in rows: print(r[0][:42].ljust(43),r[1],r[2],r[3],r[4],r[5])
print('dup titles',[k for k,v in titles.items() if v>1]);print('dup descs',[k for k,v in descs.items() if v>1])
