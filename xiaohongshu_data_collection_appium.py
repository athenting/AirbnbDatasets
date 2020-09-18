from appium import webdriver
import time
import random

def slide_app(keywords):

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': 'OPPO R11 Plus',
        'appPackage': 'com.xingin.xhs',
        'appActivity': 'com.xingin.alioth.search.GlobalSearchActivity t29',
        'noReset': 'True',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True'
    }

    # Appium Server
    server = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(server, desired_caps)

    search = driver.find_element_by_id('com.xingin.xhs:id/bos')
    search.click()
    time.sleep(10)
    text = driver.find_element_by_id('com.xingin.xhs:id/bos')
    time.sleep(10)
    text.send_keys(keywords)
    button = driver.find_element_by_id('com.xingin.xhs:id/bow')
    button.click()
    time.sleep(10)
    latest_post = driver.find_element_by_id('com.xingin.xhs:id/cxk')
    latest_post.click()
    time.sleep(10)

    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    slide = 0

    while slide < 500:
        print('Keywords: {}, Slide: {}/500'.format(keywords,slide))
        postname = driver.find_elements_by_id('com.xingin.xhs:id/c4t')
        driver.swipe(width * 0.5, height * 0.75, width * 0.5, height * 0.25)
        slide = slide + 1
        time.sleep(random.uniform(2, 5))
        print(postname)

    driver.save_screenshot('endpos.png')


def run():
#insert the words you want to search in Xiaohongshu app
    keywords_list = ['成都民宿']
    for keywords in keywords_list:
        print('Start Spider...')
        print('Keywords: {}'.format(keywords))
        slide_app(keywords)
        time.sleep(60)


if __name__ == '__main__':
    run()
