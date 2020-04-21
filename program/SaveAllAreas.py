import json
from selenium.common.exceptions import NoSuchElementException

def DownloadAreaNames(driver):
    driver.find_element_by_id('com.sankuai.meituan:id/area').click()

    LastKeyList = ['迪士尼/浦东机场', '光启城', '北新泾/淞虹路', '西藏南路/世博会馆', '上海长途汽车站', '新乐坊', '东外滩', '月星环球港', '大柏树', '高境', '开元地中海',
                   '华亭镇', '廊下', '虹桥枢纽周边区', '正阳世纪星城', '东湖游览区']
    BigAreas = ['浦东新区', '徐汇区', '长宁区', '黄浦区', '静安区', '闵行区', '杨浦区', '普陀区', '虹口区', '宝山区', '松江区', '嘉定区', '金山区', '青浦区',
                '奉贤区', '崇明区']
    SmallAreas = list()

    for BigArea in BigAreas:
        SmallAreasList = []
        YH = False
        Over = False

        while True:
            try:
                if Over:
                    break

                else:
                    pass

                if YH:
                    pass

                else:
                    print("It's finding {} now!".format(BigArea))
                    driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(BigArea)).click()
                    print('Find Success')

                YH = True
                elementList = driver.find_elements_by_xpath("//android.widget.ListView[2]/android.widget.LinearLayout/android.widget.TextView")

                for element in elementList:
                    print(element.get_attribute('text'))
                    if element.get_attribute("text") == '全部':
                        pass

                    elif element.get_attribute('text') in SmallAreasList:
                        pass

                    else:
                        print('join keyword:', element.get_attribute('text'))
                        SmallAreasList.append(element.get_attribute("text"))

                        if element.get_attribute('text') in LastKeyList:
                            SmallAreas.append([BigArea, SmallAreasList])
                            print('{} save success'.format(BigArea))
                            print(SmallAreasList)
                            Over = True

                        else:
                            pass

                driver.swipe(663, 1400, 663, 700, 1000)

            except NoSuchElementException:
                driver.swipe(187, 1400, 187, 700, 1000)

    print(SmallAreas)
    driver.find_element_by_id('com.sankuai.meituan:id/area').click()

    with open('F:/python files/Meituan/TimeSave/DownloadAreas.txt', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(SmallAreas))

    with open('F:/python files/Meituan/TimeSave/process.txt', 'w+', encoding='utf-8') as fp:
        fp.write('0Step')

    print('write success!')
