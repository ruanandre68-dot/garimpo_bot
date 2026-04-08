html_ultra = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>ULTRA BIO-HAZARD 3D</title>
    <style>
        body { margin: 0; background: #000; overflow: hidden; font-family: 'Arial'; }
        canvas { width: 100vw; height: 100vh; image-rendering: pixelated; filter: contrast(1.2) saturate(1.2); }
        #hud { position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 300px; pointer-events: none; }
        .crosshair { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: rgba(255,0,0,0.5); font-size: 24px; }
        .controls { position: absolute; bottom: 20px; left: 20px; display: grid; grid-template-columns: repeat(3, 70px); gap: 10px; opacity: 0.6; }
        .btn { width: 70px; height: 70px; background: rgba(255,255,255,0.1); border: 2px solid #fff; color: #fff; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: bold; font-size: 20px; }
    </style>
</head>
<body>
    <div class="crosshair">+</div>
    <div id="hud">
        <div id="weapon" style="width: 100%; height: 150px; background: linear-gradient(to top, #111, transparent); border-radius: 50% 50% 0 0; border: 4px solid #222;"></div>
    </div>

    <div class="controls">
        <div></div><div class="btn" id="up">↑</div><div></div>
        <div class="btn" id="left">←</div><div class="btn" id="down">↓</div><div class="btn" id="right">→</div>
    </div>

    <canvas id="c"></canvas>

    <script>
        const canvas = document.getElementById('c');
        const ctx = canvas.getContext('2d');
        const W = 400, H = 250; // Resolução interna alta
        canvas.width = W; canvas.height = H;

        let player = { x: 3.5, y: 3.5, dir: 0, v: 0, av: 0, b: 0 };
        const map = [
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,2,0,2,0,0,3,0,1],
            [1,0,0,0,0,0,0,3,0,1],
            [1,0,2,0,2,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1]
        ];

        // Gerador de Textura Procedural (Engenharia de Elite)
        const tex = ctx.createRadialGradient(32,32,5,32,32,32);
        tex.addColorStop(0, '#555'); tex.addColorStop(1, '#222');

        function render() {
            // Chão e Teto com Degradê (Imersão)
            let sky = ctx.createLinearGradient(0,0,0,H);
            sky.addColorStop(0, '#050505'); sky.addColorStop(0.5, '#111'); sky.addColorStop(1, '#050515');
            ctx.fillStyle = sky; ctx.fillRect(0,0,W,H);

            for(let x=0; x<W; x++) {
                let camX = 2 * x / W - 1;
                let rDirX = Math.cos(player.dir) + Math.cos(player.dir + 1.57) * camX * 0.8;
                let rDirY = Math.sin(player.dir) + Math.sin(player.dir + 1.57) * camX * 0.8;

                let mX = Math.floor(player.x), mY = Math.floor(player.y);
                let dX = Math.abs(1/rDirX), dY = Math.abs(1/rDirY);
                let sX, sY, sdX, sdY, hit=0, side;

                if(rDirX<0) {{ sX=-1; sdX=(player.x-mX)*dX; }} else {{ sX=1; sdX=(mX+1-player.x)*dX; }}
                if(rDirY<0) {{ sY=-1; sdY=(player.y-mY)*dY; }} else {{ sY=1; sdY=(mY+1-player.y)*dY; }}

                while(!hit) {
                    if(sdX<sdY) {{ sdX+=dX; mX+=sX; side=0; }} else {{ sdY+=dY; mY+=sY; side=1; }}
                    if(map[mY][mX]>0) hit=map[mY][mX];
                }

                let dist = side==0 ? sdX-dX : sdY-dY;
                let h = H/dist;

                // Desenho da Parede com Textura de "Ranhuras"
                let brightness = Math.min(255, 200/dist);
                let r = hit==2 ? brightness : 0;
                let g = hit==3 ? brightness : brightness/2;
                let b = brightness/1.5;

                ctx.strokeStyle = `rgb(${r},${g},${b})`;
                // Efeito de Scanline/Textura
                if(x % 2 == 0) ctx.strokeStyle = `rgb(${r*0.8},${g*0.8},${b*0.8})`;

                ctx.beginPath();
                ctx.moveTo(x, H/2 - h/2 + player.b);
                ctx.lineTo(x, H/2 + h/2 + player.b);
                ctx.stroke();
            }

            // Movimento e Bobbing (Balanço da Câmera)
            if(player.v != 0) player.b = Math.sin(Date.now()/100) * 5;
            else player.b *= 0.9;

            player.dir += player.av;
            let nx = player.x + Math.cos(player.dir) * player.v;
            let ny = player.y + Math.sin(player.dir) * player.v;
            if(map[Math.floor(player.y)][Math.floor(nx)] == 0) player.x = nx;
            if(map[Math.floor(ny)][Math.floor(player.x)] == 0) player.y = ny;

            requestAnimationFrame(render);
        }

        const btn = (id, v, av) => {
            const e = document.getElementById(id);
            e.ontouchstart = () => { player.v = v; player.av = av; };
            e.ontouchend = () => { player.v = 0; player.av = 0; };
        };
        btn('up', 0.06, 0); btn('down', -0.06, 0); btn('left', 0, -0.04); btn('right', 0, 0.04);

        render();
    </script>
</body>
</html>
"""
with open("ultra_game.html", "w") as f: f.write(html_ultra)
print("Engenharia ULTRA HD Finalizada!")

