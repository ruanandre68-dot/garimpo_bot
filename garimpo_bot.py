import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse

print("--- 🛰️ PROTOCOLO: ZONAS DE SOMBRA (ORIENTE MÉDIO / ÁFRICA) ---")
print("Escaneando infraestrutura em regiões de baixa proteção...")

# Dorks com filtros de países (AE=Emirados, TR=Turquia, EG=Egito, NG=Nigéria, ZA=África do Sul)
queries = [
    'intitle:"Live View / - AXIS" site:.ae', # Emirados Árabes (Riqueza/Petróleo)
    'intitle:"Live View / - AXIS" site:.tr', # Turquia (Indústrias)
    'intitle:"Live View / - AXIS" site:.eg', # Egito (Logística)
    'intitle:"Live View / - AXIS" site:.ng', # Nigéria (Exploração)
    'intitle:"Live View / - AXIS" site:.za', # África do Sul (Mineração)
    'inurl:"viewerframe?mode=" site:.jo'     # Jordânia
]

blacklist = ["amazon", "ebay", "dicio", "reviews", "youtube", "google", "facebook", "pinterest", "reddit", "blog"]
links_finais = []
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}

for q in queries:
    print(f"[SCANNING REGION]: {q.split('.')[-1]}")
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers, timeout=12)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='result__a')
            
            for l in links:
                url_suja = l['href']
                if 'uddg=' in url_suja:
                    url_real = unquote(url_suja.split('uddg=')[1].split('&')[0])
                else:
                    url_real = url_suja

                if not any(lixo in url_real.lower() for lixo in blacklist):
                    if url_real.startswith('http'):
                        links_finais.append({'titulo': l.text.strip(), 'url': url_real})
                        print(f"[ALVO CONFIRMADO]: {url_real}")
    except:
        continue

# --- GERADOR DE PAINEL DE MONITORAMENTO ---
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SCANNER GLOBAL - ZONAS DE SOMBRA</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: 'Courier New', monospace; padding: 20px; }}
        .radar {{ border: 2px solid #f00; padding: 20px; box-shadow: 0 0 20px #f00; background: rgba(20,0,0,0.9); }}
        h1 {{ color: #f00; text-align: center; text-shadow: 0 0 10px #f00; }}
        .item {{ border-left: 4px solid #f00; padding: 15px; margin: 15px 0; background: #111; }}
        a {{ color: #0ff; text-decoration: none; font-size: 16px; font-weight: bold; }}
        .geo {{ color: #ff0; font-size: 11px; text-transform: uppercase; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ GLOBAL SHADOW MONITORING</h1>
        <p style="text-align:center">> ALVOS FILTRADOS POR REGIÃO GEOPOLÍTICA <</p>
"""

for i in links_finais:
    domain = urlparse(i['url']).netloc
    html_content += f"""
        <div class="item">
            <div class="geo">REGIÃO DETECTADA: {domain.split('.')[-1]}</div>
            <div style="color:#eee; margin: 5px 0;">{i['titulo']}</div>
            <a href="{i['url']}" target="_blank">>>> ACESSAR TRANSMISSÃO REMOTA</a>
        </div>
    """

html_content += "</div></body></html>"

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"--- 🛰️ CONCLUÍDO: {len(links_finais)} DISPOSITIVOS ENCONTRADOS ---")

