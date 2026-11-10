import re,glob,hashlib,os,shutil,subprocess
os.chdir('/tmp/claude-0/-home-claude/35c3f5ad-aa3e-5285-ae81-3a4fa777bc81/scratchpad')
keep404=open('prod/404.html',encoding='utf-8').read()
main404=keep404[keep404.index('<main'):keep404.index('</main>')+7]
for f in glob.glob('site2/*.html'):
    if os.path.basename(f).startswith('_'): continue
    shutil.copy(f,'prod/'+os.path.basename(f))
os.makedirs('prod/ar',exist_ok=True)
for f in glob.glob('site2/ar/*.html'): shutil.copy(f,'prod/ar/'+os.path.basename(f))
for a in ['assets/site.js','assets/site.css','sitemap.xml','llms.txt','robots.txt']: shutil.copy('site2/'+a,'prod/'+a)
os.chdir('prod')
cv=hashlib.md5(open('assets/site.css','rb').read()).hexdigest()[:8]; jv=hashlib.md5(open('assets/site.js','rb').read()).hexdigest()[:8]
for f in glob.glob('*.html')+glob.glob('ar/*.html'):
    if f=='404.html': continue
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'<meta name="claude:[^"]*" content="[^"]*">\n?','',s)
    s=s.replace('href="assets/site.css"',f'href="assets/site.css?v={cv}"').replace('src="assets/site.js"',f'src="assets/site.js?v={jv}"')
    s=re.sub(r'<video\b[^>]*>', lambda m: re.sub(r'\sposter="', ' data-lposter="', m.group(0)) if ('data-src=' in m.group(0) and 'sr-v' not in m.group(0)) else m.group(0), s)
    if f=='index.html' and not s.lstrip().lower().startswith('<!doctype'):
        i=s.index('</style>')+8
        s='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+s[:i]+'\n</head>\n<body>'+s[i:].rstrip()+'\n</body>\n</html>\n'
    open(f,'w',encoding='utf-8').write(s)
s=open('about.html',encoding='utf-8').read(); he=s.index('</head>'); h=s[:he]
h=re.sub(r'<title>.*?</title>','<title>Page not found | Ads n&#x27; Codes</title>',h,flags=re.S)
h=re.sub(r'<meta name="description"[^>]*>','<meta name="description" content="This page has moved or no longer exists.">',h)
h=re.sub(r'<meta name="robots"[^>]*>','',h); h=re.sub(r'<link rel="(canonical|alternate)"[^>]*>','',h)
h=re.sub(r'<script type="application/ld\+json">.*?</script>','',h,flags=re.S); h=re.sub(r'<meta property="og:[^>]*>','',h)
h=h.replace('<head>','<head>\n<base href="/">\n<meta name="robots" content="noindex">',1)
b=s[he:]; open('404.html','w',encoding='utf-8').write(h+b[:b.index('<main')].replace('<a class="skip" href="#top">Skip to content</a>\n','')+main404+b[b.index('</main>')+7:])
print(cv,jv)
