
import pathlib

html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ferreira & Associados — Advocacia de Alto Padrao</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg:#080808; --bg-1:#0f0f0f; --bg-2:#141414;
      --gold:#c9a96e; --white:#f5f0e8; --muted:#888880; --dim:#333330; --border:#1e1e1c;
    }
    html { scroll-behavior: smooth; }
    body { background:var(--bg); color:var(--white); font-family:Inter,sans-serif; overflow-x:hidden; line-height:1.6; }
    a { color:inherit; text-decoration:none; }

    header {
      position:fixed; top:0; left:0; right:0; z-index:99;
      display:flex; align-items:center; justify-content:space-between;
      padding:0 60px; height:80px; background:rgba(8,8,8,0); transition:background .4s,height .4s;
    }
    header.scrolled { background:rgba(8,8,8,.96); backdrop-filter:blur(16px); height:68px; border-bottom:1px solid var(--border); }
    .lname { font-family:"Cormorant Garamond",serif; font-size:20px; font-weight:600; letter-spacing:.12em; text-transform:uppercase; }
    .lsub  { font-size:9px; font-weight:500; letter-spacing:.25em; text-transform:uppercase; color:var(--gold); }
    nav { display:flex; gap:36px; align-items:center; }
    nav a { font-size:11px; font-weight:500; letter-spacing:.18em; text-transform:uppercase; color:var(--muted); transition:color .2s; }
    nav a:hover { color:var(--white); }
    .bcta { height:40px; padding:0 28px; border:1px solid var(--gold); color:var(--gold); font-size:10px; font-weight:600; letter-spacing:.2em; text-transform:uppercase; display:flex; align-items:center; transition:background .2s,color .2s; }
    .bcta:hover { background:var(--gold); color:var(--bg); }

    .hero { position:relative; height:100vh; min-height:700px; display:flex; align-items:center; overflow:hidden; }
    .hslides { position:absolute; inset:0; }
    .hs {
      position:absolute; inset:0; background-size:cover; background-position:center;
      opacity:0; transition:opacity 1.8s ease-in-out;
    }
    .hs.on { opacity:1; animation:kb 14s ease-in-out infinite alternate; }
    @keyframes kb { from{transform:scale(1.06)} to{transform:scale(1) translate(-.5%,-.5%)} }
    .hs1 { background-image:url(https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1800&q=85); }
    .hs2 { background-image:url(https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1800&q=85); }
    .hs3 { background-image:url(https://images.unsplash.com/photo-1575505586569-646b2ca898fc?w=1800&q=85); }
    .hs4 { background-image:url(https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1800&q=85); }
    .hov { position:absolute; inset:0; background:linear-gradient(105deg,rgba(8,8,8,.9) 0%,rgba(8,8,8,.6) 50%,rgba(8,8,8,.25) 100%); }
    .hc  { position:relative; z-index:2; padding:0 60px; max-width:860px; }
    .hlb { display:flex; align-items:center; gap:16px; font-size:10px; font-weight:600; letter-spacing:.3em; text-transform:uppercase; color:var(--gold); margin-bottom:36px; }
    .hlb::before { content:""; display:block; width:40px; height:1px; background:var(--gold); }
    .hero h1 { font-family:"Cormorant Garamond",serif; font-size:clamp(44px,5.5vw,76px); font-weight:300; line-height:1.12; letter-spacing:-.01em; margin-bottom:28px; }
    .hero h1 em { font-style:italic; color:var(--gold); }
    .hdesc { font-size:16px; color:rgba(245,240,232,.7); max-width:520px; line-height:1.8; margin-bottom:52px; }
    .hact { display:flex; gap:20px; align-items:center; flex-wrap:wrap; }
    .bprim { height:52px; padding:0 40px; background:var(--gold); color:var(--bg); font-size:11px; font-weight:600; letter-spacing:.2em; text-transform:uppercase; display:flex; align-items:center; gap:12px; transition:background .2s; }
    .bprim:hover { background:#d4b87a; }
    .bgh { font-size:11px; font-weight:500; letter-spacing:.15em; text-transform:uppercase; color:rgba(245,240,232,.6); transition:color .2s; }
    .bgh:hover { color:var(--white); }
    .hdots { position:absolute; bottom:48px; left:60px; z-index:2; display:flex; gap:10px; }
    .hd { width:24px; height:2px; background:rgba(201,169,110,.3); cursor:pointer; transition:background .3s,width .3s; }
    .hd.on { width:48px; background:var(--gold); }
    .hscroll { position:absolute; bottom:48px; right:60px; z-index:2; font-size:9px; letter-spacing:.2em; text-transform:uppercase; color:var(--muted); writing-mode:vertical-rl; display:flex; align-items:center; gap:12px; }
    .hscroll::after { content:""; display:block; width:1px; height:60px; background:linear-gradient(to bottom,var(--gold),transparent); animation:sl 2s ease-in-out infinite; }
    @keyframes sl { 0%{opacity:1;transform:scaleY(1)} 100%{opacity:0;transform:scaleY(.5) translateY(20px)} }

    .creds { background:var(--bg-1); border-top:1px solid var(--border); border-bottom:1px solid var(--border); padding:56px 60px; display:grid; grid-template-columns:repeat(4,1fr); }
    .cred { padding:0 40px; border-right:1px solid var(--border); text-align:center; }
    .cred:first-child { padding-left:0; text-align:left; }
    .cred:last-child  { border-right:0; }
    .cn { font-family:"Cormorant Garamond",serif; font-size:52px; font-weight:300; color:var(--gold); line-height:1; margin-bottom:8px; }
    .cn sup { font-size:24px; vertical-align:super; }
    .cl { font-size:11px; font-weight:500; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); }

    .sobre { padding:120px 60px; display:grid; grid-template-columns:1fr 1fr; gap:100px; align-items:center; max-width:1400px; margin:0 auto; }
    .stag { font-size:10px; font-weight:600; letter-spacing:.3em; text-transform:uppercase; color:var(--gold); margin-bottom:24px; display:flex; align-items:center; gap:16px; }
    .stag::before { content:""; display:block; width:32px; height:1px; background:var(--gold); }
    .sobre h2 { font-family:"Cormorant Garamond",serif; font-size:clamp(34px,3.5vw,50px); font-weight:400; line-height:1.2; margin-bottom:32px; }
    .sobre h2 em { font-style:italic; color:var(--gold); }
    .sobre p { font-size:15px; color:var(--muted); line-height:1.9; margin-bottom:20px; }
    .sobre p strong { color:var(--white); font-weight:500; }
    .simg { position:relative; }
    .simg img { width:100%; height:560px; object-fit:cover; filter:brightness(.85); display:block; }
    .simg::before { content:""; position:absolute; top:-20px; left:-20px; right:20px; bottom:20px; border:1px solid var(--gold); opacity:.3; z-index:-1; }

    .areas { padding:120px 60px; background:var(--bg-1); border-top:1px solid var(--border); border-bottom:1px solid var(--border); }
    .ahd { max-width:1400px; margin:0 auto 72px; display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:end; }
    .ahd h2 { font-family:"Cormorant Garamond",serif; font-size:clamp(34px,3.5vw,52px); font-weight:300; line-height:1.15; }
    .ahd h2 em { font-style:italic; color:var(--gold); }
    .ahd p { font-size:15px; color:var(--muted); line-height:1.8; }
    .agrid { max-width:1400px; margin:0 auto; display:grid; grid-template-columns:repeat(3,1fr); gap:2px; }
    .ac { background:var(--bg-2); padding:48px 40px; border:1px solid var(--border); position:relative; overflow:hidden; transition:background .3s,border-color .3s; cursor:default; }
    .ac::before { content:""; position:absolute; bottom:0; left:0; width:0; height:2px; background:var(--gold); transition:width .4s; }
    .ac:hover { background:#181816; border-color:#333330; }
    .ac:hover::before { width:100%; }
    .an { font-family:"Cormorant Garamond",serif; font-size:13px; color:var(--gold); opacity:.6; margin-bottom:28px; letter-spacing:.1em; }
    .ac h3 { font-family:"Cormorant Garamond",serif; font-size:24px; font-weight:500; margin-bottom:16px; }
    .ac p { font-size:13.5px; color:var(--muted); line-height:1.7; }

    .proc { padding:120px 60px; max-width:1400px; margin:0 auto; }
    .phd { margin-bottom:72px; display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:end; }
    .phd h2 { font-family:"Cormorant Garamond",serif; font-size:clamp(34px,3.5vw,52px); font-weight:300; line-height:1.15; }
    .phd h2 em { font-style:italic; color:var(--gold); }
    .phd p { font-size:15px; color:var(--muted); line-height:1.8; }
    .steps { display:grid; grid-template-columns:repeat(4,1fr); border-top:1px solid var(--border); }
    .step { padding:52px 40px 52px 0; border-right:1px solid var(--border); }
    .step:last-child { border-right:0; padding-right:0; }
    .snum { font-family:"Cormorant Garamond",serif; font-size:56px; font-weight:300; color:var(--gold); opacity:.25; line-height:1; margin-bottom:24px; }
    .step h4 { font-size:15px; font-weight:600; letter-spacing:.04em; margin-bottom:12px; }
    .step p { font-size:13.5px; color:var(--muted); line-height:1.7; }

    .dep { background:var(--bg-1); border-top:1px solid var(--border); border-bottom:1px solid var(--border); padding:120px 60px; text-align:center; position:relative; overflow:hidden; }
    .dep::before { content:"\\201C"; position:absolute; top:-40px; left:50%; transform:translateX(-50%); font-family:"Cormorant Garamond",serif; font-size:320px; color:var(--gold); opacity:.04; line-height:1; pointer-events:none; }
    .dep blockquote { position:relative; font-family:"Cormorant Garamond",serif; font-size:clamp(24px,3vw,36px); font-weight:300; font-style:italic; line-height:1.5; max-width:860px; margin:0 auto 40px; }
    .dep cite { font-size:11px; font-weight:600; letter-spacing:.2em; text-transform:uppercase; color:var(--gold); font-style:normal; }
    .dep cite span { display:block; font-weight:400; letter-spacing:.1em; color:var(--muted); margin-top:6px; }

    .ctas { padding:140px 60px; text-align:center; position:relative; overflow:hidden; }
    .ctabg { position:absolute; inset:0; background-image:url(https://images.unsplash.com/photo-1486325212027-8081e485255e?w=1800&q=80); background-size:cover; background-position:center; opacity:.07; }
    .ctac { position:relative; z-index:1; max-width:700px; margin:0 auto; }
    .ctac h2 { font-family:"Cormorant Garamond",serif; font-size:clamp(36px,4.5vw,60px); font-weight:300; line-height:1.2; margin-bottom:24px; }
    .ctac h2 em { font-style:italic; color:var(--gold); }
    .ctac p { font-size:16px; color:var(--muted); line-height:1.8; max-width:540px; margin:0 auto 52px; }
    .cact { display:flex; gap:24px; justify-content:center; align-items:center; flex-wrap:wrap; }
    .cnote { margin-top:28px; font-size:12px; color:var(--dim); letter-spacing:.08em; }

    footer { background:var(--bg-1); border-top:1px solid var(--border); padding:80px 60px 40px; }
    .ftop { display:grid; grid-template-columns:1.5fr 1fr 1fr 1fr; gap:48px; padding-bottom:64px; border-bottom:1px solid var(--border); margin-bottom:40px; }
    .fb p { font-size:13px; color:var(--muted); line-height:1.7; margin-top:16px; max-width:280px; }
    .fc h4 { font-size:10px; font-weight:600; letter-spacing:.2em; text-transform:uppercase; color:var(--gold); margin-bottom:24px; }
    .fc a { display:block; font-size:13px; color:var(--muted); margin-bottom:12px; transition:color .2s; }
    .fc a:hover { color:var(--white); }
    .fbot { display:flex; justify-content:space-between; align-items:center; }
    .fbot p { font-size:12px; color:var(--dim); }

    @media(max-width:1024px){
      .sobre,.ahd,.phd{grid-template-columns:1fr;gap:40px;}
      .agrid{grid-template-columns:repeat(2,1fr);}
      .steps{grid-template-columns:repeat(2,1fr);}
      .creds{grid-template-columns:repeat(2,1fr);gap:32px;}
      .ftop{grid-template-columns:1fr 1fr;}
    }
    @media(max-width:768px){
      header{padding:0 24px;} nav{display:none;}
      .hc{padding:0 24px;}
      .creds,.sobre,.areas,.proc,.dep,.ctas,footer{padding-left:24px;padding-right:24px;}
      .agrid,.steps{grid-template-columns:1fr;}
      .creds{grid-template-columns:1fr 1fr;}
      .hdots{left:24px;} .hscroll{display:none;}
      .ftop{grid-template-columns:1fr;}
    }
  </style>
</head>
<body>

<header id="hdr">
  <div>
    <div class="lname">Ferreira &amp; Associados</div>
    <div class="lsub">Advocacia &amp; Consultoria Jur&#237;dica</div>
  </div>
  <nav>
    <a href="#sobre">Sobre</a>
    <a href="#areas">&#193;reas</a>
    <a href="#proc">Como Trabalhamos</a>
    <a href="#contato" class="bcta">Consulta Gratuita</a>
  </nav>
</header>

<section class="hero">
  <div class="hslides">
    <div class="hs hs1 on"></div>
    <div class="hs hs2"></div>
    <div class="hs hs3"></div>
    <div class="hs hs4"></div>
  </div>
  <div class="hov"></div>
  <div class="hc">
    <div class="hlb">Ferreira &amp; Associados &middot; Desde 2008</div>
    <h1>O direito que<br>voc&#234; merece,<br><em>defendido com rigor.</em></h1>
    <p class="hdesc">Mais de 15 anos protegendo patrim&#244;nios, empresas e fam&#237;lias com precis&#227;o jur&#237;dica e comprometimento absoluto com o resultado.</p>
    <div class="hact">
      <a href="#contato" class="bprim">Falar com um advogado <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      <a href="#areas" class="bgh">Ver especialidades &#8594;</a>
    </div>
  </div>
  <div class="hdots">
    <div class="hd on" data-i="0"></div>
    <div class="hd" data-i="1"></div>
    <div class="hd" data-i="2"></div>
    <div class="hd" data-i="3"></div>
  </div>
  <div class="hscroll">Scroll</div>
</section>

<div class="creds">
  <div class="cred"><div class="cn">15<sup>+</sup></div><div class="cl">Anos de experi&#234;ncia</div></div>
  <div class="cred"><div class="cn">98<sup>%</sup></div><div class="cl">Taxa de &#234;xito nos casos</div></div>
  <div class="cred"><div class="cn">2.4<sup>k</sup></div><div class="cl">Clientes atendidos</div></div>
  <div class="cred"><div class="cn">6</div><div class="cl">&#193;reas de especializa&#231;&#227;o</div></div>
</div>

<section class="sobre" id="sobre">
  <div>
    <div class="stag">Sobre o escrit&#243;rio</div>
    <h2>Experi&#234;ncia que faz a <em>diferen&#231;a</em> no seu caso.</h2>
    <p>Fundado em 2008, o escrit&#243;rio Ferreira &amp; Associados consolidou-se como refer&#234;ncia em <strong>advocacia empresarial e patrimonial</strong>. Nossa abordagem combina profundo conhecimento t&#233;cnico com vis&#227;o estrat&#233;gica voltada para resultados.</p>
    <p>N&#227;o somos um escrit&#243;rio de volume. Cada caso recebe <strong>aten&#231;&#227;o personalizada</strong> de um advogado s&#234;nior responsável do in&#237;cio ao fim &#8212; sem repassar seu processo para estagi&#225;rios.</p>
    <p>Atuamos com discri&#231;&#227;o, agilidade e total transpar&#234;ncia. Voc&#234; sempre sabe onde seu processo est&#225;.</p>
  </div>
  <div class="simg">
    <img src="https://images.unsplash.com/photo-1555374018-13a8994ab246?w=800&q=85" alt="Escrit&#243;rio">
  </div>
</section>

<section class="areas" id="areas">
  <div class="ahd">
    <div>
      <div class="stag">&#193;reas de atua&#231;&#227;o</div>
      <h2>Expertise onde voc&#234; mais <em>precisa.</em></h2>
    </div>
    <p>Equipes especializadas que dominam cada aspecto do seu segmento. N&#227;o fazemos tudo &#8212; fazemos muito bem o que importa para o seu caso.</p>
  </div>
  <div class="agrid">
    <div class="ac"><div class="an">01</div><h3>Direito Empresarial</h3><p>Contratos, fus&#245;es, aquisi&#231;&#245;es, reestrutura&#231;&#245;es societ&#225;rias e prote&#231;&#227;o do neg&#243;cio em todas as fases do crescimento.</p></div>
    <div class="ac"><div class="an">02</div><h3>Direito Tribut&#225;rio</h3><p>Planejamento fiscal, defesa em autua&#231;&#245;es, recupera&#231;&#227;o de cr&#233;ditos tribut&#225;rios e compliance para empresas de todos os portes.</p></div>
    <div class="ac"><div class="an">03</div><h3>Direito Civil e Fam&#237;lia</h3><p>Div&#243;rcio, invent&#225;rios, planejamento sucess&#243;rio e prote&#231;&#227;o patrimonial para voc&#234; e sua fam&#237;lia, com total discri&#231;&#227;o.</p></div>
    <div class="ac"><div class="an">04</div><h3>Direito Trabalhista</h3><p>Defesa de empresas em a&#231;&#245;es trabalhistas, reestrutura&#231;&#227;o de passivos e consultoria preventiva para evitar lit&#237;gios.</p></div>
    <div class="ac"><div class="an">05</div><h3>Direito Imobili&#225;rio</h3><p>Due diligence, contratos de compra e venda, loca&#231;&#245;es comerciais, regulariza&#231;&#227;o de im&#243;veis e gest&#227;o de ativos.</p></div>
    <div class="ac"><div class="an">06</div><h3>Contencioso Estrat&#233;gico</h3><p>Lit&#237;gios de alta complexidade, arbitragem e media&#231;&#227;o &#8212; quando o volume financeiro justifica a melhor defesa poss&#237;vel.</p></div>
  </div>
</section>

<section class="proc" id="proc">
  <div class="phd">
    <div>
      <div class="stag">Como trabalhamos</div>
      <h2>M&#233;todo claro.<br><em>Resultado certo.</em></h2>
    </div>
    <p>Da primeira conversa &#224; resolu&#231;&#227;o final, voc&#234; sabe exatamente o que esperar &#8212; sem surpresas, sem promessas vazias. S&#243; estrat&#233;gia bem executada.</p>
  </div>
  <div class="steps">
    <div class="step"><div class="snum">01</div><h4>Consulta inicial</h4><p>Reuni&#227;o confidencial para entender seu caso. Sem custo, sem compromisso. Voc&#234; sai com clareza sobre o caminho jur&#237;dico ideal.</p></div>
    <div class="step"><div class="snum">02</div><h4>Diagn&#243;stico e estrat&#233;gia</h4><p>An&#225;lise aprofundada, levantamento de riscos e elabora&#231;&#227;o de uma estrat&#233;gia personalizada para seu caso espec&#237;fico.</p></div>
    <div class="step"><div class="snum">03</div><h4>Execu&#231;&#227;o precisa</h4><p>Advogado s&#234;nior dedicado ao seu processo, com atualiza&#231;&#245;es regulares e total acesso para tirar d&#250;vidas a qualquer momento.</p></div>
    <div class="step"><div class="snum">04</div><h4>Resolu&#231;&#227;o e prote&#231;&#227;o</h4><p>Conclus&#227;o do caso e implementa&#231;&#227;o de medidas preventivas para que o mesmo problema nunca se repita.</p></div>
  </div>
</section>

<section class="dep">
  <blockquote>&#8220;O escrit&#243;rio Ferreira &amp; Associados n&#227;o apenas ganhou meu processo &#8212; reorganizou toda a estrutura jur&#237;dica da minha empresa. S&#227;o anos de parceria que meu neg&#243;cio n&#227;o sobreviveria sem.&#8221;</blockquote>
  <cite>Ricardo M.<span>CEO &#8212; Grupo Meridian Investimentos</span></cite>
</section>

<section class="ctas" id="contato">
  <div class="ctabg"></div>
  <div class="ctac">
    <div class="stag" style="justify-content:center">Primeira consulta gratuita</div>
    <h2>Seu problema tem<br><em>solu&#231;&#227;o jur&#237;dica.</em></h2>
    <p>Fale com um advogado s&#234;nior hoje. Sem enrola&#231;&#227;o, sem promessas imposs&#237;veis &#8212; s&#243; clareza sobre o que pode ser feito pelo seu caso.</p>
    <div class="cact">
      <a href="https://wa.me/5511999999999" class="bprim">Falar no WhatsApp <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      <a href="tel:+5511999999999" class="bcta">Ligar agora</a>
    </div>
    <p class="cnote">Atendimento seg&#8211;sex, 8h&#8211;19h &middot; Sigilo absoluto garantido</p>
  </div>
</section>

<footer>
  <div class="ftop">
    <div class="fb">
      <div class="lname">Ferreira &amp; Associados</div>
      <div class="lsub">Advocacia &amp; Consultoria Jur&#237;dica</div>
      <p>Escrit&#243;rio especializado em direito empresarial, tribut&#225;rio e patrimonial. S&#227;o Paulo, SP.</p>
    </div>
    <div class="fc"><h4>&#193;reas</h4><a href="#areas">Direito Empresarial</a><a href="#areas">Direito Tribut&#225;rio</a><a href="#areas">Direito Civil e Fam&#237;lia</a><a href="#areas">Direito Trabalhista</a><a href="#areas">Direito Imobili&#225;rio</a></div>
    <div class="fc"><h4>Escrit&#243;rio</h4><a href="#sobre">Sobre n&#243;s</a><a href="#proc">Como trabalhamos</a><a href="#contato">Contato</a></div>
    <div class="fc"><h4>Contato</h4><a href="https://wa.me/5511999999999">WhatsApp</a><a href="tel:+5511999999999">(11) 9 9999-9999</a><a href="#">Av. Paulista, 1000 &middot; S&#227;o Paulo</a></div>
  </div>
  <div class="fbot">
    <p>&#169; 2026 Ferreira &amp; Associados Advocacia. OAB/SP 000.000.</p>
    <p>Todos os direitos reservados.</p>
  </div>
</footer>

<script>
window.addEventListener("scroll",function(){document.getElementById("hdr").classList.toggle("scrolled",window.scrollY>60);});
(function(){
  var s=document.querySelectorAll(".hs"),d=document.querySelectorAll(".hd"),c=0,t;
  function go(n){s[c].classList.remove("on");d[c].classList.remove("on");c=n;s[c].classList.add("on");d[c].classList.add("on");}
  function nx(){go((c+1)%s.length);}
  function st(){t=setInterval(nx,6000);}
  function rs(){clearInterval(t);st();}
  d.forEach(function(x){x.addEventListener("click",function(){go(parseInt(x.dataset.i));rs();});});
  st();
})();
</script>
</body>
</html>'''

dest = pathlib.Path("c:/Users/User/Documentos/lp-resultiva/advogado/index.html")
dest.write_text(html, encoding="utf-8")
print(f"OK: {len(html)} bytes")
