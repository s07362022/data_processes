#Gmail#################################
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
def smtp(img_name,label):
    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "detector to  Stand or fall"  #郵件標題
    content["from"] = "gish1040403@gmail.com"  #寄件者
    content["to"] = "qaz3661537@gmail.com" #收件者
    timenow = datetime.datetime.now()
    timenow = str(timenow)
    content.attach(MIMEText(timenow + " " +label))  #郵件內容
    phto = Path(img_name).read_bytes()
    content.attach(MIMEImage(phto))
    #文字
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("gish1040403@gmail.com", "cffakphyrorydcti")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
######################################
