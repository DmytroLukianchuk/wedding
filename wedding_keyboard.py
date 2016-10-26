import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# navigation to the first image of the gallery
main_url = "http://dimaplusnadia.wixsite.com/dimanadialovestory/fullscreen-page/comp-iui1lr44/f9697f2b-3439-4542-b4b7" \
           "-748bfbab1a1f/0/%3Fi%3D0%26p%3Dc1dmp%26s%3Dstyle-iui32ah4"

# run Chrome in a fullscreen mode (click on the screen before to run Chrome there)
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome(chrome_options=chromeOptions)

# forever loop, non stop gallery slideshow
while True:
    # open the main url
    driver.get(main_url)
    # wait for iframe to be loaded
    time.sleep(2)
    # switch to the iframe
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)
    # allocate expand and close buttons
    expand_button = driver.find_element_by_class_name('fullscreen-expand')
    close_button = driver.find_element_by_class_name('fullscreen-close')
    # click expand and wait for three seconds
    expand_button.click()

    time.sleep(3)
    # set the general quantity of the gallery
    image_quantity = 180
    # changing photos by clicking right arrow on the keyboard till the end of the gallery
    while image_quantity > 0:
        next_image_action = ActionChains(driver).send_keys('\ue014')
        next_image_action.perform()
        # delay between slides is 3 sec
        time.sleep(3)

        image_quantity -= 1
    # close the expand mode when end of gallery
    close_button.click()
