import os

print("--- ☣️ PROTOCOLO: JANELA PARA O SUBMUNDO v8 ---")
print("Sincronizando com os fóruns anônimos globais...")

html_submundo = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>SISTEMA DE MONITORAMENTO: SUBMUNDO</title>
    <style>
        body { background: #000; color: #0f0; font-family: 'Courier New', monospace; margin: 0; padding: 10px; }
        .terminal { border: 2px solid #0f0; padding: 20px; background: rgba(0,20,0,0.9); box-shadow: 0 0 20px #0f0; }
        h1 { color: #f00; text-align: center; text-transform: uppercase; border-bottom: 2px solid #f00; }
        .post { border-bottom: 1px dashed #0f0; padding: 10px; margin-bottom: 10px; animation: fadeIn 0.5s ease; }
        .post-info { color: #ff0; font-size: 11px; margin-bottom: 5px; }
        .post-content { color: #fff; font-size: 14px; word-break: break-all; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
        .warning { color: red; font-weight: bold; text-align: center; font-size: 12px; border: 1px solid red; padding: 5px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="terminal">
        <h1>☣️ ANONYMOUS GLOBAL FEED</h1>
        <div class="warning">CUIDADO: CONTEÚDO NÃO FILTRADO / ALTAMENTE TÓXICO</div>
        <p style="font-size: 10px; text-align: center;">MONITORANDO BOARD: /b/ (RANDOM) e /pol/ (POLITICALLY INCORRECT)</p>
        
        <div id="feed">
            [AGUARDANDO TRANSMISSÃO...]
        </div>
    </div>

    <script>
        async function fetchPosts() {
            const boards = ['b', 'pol'];
            const board = boards[Math.floor(Math.random() * boards.length)];
            const feed = document.getElementById('feed');
            
            try {
                const response = await fetch(`https://a.4cdn.org/${board}/0.json`);
                const data = await response.json();
                const threads = data.threads;
                const post = threads[Math.floor(Math.random() * threads.length)].posts[0];
                
                if (post.com) {
                    const cleanText = post.com.replace(/<[^>]*>/g, '').substring(0, 200);
                    const postDiv = document.createElement('div');
                    postDiv.className = 'post';
                    postDiv.innerHTML = `
                        <div class="post-info">>> BOARD: /${board}/ | ID: ${post.no} | DATA: ${post.now}</div>
                        <div class="post-content">${cleanText}...</div>
                    `;
                    
                    feed.prepend(postDiv);
                    if (feed.childNodes.length > 10) feed.removeChild(feed.lastChild);
                }
            } catch (e) {
                console.log("Erro na escuta.");
            }
        }

        setInterval(fetchPosts, 3000); // Atualiza a cada 3 segundos
    </script>
</body>
</html>
"""

with open("submundo.html", "w", encoding="utf-8") as f:
    f.write(html_submundo)

print("--- ☣️ MONITOR DE SUBMUNDO PRONTO ---")

