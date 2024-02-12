

#################### main.py ##############################

user_tc_no = ""
user_pass = ""

error_message = "Hatası Oluştu..."

notifications_down_print1 = "İcra Dosyası İndirilmiştir..."
notifications_down_print2 = "İndirilecek İcra Dosyası Bulunamamıştır..."
main_file_print1 = "İşlem Sonuçlandı..."



url = "https://ptt.etebligat.gov.tr/login"
e_devlet_button = "//a[contains(text(), ' e-Devlet' )]"
tc_no = "mat-input-0"
e_devlet_pass = "mat-input-1"
enter_button = "button[class='btn btn-accent m-btn m-btn--custom m-btn--icon m-btn--air']"
guvenlik_giris = "//*[@id='m_login']/div[2]/div[2]/m-sms-code/div/form/div/div[2]/input"
guvenlik_button = "button[class='btn btn-brand']"
compant_button = "button[class='btn btn-accent btn-sm m-btn--custom m-btn--icon m-btn--air']"
notifications = "//span[contains(text(), 'Tebligatlarım')]"
link_button = "button[class='btn btn-grey btn-sm text-uppercase dropdown-toggle edit-toggle']"
viewing_button = "a[class='view-btn btn btn-sm m-btn--icon mr-2 ng-star-inserted']"
pdf_link = "span[class='link']"
del_button = "button[class='delete-btn btn btn-sm m-btn--icon ng-star-inserted']"
dell_button = "button[class='btn btn-danger m-btn--icon ng-star-inserted']"


#################### file_mail ##############################

pach1 = "C:/Users/gokhan.kaya/Downloads/"
pach2 = "C:/Users/gokhan.kaya/OneDrive - Aster Textile/Desktop/BELGELERİM/GELEN İCRA/yeniİcraKlasörü/"

pdf_transfer_print1 = "İcra Evrakı klasöre taşınmıştır..."
pdf_transfer_print2 = "İndirilenler klasöründe icra evrakı mecvut değildir..."
pdf_transfer_print3 = "Dosya'da gönderilecek evrak bulunamamıştır..."
