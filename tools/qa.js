const {chromium}=require('playwright');const fs=require('fs');
const pages=fs.readdirSync('prod').filter(f=>f.endsWith('.html')&&f!=='404.html').concat(fs.readdirSync('prod/ar').map(f=>'ar/'+f));
(async()=>{const b=await chromium.launch();const out=[];
for (const [w,h] of [[390,844],[820,1180],[1440,900]]){
 const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:w<800,hasTouch:w<1100});
 for (const f of pages){
  const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('JS '+e.message));p.on('console',m=>{if(m.type()==='error'&&!/maps|google|facebook|fbevents|gstatic|ERR_|net::/i.test(m.text()))errs.push('C '+m.text().slice(0,120))});
  p.on('requestfailed',r=>{const u=r.url();if(u.startsWith('http://localhost'))errs.push('404 '+u.replace('http://localhost:8765/',''))});
  try{await p.goto('http://localhost:8765/'+f,{waitUntil:'load',timeout:30000});}catch(e){errs.push('LOAD '+e.message.slice(0,80))}
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}scrollTo(0,0)});
  await p.waitForTimeout(400);
  const r=await p.evaluate(()=>{const W=innerWidth;const over=[];document.querySelectorAll('body *').forEach(e=>{const s=getComputedStyle(e);if(s.position==='fixed')return;const r=e.getBoundingClientRect();if(r.width>0&&r.right>W+2&&!e.closest('.panels,.marquee,.logos,.clients,.reel,.sreel,.strip,.mq,[class*=marq],[class*=track],.demos,.wa,.ticker')) over.push((e.className||e.tagName).toString().slice(0,40)+':'+Math.round(r.right))});
   const brokenImg=[...document.images].filter(i=>i.complete&&i.naturalWidth===0&&i.getAttribute('loading')!=='lazy').map(i=>i.src.slice(-40));
   return {sw:document.documentElement.scrollWidth,W,over:[...new Set(over)].slice(0,4),brokenImg}});
  if(errs.length||r.sw>r.W+1||r.over.length||r.brokenImg.length) out.push({f,w,errs:[...new Set(errs)].slice(0,5),sw:r.sw,over:r.over,bi:r.brokenImg});
  await p.close();}
 await ctx.close();}
fs.writeFileSync('qa.json',JSON.stringify(out,null,1));console.log(out.length);await b.close();})();
