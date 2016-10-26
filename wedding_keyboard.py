import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

main_url = "http://dimaplusnadia.wixsite.com/dimanadialovestory/fullscreen-page/comp-iui1lr44/f9697f2b-3439-4542-b4b7" \
           "-748bfbab1a1f/0/%3Fi%3D0%26p%3Dc1dmp%26s%3Dstyle-iui32ah4"
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome(chrome_options=chromeOptions)

while True:
    driver.get(main_url)
    time.sleep(2)

    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)

    expand_button = driver.find_element_by_class_name('fullscreen-expand')
    close_button = driver.find_element_by_class_name('fullscreen-close')

    expand_button.click()

    time.sleep(2)

    image_quantity = 180

    while image_quantity > 0:
        next_image_action = ActionChains(driver).send_keys('\ue014')
        next_image_action.perform()
        time.sleep(3)

        image_quantity -= 1

    close_button.click()