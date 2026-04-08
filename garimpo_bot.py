import requests
from bs4 import BeautifulSoup
import time

print("--- ☣️ INICIANDO PROTOCOLO OSINT: GARIMPO FANTASMA ☣️ ---")
print("Escaneando a web em busca de vestígios digitais expostos...")

# A pesquisa assustadora (Google Dork para Open Directories de imagens/logs)
# NOTA: Usamos um User-Agent para o Google não nos bloquear imediatamente.
query = 'intitle:"index of" "dcim" | "logs" | "camera"'
url = f"https://www.google.com/search?q={query}&num=10"
headers = {{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}}

try:
    response = requests.get(url, headers=headers)
    links_encontrados = []

    if response.status_code == 200:
        sopa = BeautifulSoup(response.text, 'html.parser')
        # Encontrar os links reais nos resultados do Google
        for g in sopa.find_all('div', class_='tF2Cxc'):
            link = g.find('a')['href']
            titulo = g.find('h3').text
            if "google.com" not in link: # Ignorar links internos do Google
                links_encontrados.append({{'titulo': titulo, 'url': link}})
                print(f"[VESTÍGIO DETECTADO]: {{titulo[:30]}}...")
    else:
        print("❌ Acesso negado pelo Google (CAPTCHA necessário). Tente novamente mais tarde.")
        # Se falhar, geramos links de exemplo para o HTML funcionar
        links_encontrados = [
            {{'titulo': '⚠️ Exemplo de Logs Expostos', 'url': '# logs vazios'}},
            {{'titulo': '⚠️ Exemplo de Câmera IP', 'url': '# camera offline'}}
        ]

    # --- ENGENHARIA DO HTML ASSUSTADOR ---
    html_garimpo = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>PROTOCOLO GARIMPO FANTASMA v1.0</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
            body {{ background-color: #000; color: #0f0; font-family: 'Share Tech Mono', monospace; margin: 0; padding: 20px; overflow-x: hidden; }}
            
            /* Efeito de Scanline de TV Velha */
            body::before {{ content: " "; display: block; position: fixed; top: 0; left: 0; bottom: 0; right: 0; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06)); z-index: 10; background-size: 100% 2px, 3px 100%; pointer-events: none; }}
            
            h1 {{ text-align: center; color: #f00; text-shadow: 0 0 10px #f00; animation: glitch 1s linear infinite; font-size: 32px; }}
            @keyframes glitch{{ 2%,64%{{transform: translate(2px,0) skew(0deg);}} 4%,60%{{transform: translate(-2px,0) skew(0deg);}} 62%{{transform: translate(0,0) skew(5deg);}} }}
            
            .container {{ max-width: 900px; margin: 0 auto; border: 1px solid #0f0; padding: 20px; box-shadow: 0 0 20px rgba(0,255,0,0.2); background: rgba(0,20,0,0.5); }}
            .status {{ color: #ff0; text-align: center; margin-bottom: 30px; border-bottom: 1px dashed #0f0; padding-bottom: 10px; }}
            
            .data-item {{ background: rgba(0,255,0,0.05); border: 1px solid #0a0; padding: 15px; margin-bottom: 15px; transition: 0.3s; position: relative; overflow: hidden; }}
            .data-item:hover {{ background: rgba(0,255,0,0.15); border-color: #0f0; transform: scale(1.02); }}
            .data-item h3 {{ margin: 0 0 10px 0; font-size: 18px; color: #0f0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
            .data-item a {{ color: #ff0; text-decoration: none; font-size: 14px; word-break: break-all; }}
            .data-item a:hover {{ text-decoration: underline; color: #fff; }}
            
            /* Detalhe estético de "vazamento" */
            .data-item::after {{ content: "EXPOSED DATA"; position: absolute; top: 5px; right: -20px; background: red; color: white; font-size: 10px; padding: 2px 20px; transform: rotate(45deg); font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>BIO-DIGITAL SCAVENGER</h1>
            <div class="status">
                > STATUS: <span style="color:#f00">BUSCA FINALIZADA</span><br>
                > ALVOS DETECTADOS: {len(links_encontrados)}<br>
                > ATENÇÃO: Navegue por sua conta e risco. Não altere nada.
            </div>
            <div class="results">
    """

    for item in links_encontrados:
        html_garimpo += f"""
                <div class="data-item">
                    <h3>> {item['titulo']}</h3>
                    <a href="{item['url']}" target="_blank">{item['url']}</a>
                </div>
        """

    html_garimpo += """
            </div>
            <p style="text-align:center; color:#555; margin-top:30px;">[FIM DA TRANSMISSÃO - SISTEMA FANTASMA]</p>
        </div>
    </body>
    </html>
    """

    # Salvar o HTML do Garimpo
    with open("garimpo.html", "w", encoding="utf-8") as f:
        f.write(html_garimpo)

    print("--- ☣️ GARIMPO FINALIZADO. garimpo.html GERADO ☣️ ---")
    print("Mande para o GitHub para visualizar a colheita.")

except Exception as e:
    print(f"❌ Erro crítico no protocolo: {{e}}")

