import requests
from bs4 import BeautifulSoup

print("A iniciar a varredura por computadores portáteis...")

# Nova rota: procurar apenas portáteis (notebooks)
url = "https://lista.mercadolivre.com.br/notebook"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# O teu link de afiliado oficial
LINK_AFILIADO = "https://meli.la/1VKV9Jd"

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    todos_h2 = sopa.find_all('h2')
    produtos_reais = []
    
    # O filtro aprimorado para ignorar menus
    for h2 in todos_h2:
        texto = h2.text.strip()
        if len(texto) > 15 and "Filtros" not in texto and "Resultados" not in texto:
            produtos_reais.append(texto)
    
    # A construir uma página mais bonita (com botões e cores)
    site_html = "<html><head><meta charset='utf-8'><title>Montra de Portáteis</title></head><body style='font-family: Arial, sans-serif; padding: 20px;'>"
    site_html += "<h1 style='color: #0056b3;'>As Melhores Ofertas de Portáteis</h1>"
    site_html += "<p>Equipamentos selecionados automaticamente:</p><ul>"
    
    for nome in produtos_reais[:6]:
        site_html += f"<li style='margin-bottom: 25px; font-size: 18px; list-style: none;'><b>{nome}</b><br>"
        # Botão azul chamativo com o teu link
        site_html += f"<a href='{LINK_AFILIADO}' style='background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 8px;'>Ver Preço e Comprar</a></li>"
        print(f"Produto detetado: {nome}")
        
    site_html += "</ul></body></html>"
    
    with open("index.html", "w", encoding="utf-8") as ficheiro:
        ficheiro.write(site_html)
        
    print("Sucesso! O ficheiro index.html foi atualizado e está pronto a faturar.")
else:
    print("Erro de ligação.")

