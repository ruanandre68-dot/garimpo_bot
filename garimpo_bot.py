import requests
from bs4 import BeautifulSoup

print("--- 🛰️ INICIANDO PROTOCOLO: SNIPER DE TRANSMISSÃO ---")
print("Buscando fluxos de vídeo ao vivo e painéis AXIS...")

# As Dorks de precisão para câmeras reais
queries = [
    'intitle:"Live View / - AXIS"',
    'inurl:"/view/viewer_index.shtml"',
    'intitle:"Network Camera NetworkCamera"',
    'inurl:"/mjpg/video.mjpg"'
]

links_finais = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for q in queries:
    # Usando DuckDuckGo para evitar bloqueios rápidos
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            # Pega os resultados do DuckDuckGo
            links = sopa.find_all('a', class_='result__a')
            for l in links[:5]: 
                links_finais.append({'titulo': l.text.strip(), 'url': l['href']})
                print(f"[ALVO]: {l.text[:40]}...")
    except:
        continue

# --- HTML DE MONITORAMENTO ---
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SISTEMA OLHO DE DEUS</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: monospace; padding: 20px; }}
        .radar {{ border: 2px solid #0f0; padding: 20px; box-shadow: 0 0 15px #0f0; }}
        .cam-item {{ margin: 15px 0; border-left: 3px solid #f00; padding: 10px; background: rgba(255,0,0,0.05); }}
        a {{ color: #0ff; text-decoration: none; font-weight: bold; }}
        h1 {{ color: #f00; text-shadow: 0 0 5px #f00; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ FEED DE VÍDEO DETECTADO</h1>
        <p>> ESCANEANDO FREQUÊNCIAS...</p>
"""

for i in links_finais:
    html += f"""
        <div class="cam-item">
            <div style="color:#0f0">> CANAL: {i['titulo']}</div>
            <a href="{i['url']}" target="_blank">CONECTAR AO FLUXO DE VÍDEO</a>
        </div>
    """

html += "</div></body></html>"

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html)
print("--- 🛰️ PROTOCOLO CONCLUÍDO. garimpo.html GERADO ---")

