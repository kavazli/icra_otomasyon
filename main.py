import time
import variables as vb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def browser_enter():

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=chrome_options) # options=chrome_options
        browser.get(vb.url)
        browser.maximize_window()
        # WebDriverWait(browser, 6).until(EC.visibility_of_element_located((By.XPATH, vb.e_devlet_button)))
        # browser.find_element(By.XPATH, vb.e_devlet_button).click()
        return browser
    except Exception as e:
        print(f"{e}", vb.error_message)

def sistem_enter(link):

    try:
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.ID, vb.tc_no)))
        link.find_element(By.ID, vb.tc_no).send_keys(vb.user_tc_no)
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.ID, vb.e_devlet_pass)))
        link.find_element(By.ID, vb.e_devlet_pass).send_keys(vb.user_pass)
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, vb.enter_button)))
        link.find_element(By.CSS_SELECTOR, vb.enter_button).click()
        kod = input("Lütfen Güvenlik Kodunu Giriniz...: ")
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.XPATH, vb.guvenlik_giris)))
        link.find_element(By.XPATH, vb.guvenlik_giris).send_keys(kod)
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, vb.guvenlik_button)))
        link.find_element(By.CSS_SELECTOR, vb.guvenlik_button).click()



        return link
    except Exception as a:
        print(f"{a}", vb.error_message)


def company_enter(link, sayı):
    try:
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, vb.compant_button)))
        link.find_elements(By.CSS_SELECTOR, vb.compant_button)[int(sayı)].click()
        WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.XPATH, vb.notifications)))
        link.find_element(By.XPATH, vb.notifications).click()
        time.sleep(2)
        return link
    except Exception as d:
        print(f"{d}", vb.error_message)


def notifications_down(link):
    WebDriverWait(link, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, vb.link_button)))
    buton = link.find_element(By.CSS_SELECTOR, vb.link_button)

    if buton.is_enabled():

        try:
            WebDriverWait(link, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, vb.viewing_button)))
            link.find_element(By.CSS_SELECTOR, vb.viewing_button).click()
            WebDriverWait(link, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, vb.pdf_link)))
            link.find_element(By.CSS_SELECTOR, vb.pdf_link).click()
            time.sleep(2)
            link.back()
            link.refresh()
            WebDriverWait(link, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, vb.del_button)))
            link.find_element(By.CSS_SELECTOR, vb.del_button).click()
            WebDriverWait(link, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, vb.dell_button)))
            link.find_element(By.CSS_SELECTOR, vb.dell_button).click()
            print(vb.notifications_down_print1)
            time.sleep(1)
            link.quit()
        except Exception as k:
            print(f"{k}", vb.error_message)

    else:
        time.sleep(1)
        print(vb.notifications_down_print2)
        link.quit()

def main_file():


    try:
        link = browser_enter()
        sistem_enter(link)
        firma_kodu = input("Lütfen Firma kodunu giriniz...:")
        company_enter(link, firma_kodu)
        notifications_down(link)
        print(f"{vb.main_file_print1}{firma_kodu}")
    except Exception as l:
        print(f"{l}", vb.error_message)






if __name__ == "__main__":

    main_file()



