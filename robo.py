import requests
from bs4 import BeautifulSoup

print("Iniciando a varredura financeira...")

# Vamos focar num nicho que você entende: equipamentos técnicos e biológicos
url = "https://lista.mercadolivre.com.br/lote-laboratorio-microscopio"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# O seu link de afiliado oficial
LINK_AFILIADO = "https://meli.la/1VKV9Jd"

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    todos_h2 = sopa.find_all('h2')
    produtos_reais = []
    
    for h2 in todos_h2:
        texto = h2.text.strip()
        # Filtro para pegar apenas produtos reais e ignorar menus
        if len(texto) > 15 and "Filtros" not in texto:
            produtos_reais.append(texto)
    
    site_html = "<html><head><meta charset='utf-8'><title>Vitrine Investigativa de Biologia</title></head><body>"
    site_html += "<h1 style='color: #2e7d32;'>Garimpo Técnico: Lotes e Equipamentos</h1>"
    site_html += "<p>Produtos selecionados via varredura automatizada.</p><ul>"
    
    # Gerando os links com a sua comissão
    for nome in produtos_reais[:8]:
        site_html += f"<li style='margin-bottom: 15px;'><b>{nome}</b><br>"
        site_html += f"<a href='{LINK_AFILIADO}' style='color: blue;'>Ver Preço e Detalhes na Loja Oficial</a></li>"
        print(f"Produto lucrativo detectado: {nome}")
        
    site_html += "</ul></body></html>"
    
    with open("index.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(site_html)
        
    print("Sucesso! Vitrine monetizada com seu link de afiliado.")
else:
    print("Erro de conexão.")

