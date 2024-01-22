import os
import time
import main
import random
import smtplib
import variables as vb
from datetime import date
from email.message import EmailMessage


def pdf_transfer():

    pdf_lıst = []
    randm = ""
    file = os.listdir(vb.pach1)
    if len(file) == 0:
        print(vb.pdf_transfer_print2)
        return
    else:
        try:
            for i in file:
                randm = f"{date.today()}-{random.randint(1, 999)}"
                pdf_lıst.append(randm)
                os.rename(vb.pach1 + str(i), f"{vb.pach2}{randm}.pdf")
                print(vb.pdf_transfer_print1+i)
            return pdf_lıst
        except Exception as e:
            print(f"{e} {vb.error_message}")


def send_mail(aktarım):

    try:
        if aktarım is None:
            print(vb.pdf_transfer_print3)
        else:
            for i in range(len(aktarım)):
                mail_subject = "Gelen İcra Evrakı"
                mail_from = "pythonmailgonderim@gmail.com"
                mail_to = ["gokhan.kaya@astertextile.com", "ayten.guler@astertextile.com"]
                mail_mesaj = "Merhaba, Ekte bugün uets kanalı ile tarafımıza ulaşmış icra evrakı evrak mevcuttur. İyi Çalışmalar."
                appPassword = "clbj ioyn gmhy pqzp"
                with open(f"{vb.pach2}{aktarım[i]}.pdf", "rb") as f:
                    file = f.read()
                    file_name = f.name[92:]
                mail = EmailMessage()
                mail["Subject"] = mail_subject
                mail["From"] = mail_from
                mail["To"] = mail_to
                mail.set_content(mail_mesaj)
                mail.add_attachment(file, maintype="application", subtype="octet-stream", filename=file_name)
                with smtplib.SMTP_SSL("smtp.gmail.com") as sent:
                    sent.login("pythonmailgonderim@gmail.com", appPassword)
                    sent.send_message(mail)
                    sent.quit()
                print(f"{f.name[92:]} isimli dosya mail olarak gönderilmiştir...")
    except Exception as e:
        print(f"{e} {vb.error_message}")




if __name__ == "__main__":

    başlama_süresi = time.time()

    main.main_file()
    time.sleep(1)
    aktarım = pdf_transfer()
    send_mail(aktarım)

    bitiş_süresi = time.time()

    print(f"Tüm işlemler {bitiş_süresi - başlama_süresi} saniyede bitmiştir...")









