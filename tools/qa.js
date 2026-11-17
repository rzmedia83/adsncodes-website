const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const [w,n] of [[390,'m'],[1366,'d']]){const p=await b.newPage({viewport:{width:w,height:800}});
await p.goto('http://localhost:8811/insights-best-ecommerce-development-companies-dubai.html',{waitUntil:'networkidle'});
const o=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);console.log(n,'overflow',o);
await p.screenshot({path:`qa-ec-${n}.png`,fullPage:false});}
await b.close();})();
