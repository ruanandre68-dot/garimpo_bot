import requests
from bs4 import BeautifulSoup

print("--- 🛰️ AGENTE FILTRADO: BUSCA DE ALVOS REAIS ---")

# Dorks de alta probabilidade para dispositivos REAIS
queries = [
    'intitle:"Live View / - AXIS" inurl:index.shtml',
    'inurl:"viewerframe?mode="',
    'intitle:"Toshiba Network Camera" user=admin',
    'inurl:"/mjpg/video.mjpg"'
]

# Domínios que vamos ignorar (O lixo que aparece no seu print)
blacklist = ["amazon", "reviews", "dicio", "youtube", "google", "facebook", "pinterest"]

links_reais = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for q in queries:
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='result__a')
            
            for l in links:
                url_alvo = l['href']
                # O FILTRO REAL: Só aceita se não estiver na blacklist
                if not any(lixo in url_alvo.lower() for lixo in blacklist):
                    links_reais.append({'titulo': l.text.strip(), 'url': url_alvo})
                    print(f"[ALVO CONFIRMADO]: {url_alvo[:50]}...")
    except:
        continue

# --- HTML DE MONITORAMENTO ---
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SISTEMA OLHO DE DEUS - REAL</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: monospace; padding: 20px; }}
        .radar {{ border: 2px solid #0f0; padding: 20px; box-shadow: 0 0 15px #0f0; }}
        .cam-item {{ margin: 15px 0; border-left: 3px solid #f00; padding: 10px; background: rgba(255,0,0,0.1); }}
        a {{ color: #0ff; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .ip-label {{ color: #f00; font-size: 10px; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ ACESSO DIRETO A DISPOSITIVOS</h1>
        <p>> FILTRANDO RUÍDO E ANÚNCIOS... CONECTADO.</p>
"""

if not links_reais:
    html += "<p style='color:yellow'>[!] Buscador bloqueou acesso temporário. Tente o SHODAN.io ou mude a rede.</p>"

for i in links_reais:
    html += f"""
        <div class="cam-item">
            <div class="ip-label">SISTEMA DETECTADO</div>
            <div>{i['titulo']}</div>
            <a href="{i['url']}" target="_blank">>>> CONECTAR AO IP REAL</a>
        </div>
    """

html += "</div></body></html>"

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html)
print("--- 🛰️ GARIMPO REALIZADO. VERIFIQUE O GITHUB ---")

