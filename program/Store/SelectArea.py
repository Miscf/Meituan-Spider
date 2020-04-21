from selenium.common.exceptions import NoSuchElementException
import json

def SelectArea(driver, BigArea, SmallArea):
    driver.find_element_by_id('com.sankuai.meituan:id/area').click()

    while True:
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(BigArea)).click()

            while True:
                try:
                    driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(SmallArea)).click()

                    with open('F:\\python files\\Meituan\\TimeSave\\process.txt', 'w', encoding='utf-8') as f:
                        f.write(json.dumps(str(BigArea + ' ' + SmallArea + 'C')))

                    break

                except NoSuchElementException:
                    driver.swipe(663, 1500, 663, 1000, 1000)
            break

        except NoSuchElementException:
            driver.swipe(187, 1500, 187, 1000, 1000)