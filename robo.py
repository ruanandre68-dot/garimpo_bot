import requests
from bs4 import BeautifulSoup

print("Injetando o template de elite da loja...")

url = "https://lista.mercadolivre.com.br/notebook"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
LINK_AFILIADO = "https://meli.la/1VKV9Jd"

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    todos_h2 = sopa.find_all('h2')
    produtos_reais = []
    
    # Filtro super restritivo para tentar ignorar artigos de blog do rodapé
    string_filtros = ["Filtros", "Resultados", "Blog", "Dicas", "Como", "em 2024", "em 2025", "MacBook", "Melhores", "Marketing", "diferença", "guia", "trabalho"]
    for h2 in todos_h2:
        texto = h2.text.strip()
        if len(texto) > 15 and not any(palavra in texto for palavra in string_filtros):
            produtos_reais.append(texto)
    
    # Aqui entra o DESIGN DE ELITE (CSS e Tipografia Profissional)
    site_html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tech Elite | Ofertas de Notebooks Verificados</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
        <script src="https://kit.fontawesome.com/a62e3acae3.js" crossorigin="anonymous"></script>
        
        <style>
            :root { --main-yellow: #fff159; --main-blue: #3483fa; --dark-grey: #333; --light-grey: #666; --bg-grey: #f7f7f7; --card-bg: #ffffff; }
            body { font-family: 'Montserrat', sans-serif; background-color: var(--bg-grey); margin: 0; padding: 0; color: var(--dark-grey); }
            header { background-color: var(--main-yellow); padding: 25px 0; text-align: center; box-shadow: 0 3px 6px rgba(0,0,0,0.1); }
            header h1 { margin: 0; color: var(--dark-grey); font-size: 28px; font-weight: 700; letter-spacing: -0.5px; display: flex; align-items: center; justify-content: center; gap: 10px; }
            header .logo-icon { color: var(--dark-grey); font-size: 24px; }
            header p.sub { margin: 8px 0 0 0; color: var(--light-grey); font-size: 14px; font-weight: 400; }
            
            /* A grade de produtos dinâmicas (Mobile -> Desktop) */
            .vitrine { max-width: 1400px; margin: 50px auto; padding: 0 25px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
            
            /* Design do Card de Elite */
            .cartao { background-color: var(--card-bg); border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 6px 12px rgba(0,0,0,0.06); transition: transform 0.3s ease, box-shadow 0.3s ease; display: flex; flex-direction: column; justify-content: space-between; overflow: hidden; position: relative; border: 1px solid #eaeaea; }
            .cartao:hover { transform: translateY(-8px); box-shadow: 0 12px 24px rgba(0,0,0,0.12); }
            
            /* Elementos Visuais do Card */
            .badge-container { display: flex; justify-content: center; margin-bottom: 20px; }
            .etiqueta { background-color: #e6f0ff; color: var(--main-blue); padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
            .product-visual { height: 120px; background-color: var(--bg-grey); border-radius: 8px; margin-bottom: 25px; display: flex; align-items: center; justify-content: center; border: 1px dashed #d1d1d1; }
            .tech-icon { font-size: 60px; color: #b0b0b0; }
            
            .product-details { margin-bottom: 30px; text-align: left; }
            .titulo-produto { font-size: 16px; color: var(--dark-grey); margin: 0; font-weight: 500; line-height: 1.4; height: 45px; overflow: hidden; }
            .product-price-meta { font-size: 12px; color: var(--light-grey); margin: 5px 0 0 0; font-weight: 400; }
            
            /* O Botão de Elite Centralizado */
            .botao-comprar { background-color: var(--main-blue); color: white; text-decoration: none; padding: 15px 30px; border-radius: 8px; font-weight: 600; font-size: 15px; display: flex; align-items: center; justify-content: center; gap: 10px; width: 80%; margin: 0 auto; transition: background-color 0.3s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .botao-comprar:hover { background-color: #2968c8; }
            .btn-text { flex-grow: 1; text-align: center; }
            
            /* Responsividade */
            @media (max-width: 768px) { header h1 { font-size: 24px; } header p.sub { font-size: 13px; } .vitrine { gap: 20px; } .cartao { padding: 20px; } .product-visual { height: 100px; } .tech-icon { font-size: 50px; } }
        </style>
    </head>
    <body>
        <header>
            <h1><i class="fas fa-bolt logo-icon"></i> Tech Elite</h1>
            <p class="sub">As melhores oportunidades de notebooks rastreadas hoje</p>
        </header>
        <div class="vitrine">
    """
    
    # Gerando até 9 cartões de produtos
    for nome in produtos_reais[:9]:
        site_html += f"""
            <div class="cartao">
                <div class="card-content">
                    <div class="badge-container"><span class="etiqueta badge-new">Exclusivo: Oferta Verified</span></div>
                    <div class="product-visual">
                        <i class="fas fa-laptop tech-icon"></i>
                    </div>
                    <div class="product-details">
                        <h3 class="titulo-produto">{nome}</h3>
                        <p class="product-price-meta">Apenas no ML Full</p>
                    </div>
                </div>
                <a href="{LINK_AFILIADO}" class="botao-comprar" target="_blank">
                    <span class="btn-text">Ver Preço no Mercado Livre</span>
                    <i class="fas fa-arrow-right btn-icon"></i>
                </a>
            </div>
        """
        print(f"Adicionado à loja de elite: {nome}")
        
    site_html += """
        </div>
    </body>
    </html>
    """
    
    with open("index.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(site_html)
        
    print("Sucesso! O template de elite foi gerado. Pronta para envio.")
else:
    print("Erro de conexão.")

