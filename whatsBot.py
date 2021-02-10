from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\chromedriver')  # You need to install 'chromedriver'
sleep(5)

#      When the bot starts, you need put the QR Code using your cellphone to login.

def enviarMensagem():
    mensagem = ' *Mensagem automática*:  Oii'                 # Predefined message
    driver.get('https://web.whatsapp.com/')
    sleep(5)                                                  # Wait 5 seconds
    nome = driver.find_element_by_xpath("//span[@title='']")  # insert the person / group name inside the single quotes
    sleep(5)                                                  # Wait 5 seconds
    nome.click()
    texto_input = driver.find_element_by_class_name('DuUXI')   # Search the search field
    sleep(5)
    texto_input.send_keys(mensagem)   # Write the message
    sleep(2)
    emote = driver.find_element_by_xpath("//span[@data-icon='smiley']")   # Click the emote button
    emote.click()
    sleep(1)
    emote2 = driver.find_element_by_class_name('b76.emojik.wa')           #Choose the emote
    emote2.click()
    sleep(1)
    enter = driver.find_element_by_xpath("//span[@data-icon='send']")     #Click on the send button
    enter.click()

enviarMensagem()







