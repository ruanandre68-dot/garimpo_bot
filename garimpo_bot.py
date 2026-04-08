import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse

print("--- ☣️ PROTOCOLO INDUSTRIAL: BUSCA DE ALVOS PRIVADOS ☣️ ---")
print("Escaneando galpões, fábricas e salas de servidores...")

# Dorks de Precisão: Focando no que está trancado (ou deveria estar)
queries = [
    'intitle:"Live View / - AXIS" "Warehouse"',
    'intitle:"Live View / - AXIS" "Factory"',
    'intitle:"Live View / - AXIS" "Office"',
    'intitle:"Live View / - AXIS" "Server Room"',
    'inurl:"/view/viewer_index.shtml" "Shop"',
    'inurl:"/mjpg/video.mjpg" "Industrial"'
]

# Filtro Anti-Lixo (Ignorar sites que não são câmeras)
blacklist = ["amazon", "ebay", "dicio", "reviews", "youtube", "google", "facebook", "pinterest", "reddit"]

links_finais = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for q in queries:
    print(f"[BUSCANDO]: {q}")
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='result__a')
            
            for l in links:
                url_suja = l['href']
                
                # Desmascarando o link real do DuckDuckGo
                if 'uddg=' in url_suja:
                    url_real = unquote(url_suja.split('uddg=')[1].split('&')[0])
                else:
                    url_real = url_suja

                # Aplicando Filtro de Elite
                if not any(lixo in url_real.lower() for lixo in blacklist):
                    if url_real.startswith('http'):
                        links_finais.append({'titulo': l.text.strip(), 'url': url_real})
                        print(f"[ALVO CONFIRMADO]: {url_real}")
    except:
        continue

# --- ENGENHARIA DO HTML (V3 - INDUSTRIAL DARK) ---
html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>SISTEMA OLHO DE DEUS - INDUSTRIAL</title>
    <style>
        body {{ background: #050505; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; }}
        .radar {{ border: 2px solid #ff0000; padding: 20px; box-shadow: 0 0 20px #500; background: rgba(10,0,0,0.9); }}
        h1 {{ color: #ff0000; text-shadow: 0 0 10px #f00; text-align: center; border-bottom: 2px solid #f00; padding-bottom: 10px; }}
        .item {{ margin: 20px 0; border: 1px solid #333; padding: 15px; background: #111; transition: 0.3s; }}
        .item:hover {{ border-color: #ff0; background: #1a1a1a; }}
        .status {{ color: #ff0; font-size: 11px; margin-bottom: 5px; }}
        a {{ color: #00ffff; text-decoration: none; font-weight: bold; font-size: 16px; word-break: break-all; }}
        .footer {{ text-align: center; color: #444; margin-top: 30px; font-size: 10px; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ MONITORAMENTO DE INFRAESTRUTURA PRIVADA</h1>
        <p style="text-align:center">> STATUS: CONEXÃO PONTO-A-PONTO ESTABELECIDA <</p>
"""

if not links_finais:
    html_content += "<p style='color:orange; text-align:center;'>[!] Nenhum galpão aberto detectado nesta frequência. Tente novamente em 5 min.</p>"

for i in links_finais:
    domain = urlparse(i['url']).netloc
    html_content += f"""
        <div class="item">
            <div class="status">[!] ALVO DETECTADO: {domain}</div>
            <div style="color:#aaa; font-size:14px;">{i['titulo']}</div>
            <a href="{i['url']}" target="_blank">>>> ACESSAR TRANSMISSÃO INDUSTRIAL</a>
        </div>
    """

html_content += """
        <div class="footer">AVISO: USO EXCLUSIVO PARA ESTUDOS DE SEGURANÇA DIGITAL.</div>
    </div>
</body>
</html>
"""

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"--- 🛰️ PROTOCOLO CONCLUÍDO. {len(links_finais)} ALVOS NO GARIMPO.HTML ---")

