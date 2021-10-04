import requests
from bs4 import BeautifulSoup
import smtplib
import time


def send_mail(price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('harsit.sinha@gmail.com','moetebmzugwqvcbf')

    subject ='Harsit, Price fell down'
    body =f'PRICE : {price}\nCheck the amazon link  https://www.amazon.in/All-new-Echo-Dot-with-clock/dp/B084J4MZQM/ref=sr_1_12?crid=QK4OPVG824QP&dchild=1&keywords=echo+dot&qid=1633159884&qsid=261-7841490-3008962&smid=AT95IG9ONZD7S&sprefix=eecho+%2Caps%2C351&sr=8-12&sres=B07PFFMP9P%2CB084KSRFXJ%2CB084DWH53T%2CB085M5R82K%2CB07PGL2ZSL%2CB07PHPY4WG%2CB07PDHTHNN%2CB096S4ZWPR%2CB07XJQ89ZJ%2CB08HMZ4J7Q%2CB084J4MZQM%2CB08PLQW87C%2CB084L41R96%2CB098QJ86PT%2CB08K94M7H1%2CB08K46MXFH'
    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'harsit.sinha@gmail.com',
        'harsits20@iitk.ac.in',
        msg
    )
    print("email sent")
    server.quit()


def check_price():
    URL ='https://www.amazon.in/All-new-Echo-Dot-with-clock/dp/B084J4MZQM/ref=sr_1_12?crid=QK4OPVG824QP&dchild=1&keywords=echo+dot&qid=1633159884&qsid=261-7841490-3008962&smid=AT95IG9ONZD7S&sprefix=eecho+%2Caps%2C351&sr=8-12&sres=B07PFFMP9P%2CB084KSRFXJ%2CB084DWH53T%2CB085M5R82K%2CB07PGL2ZSL%2CB07PHPY4WG%2CB07PDHTHNN%2CB096S4ZWPR%2CB07XJQ89ZJ%2CB08HMZ4J7Q%2CB084J4MZQM%2CB08PLQW87C%2CB084L41R96%2CB098QJ86PT%2CB08K94M7H1%2CB08K46MXFH'
    headers ={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price = soup.find(id='priceblock_dealprice').get_text()
    price = float(price.replace(",", "")[1:])
    # if price < 4149:
    #     print(price)
    send_mail(price)


while True:
    check_price()
    time.sleep(60*60*12)

