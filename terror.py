import os

print("☣️ Instalação do Protocolo de Terror Iniciada...")

# Seu link para voltar a faturar
LINK_LOJA = "https://ruanandre68-dot.github.io/garimpo_bot/"

html_terror = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>BIO-HAZARD: ESCAPE</title>
    <style>
        body {{ margin: 0; background: #050000; overflow: hidden; font-family: 'Courier New', Courier, monospace; }}
        
        /* Efeito de Ruído VHS */
        .noise {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: url('https://media.giphy.com/media/oEI9uWUicGuBK/giphy.gif');
            opacity: 0.05; pointer-events: none; z-index: 10;
        }}

        canvas {{ display: block; filter: contrast(120%) brightness(80%) sepia(20%); }}

        #hud {{
            position: absolute; top: 20px; left: 20px; color: #ff0000;
            font-size: 18px; text-shadow: 2px 2px #000; z-index: 11;
        }}

        #overlay {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, transparent 20%, black 70%);
            pointer-events: none; z-index: 5;
        }}

        .game-over {{
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            color: red; text-align: center; display: none; z-index: 20;
            background: rgba(0,0,0,0.9); padding: 50px; border: 1px solid red;
        }}

        button {{
            background: transparent; color: red; border: 1px solid red;
            padding: 15px 30px; cursor: pointer; font-weight: bold; margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="noise"></div>
    <div id="overlay"></div>
    <div id="hud">DNA COLETADO: <span id="score">0</span>/10</div>

    <div id="deathScreen" class="game-over">
        <h1>SISTEMA CORROMPIDO</h1>
        <p>O Espécime 0 te alcançou.</p>
        <button onclick="location.reload()">RECONECTAR</button><br>
        <button onclick="window.location.href='{LINK_LOJA}'" style="color: #fff; border-color: #fff;">FUGIR PARA A LOJA</button>
    </div>

    <canvas id="game"></canvas>

    <script>
        const canvas = document.getElementById('game');
        const ctx = canvas.getContext('2d');
        const scoreEl = document.getElementById('score');
        const deathScreen = document.getElementById('deathScreen');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let score = 0;
        let alive = true;

        // O Jogador (Sua lanterna)
        const player = {{ x: canvas.width/2, y: canvas.height/2, r: 15 }};
        
        // O Espécime 0 (O Terror)
        const monster = {{ x: 0, y: 0, size: 40, speed: 2.5 }};
        
        const dna = {{ x: Math.random()*canvas.width, y: Math.random()*canvas.height }};

        // Movimento por toque
        window.addEventListener('touchmove', (e) => {{
            player.x = e.touches[0].clientX;
            player.y = e.touches[0].clientY;
        }});

        function gameLoop() {{
            if(!alive) return;

            ctx.fillStyle = '#050000';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Perseguição do Monstro
            let dx = player.x - monster.x;
            let dy = player.y - monster.y;
            let angle = Math.atan2(dy, dx);
            monster.x += Math.cos(angle) * monster.speed;
            monster.y += Math.sin(angle) * monster.speed;

            // Desenhar DNA (Amarelo Piscante)
            ctx.fillStyle = Math.random() > 0.5 ? '#ffff00' : '#888800';
            ctx.beginPath();
            ctx.arc(dna.x, dna.y, 8, 0, Math.PI*2);
            ctx.fill();

            // Colisão DNA
            let distDna = Math.hypot(player.x - dna.x, player.y - dna.y);
            if(distDna < 25) {{
                score++;
                scoreEl.innerText = score;
                dna.x = Math.random() * canvas.width;
                dna.y = Math.random() * canvas.height;
                monster.speed += 0.3; // Fica mais difícil
            }}

            // Desenhar Monstro (Glitch Vermelho)
            ctx.fillStyle = 'red';
            if(Math.random() > 0.8) ctx.fillStyle = 'white'; // Efeito de piscar
            ctx.fillRect(monster.x + (Math.random()*10 - 5), monster.y + (Math.random()*10 - 5), monster.size, monster.size);

            // Colisão Morte
            let distMonster = Math.hypot(player.x - monster.x, player.y - monster.y);
            if(distMonster < 30) {{
                alive = false;
                deathScreen.style.display = 'block';
            }}

            // Iluminação da Lanterna
            ctx.globalCompositeOperation = 'destination-in';
            let grad = ctx.createRadialGradient(player.x, player.y, 0, player.x, player.y, 150);
            grad.addColorStop(0, 'rgba(0,0,0,1)');
            grad.addColorStop(1, 'rgba(0,0,0,0)');
            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(player.x, player.y, 150, 0, Math.PI*2);
            ctx.fill();
            ctx.globalCompositeOperation = 'source-over';

            requestAnimationFrame(gameLoop);
        }}

        gameLoop();
    </script>
</body>
</html>
"""

with open("horror.html", "w", encoding="utf-8") as f:
    f.write(html_terror)

print("☣️ Jogo de Terror Instalado com Sucesso!")

