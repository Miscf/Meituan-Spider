from appium import webdriver
import time
from program.tools.ClickByUi import ClickByUi
# from selenium.common.exceptions import NoSuchElementExceptio
from program.Store.SelectArea import SelectArea


def CheckSlec(driver, BigArea, SmallArea):
    if '销量最高' in driver.page_source:
        pass

    else:
        driver.find_element_by_id('com.sankuai.meituan:id/sort').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("销量最高")').click()
        time.sleep(0.5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("小吃快餐")').click()

        SelectArea(driver, BigArea, SmallArea)

    return driver


def drivers(Wrong):
    print(Wrong)
    desired_caps = dict()

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = 'a3e1b4a4'
    desired_caps['autoGrantPermissions'] = True
    desired_caps['newCommandTimeout'] = 120

    # 包名
    # desired_caps['appPackage'] = 'com.sankuai.meituan'
    # 界面名
    # desired_caps['appActivity'] = 'com.meituan.android.pt.homepage.activity.MainActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()

    except:
        pass


    if Wrong:
        pass

    else:
        print('notWrong')
        driver = NoWrong(driver=driver)
        print('success')

    return driver



def NoWrong(driver):

    four_times = 0
    while True:
        driver.keyevent(4)
        driver.keyevent(4)
        driver.keyevent(4)
        print(driver.current_activity)
        if driver.current_activity == '.Launcher':
            driver.find_element_by_android_uiautomator('new UiSelector().text("美团")').click()
            print('click success')
            break

        else:
            four_times += 2
            print('开始按键 -4')
            driver.keyevent(4)
            print('按键成功 -4')
            driver.keyevent(4)

            try:
                driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()

            except:
                pass

            if four_times >= 8:
                raise AttributeError

    try:
        time.sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("同意")').click()

    except:
        pass

    time.sleep(1)

    driver.wait_activity('com.meituan.android.pt.homepage.activity.MainActivity', 60)

    time.sleep(1)
    driver.find_element_by_accessibility_id('美食').click()

    driver.wait_activity('com.meituan.android.food.homepage.FoodHomePageActivity', 60)

    for opdsaujd in range(2):
        time.sleep(0.5)
        driver.swipe(548, 1650, 548, 700, 1000)

    time.sleep(1)

    ClickByUi(driver, '小吃快餐')

    time.sleep(1)

    driver.find_element_by_android_uiautomator('new UiSelector().text("智能排序")').click()

    time.sleep(0.3)

    driver.find_element_by_android_uiautomator('new UiSelector().text("销量最高")').click()

    return driver