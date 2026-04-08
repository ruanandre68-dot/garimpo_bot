import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse, parse_qs

print("--- 🛰️ AGENTE DESMASCARADOR: EXTRAINDO IPS REAIS ---")

queries = [
    'intitle:"Live View / - AXIS" inurl:index.shtml',
    'inurl:"viewerframe?mode="',
    'intitle:"Network Camera NetworkCamera"'
]

blacklist = ["amazon", "reviews", "dicio", "youtube", "google", "facebook", "pinterest", "ebay"]
links_finais = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for q in queries:
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='result__a')
            
            for l in links:
                url_suja = l['href']
                
                # A MÁGICA: Extrair o link real de dentro do link do DuckDuckGo
                if 'uddg=' in url_suja:
                    # Pega tudo que vem depois de 'uddg='
                    url_real = unquote(url_suja.split('uddg=')[1].split('&')[0])
                else:
                    url_real = url_suja

                # Filtro de Lixo
                if not any(lixo in url_real.lower() for lixo in blacklist):
                    if url_real.startswith('http'):
                        links_finais.append({'titulo': l.text.strip(), 'url': url_real})
                        print(f"[ALVO DESMASCARADO]: {url_real}")
    except:
        continue

# --- HTML DE MONITORAMENTO DE ELITE ---
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SISTEMA OLHO DE DEUS - IP REAL</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: 'Courier New', monospace; padding: 20px; }}
        .radar {{ border: 2px solid #0f0; padding: 20px; box-shadow: 0 0 15px #0f0; }}
        .cam-item {{ margin: 15px 0; border: 1px solid #f00; padding: 15px; background: rgba(255,0,0,0.05); }}
        .cam-item:hover {{ background: rgba(255,0,0,0.2); border-color: #ff0; }}
        a {{ color: #0ff; text-decoration: none; font-weight: bold; font-size: 16px; display: block; margin-top: 10px; }}
        .status {{ color: #f00; font-size: 12px; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ ACESSO DIRETO: INFRAESTRUTURA EXPOSTA</h1>
        <p>> LINKS DESMASCARADOS. CONEXÃO PONTO-A-PONTO.</p>
"""

for i in links_finais:
    # Mostra apenas o domínio ou IP para parecer mais "profissional"
    display_url = urlparse(i['url']).netloc
    html += f"""
        <div class="cam-item">
            <div class="status">[!] DISPOSITIVO DETECTADO EM: {display_url}</div>
            <div style="font-size: 14px; margin-top:5px;">{i['titulo']}</div>
            <a href="{i['url']}" target="_blank">>>> ABRIR TRANSMISSÃO AO VIVO</a>
        </div>
    """

html += "</div></body></html>"

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html)
print("--- 🛰️ GARIMPO REALIZADO. IPS EXTRAÍDOS. ---")

