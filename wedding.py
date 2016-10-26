import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

main_url = "http://dimaplusnadia.wixsite.com/dimanadialovestory/fullscreen-page/comp-iui1lr44/f9697f2b-3439-4542-b4b7-748bfbab1a1f/0/%3Fi%3D0%26p%3Dc1dmp%26s%3Dstyle-iui32ah4"
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome(chrome_options=chromeOptions)

while True:
    driver.get(main_url)
    time.sleep(2)

    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)

    expand_button = driver.find_element_by_class_name('fullscreen-expand')
    next_button = driver.find_element_by_class_name('fullscreen-next')
    close_button = driver.find_element_by_class_name('fullscreen-close')
    full_screen_image = driver.find_element_by_id("slider")

    expand_button.click()

    time.sleep(2)

    image_quantity = 180

    while image_quantity > 0:
        full_screen_image.click()
        next_button.click()
        time.sleep(3)

        image_quantity = image_quantity - 1

    close_button.click()
