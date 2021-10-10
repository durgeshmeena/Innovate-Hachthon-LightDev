from selenium import webdriver
import time

def get_user(username, password):
        
    driver  = webdriver.Chrome('D:\\WebDrivers\\chromedriver.exe')
    driver.get("https://www.d2h.com/user-login?returnUrl=%2Fmyaccount%2Findex")

    time.sleep(5)
    
    custfor_radio_btn = driver.find_element_by_id('custfor')
    custfor_radio_btn.click()

    time.sleep(2)

    customer_id = driver.find_element_by_id('userinput')
    customer_id.send_keys(username)
    # time.sleep(2)
    password_field = driver.find_element_by_class_name('pwd')
    password_field.send_keys(password)
    # time.sleep(2)

    login_buttons = driver.find_element_by_class_name('btn-primary')
    login_buttons.click()

    time.sleep(5)

    general_details = {}

    name = driver.find_element_by_class_name("name").text
    status = driver.find_element_by_class_name("status").text
    VC_no = driver.find_element_by_tag_name('option').get_attribute("value")
    model = driver.find_element_by_tag_name('option').get_attribute("modeltype")
    # status = driver.find_element_by_tag_name('option').get_attribute("status")

    general_details["Name"] = name
    general_details["Account Status"] = status
    general_details["VC_NO."] = VC_no
    general_details["Model"] = model

    balance = {}

    balance_data = [hdval.text for hdval in  driver.find_elements_by_class_name('headtext')]
    balance_value = [ balval.text for balval in  driver.find_elements_by_tag_name('span')]

    balance['Balance_Today'] = balance_value[13]
    balance['Last Recharge Amount'] = balance_value[14]
    balance['Last Recharge Date'] = balance_value[15]
    balance['Next Recharge Date'] = balance_value[16]
    balance['Full Month Recharge'] = driver.find_element_by_tag_name("b").text

    offer = driver.find_element_by_xpath("//div[@class='contaslider']/img").get_attribute("src")


    user_data = {}
    all_data = driver.find_elements_by_class_name('font-deatil')
    all_list = []
    for data in all_data:
        all_list.append(data.text)

    j=0
    while j<8:
        user_data[all_list[j]] = all_list[j+1]
        j = j+2

    ALL = {}
    ALL[1] = general_details
    ALL[2] = balance
    ALL[3] = user_data

    driver.close()
    # print(ALL)
    return ALL

    

    # print("\n", '\n', '-------------------------------------------', '\n', '\n')

    # print(name)
    # print(status)
    # print(VC_no)
    # print(model)
    # print(balance)
    # print(user_data)
    # print(offer)

    # print("\n", '\n', '-------------------------------------------', '\n', '\n')
    