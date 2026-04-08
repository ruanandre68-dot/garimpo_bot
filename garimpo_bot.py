import requests
from bs4 import BeautifulSoup

print("--- ☣️ INICIANDO PROTOCOLO OSINT: GARIMPO FANTASMA ☣️ ---")

query = 'intitle:"index of" "dcim" | "logs"'
url = f"https://www.google.com/search?q={query}&num=10"

# CORREÇÃO AQUI: Chaves simples no dicionário
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
    response = requests.get(url, headers=headers)
    links_encontrados = []

    if response.status_code == 200:
        sopa = BeautifulSoup(response.text, 'html.parser')
        for g in sopa.find_all('div', class_='yuRUbf'): # Classe atualizada do Google
            a_tag = g.find('a')
            if a_tag:
                link = a_tag['href']
                titulo = g.find('h3').text if g.find('h3') else "Sem Título"
                links_encontrados.append({'titulo': titulo, 'url': link})
                print(f"[VESTÍGIO]: {titulo[:30]}...")
    
    # Se o Google bloquear, usamos alvos de treinamento
    if not links_encontrados:
        links_encontrados = [
            {'titulo': '⚠️ Servidor Protegido (Captcha)', 'url': 'https://www.google.com/search?q=index+of+logs'},
            {'titulo': '⚠️ Diretório de Treinamento', 'url': 'http://testphp.vulnweb.com/'}
        ]

    # HTML com chaves duplas apenas no CSS (obrigatório para f-strings)
    html_garimpo = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>GARIMPO FANTASMA</title>
        <style>
            body {{ background: #000; color: #0f0; font-family: monospace; padding: 20px; }}
            .box {{ border: 1px solid #0f0; padding: 15px; background: rgba(0,20,0,0.8); }}
            h1 {{ color: #f00; text-shadow: 0 0 5px #f00; }}
            .item {{ margin: 10px 0; padding: 10px; border-bottom: 1px solid #050; }}
            a {{ color: #ff0; text-decoration: none; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>BIO-DIGITAL SCAVENGER</h1>
            <p>> ESCANEAMENTO CONCLUÍDO. ALVOS:</p>
    """

    for item in links_encontrados:
        html_garimpo += f"""
            <div class="item">
                <div style="font-weight:bold">> {item['titulo']}</div>
                <a href="{item['url']}" target="_blank">{item['url']}</a>
            </div>
        """

    html_garimpo += "</div></body></html>"

    with open("garimpo.html", "w", encoding="utf-8") as f:
        f.write(html_garimpo)
    print("--- ☣️ SUCESSO: garimpo.html gerado ---")

except Exception as e:
    print(f"Erro: {e}")

