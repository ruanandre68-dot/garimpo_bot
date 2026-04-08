import requests
from bs4 import BeautifulSoup

print("Iniciando a varredura profunda...")
url = "https://lista.mercadolivre.com.br/lote-pecas"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    
    # Busca os títulos dos produtos (o Mercado Livre geralmente usa a tag h2 para os nomes)
    produtos = sopa.find_all('h2')
    
    # Começa a montar a estrutura do seu site
    site_html = "<html><head><meta charset='utf-8'><title>Vitrine Fantasma</title></head><body>"
    site_html += "<h1>Achados do Robô - Lotes e Peças</h1><ul>"
    
    # Pega os 5 primeiros resultados e coloca na lista do site
    for produto in produtos[:5]:
        nome = produto.text
        # Aqui, no futuro, entrará o seu link de afiliado
        site_html += f"<li><b>{nome}</b> - <a href='#'>Comprar (Link Afiliado)</a></li>"
        print(f"Alvo detectado: {nome}")
        
    site_html += "</ul></body></html>"
    
    # Salva tudo no arquivo que será a sua página na internet
    with open("index.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(site_html)
        
    print("Sucesso! Arquivo 'index.html' gerado. A sua vitrine base está pronta.")
else:
    print("Acesso negado. Código:", resposta.status_code)

