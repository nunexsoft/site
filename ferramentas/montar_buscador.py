"""Monta buscador/index.html reaproveitando o estilo, os ícones e o rodapé
do index.html principal — a página do Buscador NF-e NuneX fica com a mesma
cara do site do NuneXSoft. Mudou o estilo do site? Rode de novo:

    python ferramentas/montar_buscador.py
"""

from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parent.parent
base = (RAIZ / "index.html").read_text(encoding="utf-8")

estilo = re.search(r"<style>.*?</style>", base, re.S).group(0)
sprite = re.search(r'<svg[^>]*style="display:none"[^>]*>.*?</svg>|<svg[^>]*aria-hidden="true"[^>]*>\s*<symbol.*?</svg>',
                   base, re.S).group(0)
rodape = re.search(r"<footer.*?</footer>", base, re.S).group(0)
script = re.search(r"<script>\s*// menu no celular.*?</script>", base, re.S).group(0)

# o rodapé e o resto apontam para img/ — daqui é ../img/
rodape = rodape.replace('src="img/', 'src="../img/')

DOWNLOAD = "https://github.com/nunexsoft/site/releases/download/buscador-v1.0/Buscador-NFe-NuneX-Setup.exe"
ZAP = "https://wa.me/5533991740421?text="
MSG = {
    "conhecer": "Ol%C3%A1!%20Quero%20conhecer%20o%20Buscador%20NF-e%20NuneX.",
    "mensal": "Ol%C3%A1!%20Quero%20assinar%20o%20Buscador%20NF-e%20NuneX%20(mensal).",
    "anual": "Ol%C3%A1!%20Quero%20assinar%20o%20Buscador%20NF-e%20NuneX%20(anual).",
    "cliente": "Ol%C3%A1!%20Sou%20cliente%20NuneXSoft%20e%20quero%20o%20Buscador%20NF-e.",
}

pagina = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Buscador NF-e NuneX — notas de compra direto da SEFAZ, com XML e DANFE</title>
<meta name="description" content="Receba sozinho, direto da SEFAZ, as notas fiscais de compra emitidas contra o CNPJ da sua empresa: XML, DANFE em PDF e planilha. Notas antigas pelo e-mail, exportação para o contador. 7 dias grátis.">
<link rel="canonical" href="https://nunexsoft.com.br/buscador/">
<meta name="theme-color" content="#012454">
<link rel="icon" type="image/png" sizes="32x32" href="../img/icone-32.png">
<link rel="apple-touch-icon" href="../img/icone-celular.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="NuneXSoft">
<meta property="og:title" content="Buscador NF-e NuneX — notas de compra direto da SEFAZ">
<meta property="og:description" content="XML e DANFE das suas compras chegando sozinhos, sem esperar o e-mail do fornecedor. 7 dias grátis.">
<meta property="og:url" content="https://nunexsoft.com.br/buscador/">
<meta property="og:image" content="https://nunexsoft.com.br/img/buscador-painel.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,600;0,800;1,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<script type="application/ld+json">
{{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Buscador NF-e NuneX",
  "operatingSystem": "Windows 10, Windows 11", "applicationCategory": "BusinessApplication",
  "offers": [{{"@type": "Offer", "name": "Mensal", "price": "39.90", "priceCurrency": "BRL"}},
             {{"@type": "Offer", "name": "Anual", "price": "399.00", "priceCurrency": "BRL"}}],
  "publisher": {{"@type": "Organization", "name": "Team Fenix - NuneXSoft", "url": "https://nunexsoft.com.br/"}}}}
