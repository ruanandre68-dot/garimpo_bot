import requests
from bs4 import BeautifulSoup

print("--- 🛰️ INICIANDO PROTOCOLO: OLHO DE DEUS ---")
print("Buscando transmissões e diretórios não protegidos...")

# Dorks assustadoras: Câmeras IP (Live View) e Backups de Banco de Dados
queries = [
    'inurl:"view/view.shtml"', # Câmeras de segurança abertas
    'intitle:"index of" "password.txt" | "config.php"', # Arquivos de senha esquecidos
    'intitle:"index of" "backup" "sql"' # Backups de bancos de dados
]

links_finais = []
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}

for q in queries:
    # Usando o DuckDuckGo (Mais "amigável" para o nosso garimpo)
    url = f"https://duckduckgo.com/html/?q={q}"
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            sopa = BeautifulSoup(res.text, 'html.parser')
            links = sopa.find_all('a', class_='result__a')
            for l in links[:3]: # Pega os 3 melhores de cada categoria
                links_finais.append({'titulo': l.text, 'url': l['href']})
                print(f"[ALVO DETECTADO]: {l.text[:40]}...")
    except:
        continue

# --- HTML DE ELITE (ESTILO MATRIX/TERMINAL) ---
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SISTEMA DE MONITORAMENTO FANTASMA</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: 'Courier New'; padding: 20px; text-transform: uppercase; }}
        .radar {{ border: 2px solid #0f0; padding: 20px; box-shadow: 0 0 20px #0f0; }}
        h1 {{ color: #f00; font-size: 20px; border-bottom: 2px solid #f00; padding-bottom: 10px; }}
        .item {{ margin: 20px 0; border-left: 3px solid #f00; padding-left: 10px; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} 100% {{ opacity: 1; }} }}
        a {{ color: #0ff; text-decoration: none; font-size: 12px; }}
        .warning {{ color: #ff0; font-size: 10px; margin-top: 40px; border: 1px dashed #ff0; padding: 10px; }}
    </style>
</head>
<body>
    <div class="radar">
        <h1>☣️ ALVOS DETECTADOS NA REDE MUNDIAL</h1>
        <p>> ESCANEAMENTO DE INFRAESTRUTURA COMPLETO...</p>
"""

for i in links_finais:
    html += f"""
        <div class="item">
            <div style="font-weight:bold; color: #0f0;">> DETECTADO: {i['titulo']}</div>
            <a href="{i['url']}" target="_blank">ACESSAR TRANSMISSÃO / DIRETÓRIO</a>
        </div>
    """

html += """
        <div class="warning">
            AVISO: O acesso a sistemas de terceiros sem autorização é ilegal. 
            Este robô serve apenas para fins de estudo de segurança cibernética (OSINT).
        </div>
    </div>
</body>
</html>
"""

with open("garimpo.html", "w", encoding="utf-8") as f:
    f.write(html)
print("--- 🛰️ GARIMPO CONCLUÍDO COM SUCESSO ---")

