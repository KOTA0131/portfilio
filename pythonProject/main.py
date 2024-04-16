from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email import message


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36 Edg/123.0.0.0",
    "Accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
}

response = requests.get("https://www.amazon.co.jp/GORILLA-SQUAD-%E3%82%B4%E3%83%AA%E3%83%A9%E3%82%B9%E3%82%AF%E3%83"
                        "%AF%E3%83%83%E3%83%89-%E3%82%B4%E3%83%AA%E3%83%A9%E3%82%B0%E3%83%AA%E3%83%83%E3%83%97%E3%82"
                        "%B9Ver-2-5-%E9%AB%98%E5%BC%B7%E5%BA%A6%E6%BB%91%E3%82%8A%E6%AD%A2%E3%82%81%E3%83%A9%E3%83%90"
                        "%E3%83%BC/dp/B0BZ9KWXW6/ref=sr_1_4_sspa?crid=2C9C1D49M8H07&dib=eyJ2IjoiMSJ9"
                        ".WW9eYNtGWW8Fc1_A2m0TOIovBdE6zzdtm2NOeAu4DemHPiRBQrtZZo2Y2IJSJEuW4wNGQP"
                        "-Bfi_pBCo4tHKxNtEyglnkOGW5BEnu9g2ea4zywAOJLmAwkkOih1_ZqrqxDY8K5I_EE7LA"
                        "-cymeaGKveLvrbB5eE3hFS_nQRHVM0VoS4nYibMaKfPguHtDqfoVO5aPyptIqNVTi"
                        "-OVGratOs7C0VvnRv_FaTMYkzUNsDcs"
                        "-KOXr3y22NRZp1eF9vyCZncM5g46uc_Y1zyanVLIXhKXvhMiMtVk1b6BEhkuhSA.5xEVN"
                        "-1EOuOGAo0jzKZ4KcvQNeF9WqhKY7M2oSzGJm4&dib_tag=se&keywords=%E3%83%91%E3%83%AF%E3%83%BC%E3%82"
                        "%B0%E3%83%AA%E3%83%83%E3%83%97&qid=1713210208&sprefix=%2Caps%2C154&sr=8-4-spons&sp_csd"
                        "=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1", headers=header)
soup = BeautifulSoup(response.text, "lxml")

grip_value = soup.find("span", class_="aok-offscreen").get_text()
grip_value = grip_value.replace("￥", "")
value = int(grip_value.replace(",", ""))

grip_title = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break").get_text()

""" メール設定 """
from_email = "@outlook.jp"  # 送信元アドレス
to_email = "@outlook.jp"
smtp_host = "outlook.office365.com"

with smtplib.SMTP("outlook.office365.com", port=587) as connection:
    connection.starttls()
    result = connection.login(from_email, "K71310131k@")
    msg = message.EmailMessage()
    msg.set_content(f"{grip_title}は{value}に値下げしました。")
    msg['Subject'] = 'Test email'
    msg['From'] = from_email
    msg['To'] = to_email

    # サーバーとのやりとり
    server = smtplib.SMTP(smtp_host, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(myname, password)
    server.send_message(msg)
    server.quit()
