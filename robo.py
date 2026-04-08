import requests
from bs4 import BeautifulSoup

print("Construindo a loja com design premium...")

url = "https://lista.mercadolivre.com.br/notebook"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
LINK_AFILIADO = "https://meli.la/1VKV9Jd"

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    todos_h2 = sopa.find_all('h2')
    produtos_reais = []
    
    # Filtro ainda mais inteligente para fugir dos blogs do rodapé
    for h2 in todos_h2:
        texto = h2.text.strip()
        if len(texto) > 15 and not any(palavra in texto for palavra in ["Filtros", "Resultados", "Blog", "Dicas", "Como"]):
            produtos_reais.append(texto)
    
    # Aqui entra o Design Profissional (CSS Embutido)
    site_html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Garimpo Tech | Ofertas Verificadas</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #ebebeb; margin: 0; padding: 0; }
            header { background-color: #fff159; padding: 20px 0; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-bottom: 1px solid #e6e6e6; }
            h1 { margin: 0; color: #333; font-size: 26px; }
            p.sub { margin: 5px 0 0 0; color: #666; font-size: 15px; }
            
            /* A grade de produtos estilo loja */
            .vitrine { max-width: 1200px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; }
            
            /* O visual de cada produto */
            .cartao { background-color: #ffffff; border-radius: 8px; padding: 25px 20px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
            .cartao:hover { transform: translateY(-5px); box-shadow: 0 8px 16px rgba(0,0,0,0.15); }
            
            .etiqueta { background-color: #e6f0ff; color: #3483fa; padding: 5px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; margin-bottom: 15px; display: inline-block; }
            .titulo-produto { font-size: 16px; color: #333; margin-bottom: 25px; line-height: 1.4; font-weight: 500; height: 45px; overflow: hidden; }
            
            /* O botão azul centralizado */
            .botao-comprar { background-color: #3483fa; color: white; text-decoration: none; padding: 14px 20px; border-radius: 6px; font-weight: 600; font-size: 15px; display: block; width: 80%; margin: 0 auto; transition: background-color 0.3s; }
            .botao-comprar:hover { background-color: #2968c8; }
        </style>
    </head>
    <body>
        <header>
            <h1>⚡ Garimpo Tech</h1>
            <p class="sub">As melhores oportunidades de notebooks rastreadas hoje</p>
        </header>
        <div class="vitrine">
    """
    
    # Gerando até 6 cartões de produtos
    for nome in produtos_reais[:6]:
        site_html += f"""
            <div class="cartao">
                <div>
                    <span class="etiqueta">Oferta do Robô</span>
                    <div class="titulo-produto">{nome}</div>
                </div>
                <a href="{LINK_AFILIADO}" class="botao-comprar" target="_blank">Ver Preço no Mercado Livre</a>
            </div>
        """
        print(f"Adicionado à loja: {nome}")
        
    site_html += """
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(site_html)
        
    print("Sucesso! A loja premium foi gerada. Pronta para envio.")
else:
    print("Erro de conexão.")

