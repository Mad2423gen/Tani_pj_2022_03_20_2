import smtplib, ssl
from email.mime.text import MIMEText

# Gmail設定
my_account = 'tartnesssectional6@gmail.com'
my_password = 'bnF8D2JxEjrUZh'

def send_gmail(msg):
    """
    引数msgをGmailで送信
    """
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())
    # ログ出力
    server.set_debuglevel(0)
    # ログインしてメール送信
    server.login(my_account, my_password)
    server.send_message(msg)

def make_mime(mail_to, subject, body):
    """
    引数をMIME形式に変換
    """
    msg = MIMEText(body, 'plain') #メッセージ本文
    msg['Subject'] = subject #件名
    msg['To'] = mail_to #宛先
    msg['From'] = my_account #送信元
    return msg

def send_my_message(msg):
    """
    メイン処理
    """
    # MIME形式に変換
    msg = make_mime(
        mail_to='soramimiplatz@gmail.com', #送信したい宛先を指定
        subject='2022/01/17テスト送信',
        body= msg)
    # gmailに送信
    send_gmail(msg)

if __name__ == '__main__':
    send_my_message()