</script>
{estilo}
<style>
.regra{{max-width:860px;margin:28px auto 0;border:3px solid #d29922;background:#fff8e6;border-radius:14px;padding:18px 22px;color:#3a2a00}}
.regra b.t{{display:block;color:#a86b00;font-family:Montserrat,sans-serif;font-size:1.15rem;margin-bottom:6px}}
.tabela-origem{{width:100%;border-collapse:collapse;margin-top:18px;background:#fff;border-radius:12px;overflow:hidden}}
.tabela-origem th,.tabela-origem td{{padding:12px 14px;border-bottom:1px solid #e3e8f0;text-align:left;vertical-align:top}}
.tabela-origem th{{background:#012454;color:#fff}}
.planos.tres{{grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}}
</style>
</head>
<body>
{sprite}

<header>
  <div class="wrap topo">
    <a class="logo" href="../" aria-label="NuneXSoft — início"><img src="../img/icone-180.png" alt="" width="46" height="46"><span class="marca">Nune<span class="x">X</span>Soft<small>Brasil</small></span></a>
    <nav id="menu" aria-label="Menu principal">
      <ul>
        <li><a href="#recursos">O que faz</a></li>
        <li><a href="#antigas">Notas antigas</a></li>
        <li><a href="#telas">Telas</a></li>
        <li><a href="#planos">Planos</a></li>
        <li><a href="#baixar">Baixar</a></li>
        <li><a href="#duvidas">Dúvidas</a></li>
        <li><a href="../">NuneXSoft</a></li>
      </ul>
    </nav>
    <a class="btn btn-zap" href="{ZAP}{MSG['conhecer']}" target="_blank" rel="noopener"><svg><use href="#i-zap"/></svg>Falar no WhatsApp</a>
    <button class="menu-btn" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false"><svg><use href="#i-menu"/></svg></button>
  </div>
</header>

<main id="inicio">

<section class="hero">
  <div class="wrap grade">
    <div>
      <span class="chapeu">Buscador NF-e NuneX</span>
      <p class="pergunta">Esperando o fornecedor mandar o XML da nota por e-mail? Ou ele esqueceu de mandar?</p>
      <h1>As suas notas de compra chegam sozinhas.</h1>
      <p class="sub">Direto da SEFAZ: o <b>XML</b>, o <b>DANFE em PDF</b> e uma planilha de todas as notas emitidas contra o CNPJ da sua empresa — muitas vezes antes da mercadoria chegar.</p>
      <div class="acoes">
        <a class="btn btn-baixar" href="#baixar"><svg><use href="#i-baixar"/></svg>Testar 7 dias grátis</a>
        <a class="btn btn-borda" href="#planos">Ver planos e preços</a>
      </div>
      <ul class="selos">
        <li><svg><use href="#i-ok"/></svg>7 dias grátis, sem cadastro</li>
        <li><svg><use href="#i-ok"/></svg>Notas antigas pelo e-mail</li>
        <li><svg><use href="#i-ok"/></svg>Suporte pelo AnyDesk</li>
      </ul>
    </div>
    <div class="palco">
      <div class="tela">
        <div class="barra"><i></i><i></i><i></i></div>
        <img src="../img/buscador-painel.webp" alt="Tela principal do Buscador NF-e NuneX com as notas de compra" width="1280" height="820" fetchpriority="high">
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="regra">
      <b class="t">⏱ Busca automática: uma vez por hora</b>
      A SEFAZ permite <b>uma consulta por hora</b> para cada empresa — consultar mais que isso bloqueia o computador.
      Por isso o Buscador busca <b>sozinho, de hora em hora</b>, sem ninguém precisar clicar. Chegou nota nova, aparece um aviso perto do relógio do Windows.
    </div>
  </div>
</section>

<section class="sec" id="recursos">
  <div class="wrap">
    <div class="titulo">
      <span class="chapeu">O que faz</span>
      <h2>Tudo o que o contador e o estoque precisam</h2>
    </div>
    <div class="cards">
      <div class="card"><div class="ico"><svg><use href="#i-baixar"/></svg></div><h3>XML direto da SEFAZ</h3><p>Com o certificado digital A1 da empresa, as notas de compra chegam sem depender do fornecedor.</p></div>
      <div class="card"><div class="ico"><svg><use href="#i-fiado"/></svg></div><h3>DANFE em PDF</h3><p>Cada nota já vem com o DANFE pronto: dois cliques e você confere a mercadoria.</p></div>
      <div class="card"><div class="ico"><svg><use href="#i-grafico"/></svg></div><h3>Painel do mês</h3><p>Quantas notas, total comprado, notas aguardando e canceladas — por mês ou entre datas.</p></div>
      <div class="card"><div class="ico"><svg><use href="#i-contador"/></svg></div><h3>Para o contador</h3><p>Escolha o período e exporte um .zip com os XMLs e a planilha, pronto para mandar.</p></div>
      <div class="card"><div class="ico"><svg><use href="#i-ok"/></svg></div><h3>Ciência automática</h3><p>Quando a SEFAZ entrega só o resumo, o Buscador avisa a SEFAZ e o XML completo chega em seguida.</p></div>
      <div class="card"><div class="ico"><svg><use href="#i-cadeado"/></svg></div><h3>Seguro</h3><p>A senha do certificado fica cifrada pelo próprio Windows. Suas notas ficam no seu computador.</p></div>
    </div>
  </div>
</section>

<section class="sec cinza" id="antigas">
  <div class="wrap">
    <div class="titulo">
      <span class="chapeu">Notas antigas</span>
      <h2>Precisa das notas de janeiro? Tem jeito.</h2>
      <p>A SEFAZ só entrega os últimos 90 dias — é regra dela, igual para todos os programas. Mas o fornecedor é obrigado a mandar o XML ao comprador, e quase sempre manda por e-mail. O Buscador busca lá.</p>
    </div>
    <div style="overflow-x:auto">
    <table class="tabela-origem">
      <tr><th>De onde</th><th>Até quando</th><th>Como</th></tr>
      <tr><td><b>SEFAZ</b></td><td>últimos 90 dias</td><td>Sozinho, de hora em hora. Na primeira vez traz os 90 dias inteiros.</td></tr>
      <tr><td><b>E-mail da empresa</b></td><td>qualquer época</td><td>Você escolhe o período (ex.: 01/01 a 15/02) e o Buscador lê os XMLs anexos — sem apagar nem marcar nada.</td></tr>
      <tr><td><b>Pasta do computador</b></td><td>qualquer época</td><td>Downloads, pendrive, a pasta do contador: ele procura e junta tudo.</td></tr>
    </table>
    </div>
  </div>
</section>

<section class="sec" id="telas">
  <div class="wrap">
    <div class="titulo">
      <span class="chapeu">Veja por dentro</span>
      <h2>Telas do Buscador</h2>
      <p>Clique numa tela para ver maior.</p>
    </div>
    <div class="galeria">
      <figure><img src="../img/buscador-painel.webp" alt="Painel com as notas de compra do mês" width="1280" height="820" loading="lazy"><figcaption><b>Painel</b>As notas do mês, total comprado e situação.</figcaption></figure>
      <figure><img src="../img/buscador-periodo.webp" alt="Filtro por período com datas de e até" width="1280" height="820" loading="lazy"><figcaption><b>Período</b>Este mês, mês passado ou entre datas.</figcaption></figure>
      <figure><img src="../img/buscador-notas-antigas.webp" alt="Busca de notas antigas pelo e-mail da empresa" width="900" height="878" loading="lazy"><figcaption><b>Notas antigas</b>Pelo e-mail, no período que você escolher.</figcaption></figure>
      <figure><img src="../img/buscador-configuracoes.webp" alt="Configuração do certificado digital A1" width="930" height="1053" loading="lazy"><figcaption><b>Configuração</b>Escolha o certificado A1 e pronto.</figcaption></figure>
      <figure><img src="../img/buscador-assinatura.webp" alt="Tela da assinatura com QR Code do Mercado Pago" width="562" height="653" loading="lazy"><figcaption><b>Assinatura</b>Pague pelo QR Code e ative na hora.</figcaption></figure>
    </div>
  </div>
</section>

<section class="sec cinza" id="planos">
  <div class="wrap">
    <div class="titulo">
      <span class="chapeu">Planos</span>
      <h2>Comece com 7 dias grátis</h2>
      <p>Instale, use tudo por 7 dias sem pagar nada. Gostou? Escolha o plano. Todos com o programa completo para 1 computador.</p>
    </div>
    <div class="planos tres">
      <div class="plano">
        <h3>Mensal</h3>
        <p class="desc">Pague mês a mês, sem fidelidade.</p>
        <div class="preco"><small>por mês</small><br><b>R$ 39,90</b></div>
        <ul>
          <li><svg><use href="#i-ok"/></svg>Notas da SEFAZ de hora em hora</li>
          <li><svg><use href="#i-ok"/></svg>Notas antigas pelo e-mail</li>
          <li><svg><use href="#i-ok"/></svg>Suporte pelo WhatsApp e AnyDesk</li>
        </ul>
        <a class="btn btn-borda" href="{ZAP}{MSG['mensal']}" target="_blank" rel="noopener">Quero o mensal</a>
      </div>
      <div class="plano destaque">
        <span class="selo">2 meses grátis</span>
        <h3>Anual</h3>
        <p class="desc">Um ano inteiro pagando 10 meses.</p>
        <div class="preco"><small>por ano</small><br><b>R$ 399,00</b></div>
        <ul>
          <li><svg><use href="#i-ok"/></svg>Tudo do plano mensal</li>
          <li><svg><use href="#i-ok"/></svg>Economia de R$ 79,80</li>
          <li><svg><use href="#i-ok"/></svg>Sem se preocupar todo mês</li>
        </ul>
        <a class="btn btn-zap" href="{ZAP}{MSG['anual']}" target="_blank" rel="noopener"><svg><use href="#i-zap"/></svg>Quero o anual</a>
      </div>
      <div class="plano">
        <h3>Cliente NuneXSoft</h3>
        <p class="desc">Já usa o NuneXSoft? Tem desconto.</p>
        <div class="preco"><small>por mês</small><br><b>R$ 29,90</b></div>
        <div class="mensal">ou <b>R$ 299,00</b> por ano</div>
        <ul>
          <li><svg><use href="#i-ok"/></svg>Tudo do plano mensal</li>
          <li><svg><use href="#i-ok"/></svg>Os XMLs prontos para a entrada de mercadorias</li>
        </ul>
        <a class="btn btn-borda" href="{ZAP}{MSG['cliente']}" target="_blank" rel="noopener">Sou cliente NuneXSoft</a>
      </div>
    </div>
    <p style="text-align:center;margin-top:18px">Atendimento avulso: <b>R$ 50,00</b> por atendimento, quando você precisar.</p>
  </div>
</section>

<section class="sec cinza" id="baixar">
  <div class="wrap baixar">
    <a class="btn btn-baixar" href="{DOWNLOAD}"><svg><use href="#i-baixar"/></svg>Baixar o Buscador NF-e NuneX</a>
    <p class="baixar-info">Versão <b>1.0</b> · <b>7 dias grátis</b> · Windows 10 ou 11 (64 bits) · instalador de cerca de 46 MB</p>
    <p class="baixar-dica">Rode o <b>Buscador-NFe-NuneX-Setup.exe</b>. Se o Windows mostrar “O Windows protegeu o computador”, clique em <b>Mais informações</b> e depois em <b>Executar assim mesmo</b>. Você vai precisar do <b>certificado digital A1</b> da empresa (arquivo .pfx) e da senha dele — normalmente o contador tem. Na dúvida, <a href="{ZAP}{MSG['conhecer']}" target="_blank" rel="noopener">chame a gente no WhatsApp</a> que instalamos para você.</p>
  </div>
</section>

<section class="sec" id="duvidas">
  <div class="wrap">
    <div class="titulo">
      <span class="chapeu">Dúvidas</span>
      <h2>Perguntas frequentes</h2>
    </div>
    <div class="faq">
      <details><summary>Preciso de certificado digital?</summary><p>Sim, o certificado A1 da empresa (arquivo .pfx), o mesmo que o contador usa. O certificado A3 (cartão ou token) não é aceito: ele precisa ficar conectado e pede senha, o que impede a busca automática.</p></details>
      <details><summary>Por que só uma busca por hora?</summary><p>É regra da SEFAZ: mais de uma consulta por hora para a mesma empresa bloqueia o computador por um tempo. O Buscador respeita isso sozinho e busca de hora em hora, sem ninguém precisar clicar.</p></details>
      <details><summary>Consigo as notas de meses atrás?</summary><p>A SEFAZ só entrega os últimos 90 dias. As notas mais antigas o Buscador traz do e-mail da empresa (o fornecedor manda o XML a cada venda) ou de uma pasta do computador, no período que você escolher.</p></details>
      <details><summary>O que acontece depois dos 7 dias grátis?</summary><p>As buscas param até você assinar — mas as notas que já chegaram continuam no programa para ver, abrir e exportar. Assinou, volta tudo na hora.</p></details>
      <details><summary>Como pago e ativo?</summary><p>Na própria tela do Buscador: escolha o plano, pague pelo Mercado Pago (tem QR Code), mande o comprovante e o código do computador pelo WhatsApp e cole a chave que você recebe.</p></details>
      <details><summary>Funciona com o NuneXSoft?</summary><p>Sim. O NuneXSoft já importa o XML da nota do fornecedor na entrada de mercadorias — com o Buscador, o XML já está no computador quando a mercadoria chega. E cliente NuneXSoft paga menos.</p></details>
      <details><summary>Aparecem as notas de venda da minha loja?</summary><p>Não: o Buscador é para as notas de <b>compra</b>, emitidas contra o CNPJ da sua empresa.</p></details>
    </div>
  </div>
</section>

</main>

{rodape}

<a class="zap-flutua" href="{ZAP}{MSG['conhecer']}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp"><svg><use href="#i-zap"/></svg></a>

<dialog id="zoom"><button type="button">Fechar ✕</button><img alt=""></dialog>

{script}
</body>
</html>
"""

destino = RAIZ / "buscador" / "index.html"
destino.parent.mkdir(exist_ok=True)
destino.write_text(pagina, encoding="utf-8")
print(f"ok: {destino} ({len(pagina) // 1024} KB)")
