import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import time

print("--- 🛰️ PROTOCOLO: DEEP SCAN V5 (SNIPER CAMUFLADO) ---")

# Dorks que miram em falhas de login e roteadores de galpões
queries = [
    'intitle:"index of" "inurl:ftp" "password"',
    'intitle:"Network Camera" inurl:/view/viewer_index.shtml',
    'intitle:"toshiba network camera" inurl:user=admin',
    'inurl:"/control/userget.htm"'
]

links_finais = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0'}

for q in queries:
    print(f"[ESCANEANDO]: {q[:30]}...")
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='result__a')
            
            for l in links:
                url_suja = l['href']
                if 'uddg=' in url_suja:
                    url_real = unquote(url_suja.split('uddg=')[1].split('&')[0])
                else:
                    url_real = url_suja

                # Filtro de sites de segurança (que explicam como hackear mas não são a camera)
                if "shodan" not in url_real and "exploit-db" not in url_real:
                    if url_real.startswith('http'):
                        links_finais.append({'titulo': l.text.strip(), 'url': url_real})
                        print(f"[ALVO]: {url_real[:50]}...")
        
        # Pausa para não ser bloqueado (O segredo do garimpo silencioso)
        time.sleep(2) 
    except:
        continue

# --- HTML DE MONITORAMENTO ---
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SISTEMA OLHO DE DEUS - DEEP SCAN</title>
    <style>
        body {{ background: #050505; color: #0f0; font-family: 'Courier New', monospace; padding: 20px; }}
        .radar {{ border: 2px solid #0f0; padding: 20px; box-shadow: 0 0 20px #0f0; }}
        h1 {{ color: #f00; text-align: center; text-transform: uppercase; }}
        .item {{ border: 1px solid #0f0; padding: 15px; margin: 15px 0; background: rgba(0,255,0,0.05); }}
        a {{ color: #0ff; text-decoration: none; font-weight: bold; }}
        .warning {{ color: red; font-size: 10px; border: 1px solid red; padding: 10px; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ MONITORAMENTO DE REDES EXPOSTAS</h1>
        <p style="text-align:center">> STATUS: {len(links_finais)} DISPOSITIVOS DETECTADOS <</p>
"""

for i in links_finais:
    html_content += f"""
        <div class="item">
            <div>IDENTIFICADO: {i['titulo'][:60]}</div>
            <a href="{i['url']}" target="_blank">>>> TENTAR CONEXÃO REMOTA</a>
        </div>
    """

html_content += """
        <div class="warning">AVISO: O acesso não autorizado é ilegal. Use apenas para fins educacionais.</div>
    </div>
</body>
</html>
"""

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"--- 🛰️ CONCLUÍDO. {len(links_finais)} ALVOS NO GARIMPO.HTML ---")

