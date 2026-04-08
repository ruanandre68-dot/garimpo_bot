import requests

print("Gerando Landing Page de Elite - Notebook Dell...")

LINK_AFILIADO = "https://meli.la/1VKV9Jd"

# Aqui desenhamos o site com CSS artístico direto
site_html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oferta Exclusiva | Dell Inspiron 15</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/a62e3acae3.js" crossorigin="anonymous"></script>
    <style>
        body {{
            margin: 0; padding: 0; font-family: 'Poppins', sans-serif;
            background: linear-gradient(135th, #1a2a6c, #b21f1f, #fdbb2d);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
        }}
        @keyframes gradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        .container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            max-width: 500px;
            width: 90%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            text-align: center;
            border: 1px solid rgba(255,255,255,0.3);
        }}
        h1 {{ color: #1a2a6c; font-weight: 800; margin-bottom: 10px; }}
        .badge {{
            background: #ff4b2b; color: white; padding: 5px 15px;
            border-radius: 50px; font-size: 12px; font-weight: 600; text-transform: uppercase;
        }}
        .specs-grid {{
            display: grid; grid-template-columns: 1fr; gap: 10px; margin: 30px 0; text-align: left;
        }}
        .spec-item {{
            padding: 12px; border-radius: 10px; display: flex; align-items: center; gap: 15px;
            font-size: 14px; color: #444; font-weight: 500;
            background: #f8f9fa; border-left: 5px solid #1a2a6c;
        }}
        .spec-item i {{ color: #1a2a6c; width: 20px; }}
        .btn-comprar {{
            display: block; background: #3483fa; color: white; text-decoration: none;
            padding: 20px; border-radius: 15px; font-weight: 700; font-size: 18px;
            transition: 0.3s; box-shadow: 0 10px 20px rgba(52, 131, 250, 0.3);
        }}
        .btn-comprar:hover {{ transform: scale(1.05); background: #2968c8; }}
    </style>
</head>
<body>
    <div class="container">
        <span class="badge">Oportunidade Única</span>
        <h1>Notebook Dell Inspiron i15</h1>
        <p style="color: #666;">Intel Core i5 (13ª Geração) | 512GB SSD | 8GB RAM</p>
        
        <div class="specs-grid">
            <div class="spec-item" style="border-color: #4facfe;"><i class="fas fa-microchip"></i> Processador Intel Core i5-1334U</div>
            <div class="spec-item" style="border-color: #00f2fe;"><i class="fab fa-windows"></i> Windows 11 Home Edition</div>
            <div class="spec-item" style="border-color: #667eea;"><i class="fas fa-hdd"></i> Armazenamento 512 GB SSD (Ultra Rápido)</div>
            <div class="spec-item" style="border-color: #764ba2;"><i class="fas fa-memory"></i> Memória RAM 8 GB</div>
            <div class="spec-item" style="border-color: #6a11cb;"><i class="fas fa-desktop"></i> Tela 15.6" Full HD (1920x1080)</div>
            <div class="spec-item" style="border-color: #ff0844;"><i class="fas fa-volume-up"></i> Som Waves MaxxAudio Pro</div>
            <div class="spec-item" style="border-color: #f093fb;"><i class="fas fa-wifi"></i> Wi-Fi & Bluetooth Integrados</div>
        </div>

        <a href="{LINK_AFILIADO}" class="btn-comprar">IR PARA O MERCADO LIVRE <i class="fas fa-arrow-right"></i></a>
        <p style="font-size: 10px; color: #999; margin-top: 15px;">*Oferta por tempo limitado no Mercado Livre Full</p>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(site_html)

print("Landing Page Gerada com Sucesso!")

