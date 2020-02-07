import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.com/TP-Link-AC1750-Smart-WiFi-Router/dp/B079JD7F7G?pf_rd_p=538b030e-3f40-5f94-a1a5-376bc59a2030&pf_rd_r=74S4BKSFR7NC24E0S1MR&pd_rd_wg=YpzZ0&ref_=pd_gw_ri&pd_rd_w=64tWy&pd_rd_r=ce536f6d-3f70-420b-af95-2caaf05fc40e'
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
def checkprice():
     page = requests.get(URL, headers=headers)
     soup = BeautifulSoup(page.text,'lxml') 
     title = soup.select_one("h1 > #productTitle").get_text(strip=True)
     print(title)
     price = soup.find(id="priceblock_dealprice").get_text()
     print(price)
     converted_price = float(price[1:3])
     print(converted_price)
     if(converted_price>50):
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('devlopermail2020@gmail.com ','ywotnuzmrycibsjx')

    subject = 'price fell down'

    body = 'check the amazon link https://www.amazon.com/TP-Link-AC1750-Smart-WiFi-Router/dp/B079JD7F7G?pf_rd_p=538b030e-3f40-5f94-a1a5-376bc59a2030&pf_rd_r=74S4BKSFR7NC24E0S1MR&pd_rd_wg=YpzZ0&ref_=pd_gw_ri&pd_rd_w=64tWy&pd_rd_r=ce536f6d-3f70-420b-af95-2caaf05fc40e' 
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'devlopermail@gmail.com',
        'varun.rcb18@gmail.com',
        msg
    )
    print('Hey! email has been sent')

    server.quit()


checkprice()    

