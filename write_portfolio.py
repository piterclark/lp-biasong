
import pathlib

h = open("c:/Users/User/Documentos/lp-resultiva/portfolio.html", encoding="utf-8").read()[:10]
print("Current:", h[:30])

html = open(__file__, encoding="utf-8").read()
# Extract the HTML between HTMLSTART and HTMLEND markers
start = html.index("# HTMLSTART") + len("# HTMLSTART\n")
end = html.index("# HTMLEND")
content = html[start:end]

pathlib.Path("c:/Users/User/Documentos/lp-resultiva/portfolio.html").write_text(content, encoding="utf-8")
print(f"Written: {len(content)} bytes")

# HTMLSTART
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CREAT Studio &#8212; Landing Pages que Convertem</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#06080f; --bg1:#0a0d17; --bg2:#0f1220;
  --orange:#F97316; --blue:#5B8DEF;
  --white:#fff; --muted:rgba(255,255,255,.46); --border:rgba(255,255,255,.08);
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--white);font-family:Inter,-apple-system,sans-serif;overflow-x:hidden;line-height:1.6}
a{color:inherit;text-decoration:none}
canvas{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.5}
header{
  position:fixed;top:0;left:0;right:0;z-index:99;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 56px;height:72px;transition:background .3s,border-color .3s,backdrop-filter .3s;
  border-bottom:1px solid transparent;
}
header.s{background:rgba(6,8,15,.9);backdrop-filter:blur(20px);border-color:var(--border)}
.lname{font-size:16px;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.lname b{color:var(--orange);font-style:italic}
.ltag{font-size:9px;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
.ltag span{color:var(--orange)}
.hnav{display:flex;gap:32px;align-items:center}
.hnav a{font-size:12px;font-weight:500;color:var(--muted);letter-spacing:.06em;transition:color .2s}
.hnav a:hover{color:var(--white)}
.bh{height:38px;padding:0 22px;background:var(--orange);color:#fff;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;display:flex;align-items:center;border-radius:4px;transition:opacity .2s}
.bh:hover{opacity:.88}
.hero{position:relative;z-index:1;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:120px 56px 80px}
.badge{display:inline-flex;align-items:center;gap:10px;border:1px solid rgba(249,115,22,.3);border-radius:100px;padding:8px 20px;margin-bottom:48px;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--orange)}
.dot{width:6px;height:6px;border-radius:50%;background:var(--orange);animation:blink 2s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.hero h1{font-size:clamp(48px,7.5vw,100px);font-weight:800;line-height:1.03;letter-spacing:-.05em;max-width:1000px;margin-bottom:0}
.o{color:var(--orange)} .b{color:var(--blue)}
.hsub{font-size:clamp(17px,1.8vw,21px);color:var(--muted);max-width:560px;line-height:1.75;margin:28px auto 56px}
.hact{display:flex;gap:20px;justify-content:center;align-items:center;flex-wrap:wrap}
.bm{height:54px;padding:0 40px;background:var(--orange);color:#fff;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;display:flex;align-items:center;gap:10px;border-radius:5px;box-shadow:0 8px 32px rgba(249,115,22,.28);transition:box-shadow .2s,transform .2s}
.bm:hover{box-shadow:0 12px 48px rgba(249,115,22,.42);transform:translateY(-2px)}
.bg{font-size:13px;font-weight:500;color:var(--muted);transition:color .2s}
.bg:hover{color:var(--white)}
.stats{position:relative;z-index:1;display:flex;justify-content:center;border-top:1px solid var(--border);border-bottom:1px solid var(--border);background:var(--bg1)}
.stat{padding:44px 56px;border-right:1px solid var(--border);text-align:center;flex:1;max-width:280px}
.stat:last-child{border-right:0}
.sn{font-size:44px;font-weight:800;letter-spacing:-.04em;background:linear-gradient(135deg,var(--orange),var(--blue));-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:8px}
.sl{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.intro{position:relative;z-index:1;padding:120px 56px;text-align:center;max-width:900px;margin:0 auto}
.intro h2{font-size:clamp(32px,4vw,56px);font-weight:700;line-height:1.14;letter-spacing:-.035em;margin-bottom:24px}
.intro h2 em{font-style:normal;color:var(--orange)}
.intro p{font-size:18px;color:var(--muted);line-height:1.75;max-width:620px;margin:0 auto}
.port{position:relative;z-index:1;padding:0 56px 120px}
.plabel{text-align:center;font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--orange);margin-bottom:64px}
.pgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;max-width:1300px;margin:0 auto}
.pc{background:var(--bg1);border:1px solid var(--border);border-radius:16px;overflow:hidden;display:block;position:relative;transition:border-color .3s,transform .3s,box-shadow .3s}
.pc:hover{border-color:rgba(249,115,22,.4);transform:translateY(-6px);box-shadow:0 24px 64px rgba(0,0,0,.5),0 0 0 1px rgba(249,115,22,.08)}
.pi{height:240px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.glow{position:absolute;width:180px;height:180px;border-radius:50%;filter:blur(60px);opacity:.3;transition:opacity .3s}
.pc:hover .glow{opacity:.55}
.picon{position:relative;z-index:1;width:76px;height:76px;border-radius:20px;display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,.09);backdrop-filter:blur(10px)}
.picon svg{width:38px;height:38px}
.plive{position:absolute;top:14px;left:14px;z-index:2;font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:4px 12px;border-radius:100px;border:1px solid var(--orange);background:rgba(249,115,22,.12);color:var(--orange)}
.pb{padding:26px 30px 30px}
.pniche{font-size:10px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.ptitle{font-size:21px;font-weight:700;letter-spacing:-.02em;margin-bottom:12px}
.pdesc{font-size:14px;color:var(--muted);line-height:1.6;margin-bottom:22px}
.pcta{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--orange);transition:gap .2s}
.pc:hover .pcta{gap:14px}
.appr{position:relative;z-index:1;background:var(--bg1);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:120px 56px}
.ainner{max-width:1300px;margin:0 auto}
.ahd{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:end;margin-bottom:72px}
.ahd h2{font-size:clamp(32px,4vw,52px);font-weight:700;letter-spacing:-.03em;line-height:1.15}
.ahd h2 em{font-style:normal;color:var(--blue)}
.ahd p{font-size:16px;color:var(--muted);line-height:1.8}
.arows{border-top:1px solid var(--border)}
.arow{display:grid;grid-template-columns:80px 1fr;gap:32px;padding:44px 0;border-bottom:1px solid var(--border);align-items:start}
.anum{font-size:13px;font-weight:700;letter-spacing:.08em;color:var(--orange);font-family:monospace;padding-top:3px}
.ac h3{font-size:19px;font-weight:600;margin-bottom:8px;letter-spacing:-.01em}
.ac p{font-size:14px;color:var(--muted);line-height:1.7}
.cta{position:relative;z-index:1;padding:140px 56px;text-align:center;overflow:hidden}
.cta::before{content:"";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:800px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(249,115,22,.07) 0%,transparent 70%);pointer-events:none}
.ctac{position:relative;z-index:1;max-width:680px;margin:0 auto}
.cpre{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--orange);margin-bottom:28px}
.ctac h2{font-size:clamp(36px,5vw,68px);font-weight:800;letter-spacing:-.04em;line-height:1.08;margin-bottom:24px}
.ctac h2 em{font-style:normal;color:var(--orange)}
.ctac > p{font-size:18px;color:var(--muted);max-width:480px;margin:0 auto 52px;line-height:1.7}
.cacts{display:flex;gap:20px;justify-content:center;align-items:center;flex-wrap:wrap}
.cnote{margin-top:24px;font-size:12px;color:rgba(255,255,255,.22);letter-spacing:.06em}
footer{position:relative;z-index:1;background:var(--bg1);border-top:1px solid var(--border);padding:52px 56px;display:flex;align-items:center;justify-content:space-between}
footer p{font-size:12px;color:rgba(255,255,255,.2)}
@media(max-width:960px){.pgrid{grid-template-columns:1fr}.stats{flex-wrap:wrap}.stat{border-right:0;border-bottom:1px solid var(--border)}.ahd{grid-template-columns:1fr}}
@media(max-width:640px){header{padding:0 20px}.hnav{display:none}.hero,.port,.appr,.cta,footer{padding-left:20px;padding-right:20px}footer{flex-direction:column;gap:12px;text-align:center}}
</style>
</head>
<body>
<canvas id="cv"></canvas>
<header id="hdr">
  <div>
    <div class="lname">CR<b>EAT</b></div>
    <div class="ltag">Landing Pages <span>&bull;</span> Design que converte</div>
  </div>
  <div class="hnav">
    <a href="#port">Portf&#243;lio</a>
    <a href="#appr">Abordagem</a>
    <a href="#cta" class="bh">Falar agora &#8594;</a>
  </div>
</header>
<section class="hero">
  <div class="badge"><div class="dot"></div>Portf&#243;lio CREAT Studio</div>
  <h1>Cada nicho<br>tem sua <span class="o">linguagem.</span><br>N&#243;s <span class="b">falamos</span> todas.</h1>
  <p class="hsub">Landing pages constru&#237;das do zero para cada segmento.<br>Design limpo, copy que converte, resultado no caixa.</p>
  <div class="hact">
    <a href="#port" class="bm">Ver as p&#225;ginas <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
    <a href="#cta" class="bg">Quero uma assim &#8594;</a>
  </div>
</section>
<div class="stats">
  <div class="stat"><div class="sn">4+</div><div class="sl">Nichos ativos</div></div>
  <div class="stat"><div class="sn">100%</div><div class="sl">Sob medida</div></div>
  <div class="stat"><div class="sn">0x</div><div class="sl">Templates gen&#233;ricos</div></div>
  <div class="stat"><div class="sn">&infin;</div><div class="sl">Possibilidades</div></div>
</div>
<section class="intro">
  <h2>N&#227;o vendemos p&#225;ginas.<br>Vendemos <em>resultados.</em></h2>
  <p>Cada projeto come&#231;a com uma pergunta: o que precisa acontecer para o cliente do seu cliente dizer sim? A resposta vira a p&#225;gina.</p>
</section>
<section class="port" id="port">
  <div class="plabel">Portf&#243;lio // CREAT</div>
  <div class="pgrid">
    <a href="dentista/index.html" target="_blank" class="pc">
      <div class="pi" style="background:linear-gradient(135deg,#071418,#060f0c)">
        <div class="glow" style="background:#06b6d4"></div>
        <span class="plive">No ar</span>
        <div class="picon" style="background:rgba(6,182,212,.1)">
          <svg viewBox="0 0 40 40" fill="none" stroke="#06b6d4" stroke-width="1.5" stroke-linecap="round"><path d="M11 9C8 9 6 12 6 15c0 2.5 1 5.5 2 9l2 11h4l2-8h8l2 8h4l2-11c1-3.5 2-6.5 2-9 0-3-2-6-5-6-2 0-3.5.8-5 2-1.5-1.2-3-2-5-2z"/><path d="M15 15c1.5 1 3 1.5 5 1.5s3.5-.5 5-1.5" stroke-width="1.2"/></svg>
        </div>
      </div>
      <div class="pb">
        <div class="pniche">Sa&#250;de</div>
        <div class="ptitle">Cl&#237;nica Odontol&#243;gica</div>
        <p class="pdesc">Para dentistas e cl&#237;nicas. Foco em agendamento, confian&#231;a e autoridade local.</p>
        <span class="pcta">Abrir p&#225;gina <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
      </div>
    </a>
    <a href="salao/index.html" target="_blank" class="pc">
      <div class="pi" style="background:linear-gradient(135deg,#120a14,#0d0710)">
        <div class="glow" style="background:#a855f7"></div>
        <span class="plive">No ar</span>
        <div class="picon" style="background:rgba(168,85,247,.1)">
          <svg viewBox="0 0 40 40" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="28" r="4.5"/><line x1="16" y1="15" x2="32" y2="31"/><line x1="16" y1="25" x2="32" y2="9"/></svg>
        </div>
      </div>
      <div class="pb">
        <div class="pniche">Beleza</div>
        <div class="ptitle">Sal&#227;o de Beleza</div>
        <p class="pdesc">Para sal&#245;es e studios. Design aspiracional com agendamento direto integrado.</p>
        <span class="pcta">Abrir p&#225;gina <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
      </div>
    </a>
    <a href="advogado/index.html" target="_blank" class="pc">
      <div class="pi" style="background:linear-gradient(135deg,#130f00,#0c0900)">
        <div class="glow" style="background:#eab308"></div>
        <span class="plive">No ar</span>
        <div class="picon" style="background:rgba(234,179,8,.1)">
          <svg viewBox="0 0 40 40" fill="none" stroke="#eab308" stroke-width="1.5" stroke-linecap="round"><line x1="20" y1="5" x2="20" y2="35"/><line x1="10" y1="35" x2="30" y2="35"/><line x1="8" y1="11" x2="32" y2="11"/><path d="M8 11 L4 19 Q8 23 12 19 Z"/><path d="M32 11 L28 19 Q32 23 36 19 Z"/></svg>
        </div>
      </div>
      <div class="pb">
        <div class="pniche">Advocacia</div>
        <div class="ptitle">Escrit&#243;rio de Advocacia</div>
        <p class="pdesc">Para advogados. Luxo, autoridade e copy que captura clientes de alto valor.</p>
        <span class="pcta">Abrir p&#225;gina <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
      </div>
    </a>
    <a href="arborea/index.html" target="_blank" class="pc">
      <div class="pi" style="background:linear-gradient(135deg,#1a1a0f,#0f0f07)">
        <div class="glow" style="background:#a18c50"></div>
        <span class="plive">No ar</span>
        <div class="picon" style="background:rgba(161,140,80,.1)">
          <svg viewBox="0 0 40 40" fill="none" stroke="#a18c50" stroke-width="1.5" stroke-linecap="round"><rect x="14" y="5" width="12" height="30" rx="1"/><rect x="6" y="15" width="8" height="20" rx="1"/><rect x="26" y="15" width="8" height="20" rx="1"/><line x1="4" y1="35" x2="36" y2="35"/></svg>
        </div>
      </div>
      <div class="pb">
        <div class="pniche">Im&#243;veis</div>
        <div class="ptitle">Lan&#231;amento Imobili&#225;rio</div>
        <p class="pdesc">Para empreendimentos premium. Capta&#231;&#227;o de leads qualificados com design de luxo.</p>
        <span class="pcta">Abrir p&#225;gina <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
      </div>
    </a>
  </div>
</section>
<section class="appr" id="appr">
  <div class="ainner">
    <div class="ahd">
      <div>
        <div class="plabel" style="text-align:left;margin-bottom:20px">Nossa abordagem</div>
        <h2>Design que <em>pensa</em><br>antes de criar.</h2>
      </div>
      <p>Steve Jobs n&#227;o come&#231;ava pelo design. Come&#231;ava pela experi&#234;ncia que o usu&#225;rio deveria ter. N&#243;s tamb&#233;m. Cada p&#237;xel tem fun&#231;&#227;o. Cada palavra tem objetivo.</p>
    </div>
    <div class="arows">
      <div class="arow"><span class="anum">01 //</span><div class="ac"><h3>Diagn&#243;stico do nicho</h3><p>Antes de qualquer design, entendemos quem compra, o que trava a decis&#227;o e o que faz o cliente dizer sim. A p&#225;gina &#233; consequ&#234;ncia dessa an&#225;lise.</p></div></div>
      <div class="arow"><span class="anum">02 //</span><div class="ac"><h3>Copy e design integrados</h3><p>Texto e visual criados juntos. O design serve a mensagem. A mensagem potencializa o design. Nenhum existe sem o outro.</p></div></div>
      <div class="arow"><span class="anum">03 //</span><div class="ac"><h3>Entrega que funciona</h3><p>HTML puro, hospedado onde quiser, carregando em menos de 2 segundos. Sem plataforma, sem depend&#234;ncia, sem custo mensal.</p></div></div>
    </div>
  </div>
</section>
<section class="cta" id="cta">
  <div class="ctac">
    <div class="cpre">Pr&#243;ximo passo</div>
    <h2>Quer uma p&#225;gina<br>assim para <em>voc&#234;</em>?</h2>
    <p>Fale direto. Sem formul&#225;rio longo, sem reuni&#227;o de hora. Em 24h voc&#234; sabe o que &#233; poss&#237;vel.</p>
    <div class="cacts">
      <a href="https://wa.me/5511999999999" class="bm">Falar no WhatsApp <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      <a href="mailto:contato@creat.studio" class="bg">Enviar e-mail &#8594;</a>
    </div>
    <p class="cnote">Resposta r&#225;pida &bull; Sem enrola&#231;&#227;o &bull; Or&#231;amento gratuito</p>
  </div>
</section>
<footer>
  <div>
    <div class="lname">CR<b>EAT</b></div>
    <div class="ltag">Landing Pages <span>&bull;</span> Design que converte</div>
  </div>
  <p>&#169; 2026 CREAT Studio</p>
</footer>
<script>
window.addEventListener("scroll",function(){document.getElementById("hdr").classList.toggle("s",window.scrollY>40)});
(function(){
  var c=document.getElementById("cv"),ctx=c.getContext("2d");
  function sz(){c.width=window.innerWidth;c.height=window.innerHeight}
  sz();window.addEventListener("resize",sz);
  var pts=Array.from({length:55},function(){return{x:Math.random()*c.width,y:Math.random()*c.height,vx:(Math.random()-.5)*.28,vy:(Math.random()-.5)*.28,r:Math.random()*1.4+.4,col:Math.random()>.5?"249,115,22":"91,141,239"}});
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    pts.forEach(function(p){
      p.x+=p.vx;p.y+=p.vy;
      if(p.x<0||p.x>c.width)p.vx*=-1;
      if(p.y<0||p.y>c.height)p.vy*=-1;
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle="rgba("+p.col+",.55)";ctx.fill();
    });
    for(var i=0;i<pts.length;i++)for(var j=i+1;j<pts.length;j++){
      var dx=pts[i].x-pts[j].x,dy=pts[i].y-pts[j].y,d=Math.sqrt(dx*dx+dy*dy);
      if(d<110){ctx.beginPath();ctx.moveTo(pts[i].x,pts[i].y);ctx.lineTo(pts[j].x,pts[j].y);ctx.strokeStyle="rgba(255,255,255,"+(1-d/110)*.045+")";ctx.stroke();}
    }
    requestAnimationFrame(draw);
  }
  draw();
})();
</script>
</body>
</html>
# HTMLEND
