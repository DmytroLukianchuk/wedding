import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# set the time delay between slides
while True:
    try:
        TIME_BETWEEN_SLIDES = int(input("Enter the distance between photos in sec: "))
    except ValueError:
        print("You entered not a number. Please enter correct value")
        continue
    else:
        break
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
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    # allocate expand and close buttons
    expand_button = driver.find_element_by_class_name('fullscreen-expand')
    close_button = driver.find_element_by_class_name('fullscreen-close')
    # click expand and wait
    expand_button.click()

    time.sleep(TIME_BETWEEN_SLIDES)
    # set the general quantity of the gallery
    image_quantity = 180
    # changing photos by clicking right arrow on the keyboard till the end of the gallery
    while image_quantity > 0:
        next_image_action = ActionChains(driver).send_keys('\ue014')
        next_image_action.perform()
        # delay between slides is TIME_BETWEEN_SLIDES value sec
        time.sleep(TIME_BETWEEN_SLIDES)

        image_quantity -= 1
    # close the expand mode when end of gallery
    close_button.click()
