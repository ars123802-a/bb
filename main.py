from selenium import webdriver
import time
import schedule
options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")
options.add_argument(r'--user-data-dir=/Users/arsgib/Library/Application Support/Google/Chrome/')
driver = webdriver.Chrome(options=options, executable_path='/Users/arsgib/Downloads/chromedriver')
driver.get("https://www.nike.com/ru/launch")
time.sleep(2)
cookies = driver.get_cookies()
driver.get("https://gs.nike.com/?checkoutId=0532c18b-c05d-4339-a34f-2dd673f92cdc&launchId=e0feb537-6866-4487-9d43-482fb4104f71&skuId=c9e5ca37-574d-5e33-af64-6d14316d9df0&country=RU&locale=ru&appId=com.nike.commerce.snkrs.web&returnUrl=https:%2F%2Fwww.nike.com%2Fru%2Flaunch%2Ft%2Ffree-run-trail-green-glow%2F")
time.sleep(5)
elem = driver.find_element_by_xpath('/html/body/esw-root/div/section/esw-checkout/div/esw-shipping-details/div/div[2]/div/esw-contact-edit/form/esw-address/esw-address-ru/div/esw-input[2]/input')
elem.send_keys('Артемович')
elem = driver.find_element_by_xpath('/html/body/esw-root/div/section/esw-checkout/div/esw-shipping-details/div/div[2]/div/esw-contact-edit/form/button')
elem.click()
elem.click()
time.sleep(5)
frame = driver.find_element_by_xpath('/html/body/esw-root/div/section/esw-checkout/div/esw-payment-details/div/div[2]/div[1]/esw-stored-cards-list/div/div/esw-new-card/div/div/esw-payment-iframe/div/iframe')
driver.switch_to.frame(frame)
elem = driver.find_element_by_id('cardNumber-input')
elem.send_keys('4276550057689112')
elem = driver.find_element_by_id('cardExpiry-input')
elem.send_keys('0124')
elem = driver.find_element_by_id('cardCvc-input')
elem.send_keys('555')
time.sleep(5)
driver.switch_to.default_content()
time.sleep(5)
elem = driver.find_element_by_xpath('/html/body/esw-root/div/section/esw-checkout/div/esw-payment-details/div/div[2]/div[3]/button')
elem.click()
elem = driver.find_element_by_xpath('/html/body/esw-root/div/section/esw-checkout/div/div[1]/button')
def click():
    elem.click()
#elem.click()
schedule.every().day.at("15:24:30").do(click)
while True:
    schedule.run_pending()
    time.sleep(1)