import time
import json
import xlrd
from program.settings import CheckSlec
from xlutils.copy import copy
from json.decoder import JSONDecodeError
from program.main import main_program
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException


def SA(driver, BigArea, SmallArea):
    while True:
        try:
            main_program(driver, 2, BigArea, SmallArea, 0, 0, 0, 0, False)
            with open('F:/python files/Meituan/TimeSave/process.txt', 'r', encoding='utf-8') as f:
                if str(json.loads(f.read())) == str(BigArea + ' ' + SmallArea + 'C'):
                    return driver

                else:
                    pass

        except:
            print('Select failed')
            driver = login(False)


def login(wrong):
    while True:
        try:
            print('logining...')
            driver = main_program(driver=0, step=0, BigArea=0, SmallArea=0, workbook=0, r=0, cont=0, workbooktwo=0,
                                  wrong=wrong)

            return driver

        except Exception:
            pass


def program(BigArea, SmallArea, workbook, worksheet, workbooktwo, worksheettwo, conti, r):
    print('Everything has began, sir')

    # BigAreas = ['浦东新区', '徐汇区', '长宁区', '黄浦区', '静安区', '闵行区', '杨浦区', '普陀区', '虹口区', '宝山区', '松江区', '嘉定区', '金山区', '青浦区',
    #             '奉贤区', '崇明区']


    worksheet.write(0, 0, '店铺名称')
    worksheet.write(0, 1, '食品类型')
    worksheet.write(0, 2, '店铺评分')
    worksheet.write(0, 3, '季度销量')
    worksheet.write(0, 4, '人均消费')
    worksheet.write(0, 5, '店铺外卖')
    worksheet.write(0, 6, '连锁店铺')
    worksheet.write(0, 7, '营业时间')
    worksheet.write(0, 8, '低分率')
    worksheet.write(0, 9, '晒图率')
    worksheet.write(0, 10, '区')
    worksheet.write(0, 11, '商圈')
    worksheet.write(0, 12, '低评论总数')
    worksheet.write(0, 13, '晒图总数')
    worksheet.write(0, 14, '评论总数')

    print('write success')

    driver = login(False)
    print('Login success')

    #
    # while True:
    #     try:
    #         with open('F:/python files/Meituan/TimeSave/process.txt', 'r', encoding='utf-8') as f:
    #             if str(f.read()) == '0Step':
    #                 print('Get AreasList succss')
    #                 break
    #
    #             else:
    #                 print('Match Failed')
    #                 main_program(driver, 1, 0, 0, 0, 0, 0, 0, False)
    #
    #     except:
    #         print('Something wrong')
    #         driver = login(False)
    #
    # with open('F:/python files/Meituan/TimeSave/DownloadAreas.txt', 'r', encoding='utf-8') as op:
    #     AreasList = json.loads(op.read())

    print('current area:', BigArea, SmallArea)

    while True:
        try:
            with open('F:/python files/Meituan/TimeSave/process.txt', 'r', encoding='utf-8') as f:
                if str(json.loads(f.read())) == str(BigArea + ' ' + SmallArea + 'C'):
                    break

                else:
                    print('changing the area...')
                    main_program(driver, 2, BigArea, SmallArea, 0, 0, conti, 0, False)
                    print('changing the area success')

        except JSONDecodeError:
            print('JSONDecodeError')
            # SelectArea
            main_program(driver, 2, BigArea, SmallArea, 0, 0, conti, 0, False)


        except NoSuchElementException:
            print('Something goes wrong')
            driver = login(False)

    while True:
        # 查看状态
        with open('F:/python files/Meituan/TimeSave/process.txt', 'r', encoding='utf-8') as f:
            print('open success')
            state = f.read()

            if str(json.loads(state)) == str(BigArea + ' ' + SmallArea + 'C'):
                try:
                    print('bregin carry out DownloadStore')
                    # bef = r.get('count')
                    driver = CheckSlec(driver, BigArea, SmallArea)

                    if '全城' in driver.page_source:
                        SA(driver, BigArea, SmallArea)

                    else:
                        pass

                    main_program(driver, 3, BigArea, SmallArea, worksheet, r, conti, worksheettwo, False)
                    print('DownloadStore success')
                    workbooktwo.save(r'F:\\python files\\Meituan\\program\\Store\\comment\\pl.xls')

                except JSONDecodeError as J:
                    print(J)
                    print('JSONDecodeError twice J')
                    # bef = r.get('count')
                    main_program(driver, 3, BigArea, SmallArea, worksheet, r, conti, worksheettwo, False)
                    print('DownloadStore Success in JSON')
                    workbooktwo.save(r'F:\\python files\\Meituan\\program\\Store\\comment\\pl.xls')

                    workbooktwo = xlrd.open_workbook(r'F:\\python files\\Meituan\\program\\Store\\comment\\pl.xls')
                    workbooktwo = copy(workbooktwo)

                    worksheettwo = workbooktwo.get_sheet(0)

                except WebDriverException as w:
                    print(w)

                    if str(w).replace('\n', '') == 'Message: An unknown server-side error occurred while processing the command. Original error: Timed out after 10000 milliseconds waiting for root AccessibilityNodeInfo':
                        for poiq in range(11):
                            driver.keyevent(4)

                        login(False)

                    else:
                        pass

                    print('Something wrong twice W')
                    driver = login(True)

                    if driver.current_activity == 'com.meituan.android.pt.homepage.activity.MainActivity':
                        driver.swipe(514, 600, 514, 1600, 900)
                        driver.find_element_by_accessibility_id('美食').click()

                        for opdsaujd in range(2):
                            time.sleep(0.5)
                            driver.swipe(548, 1650, 548, 700, 1000)

                        main_program(driver, 2, BigArea, SmallArea, 0, 0, conti, 0, False)

                        driver.find_element_by_android_uiautomator('new UiSelector().text("小吃快餐")').click()

                    elif driver.current_activity == 'com.meituan.android.food.homepage.FoodHomePageActivity':
                        pass

                    elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
                        driver.keyevent(4)
                        time.sleep(0.5)

                    elif driver.current_activity == 'com.meituan.android.ugc.review.list.ui.ReviewListActivity':
                        driver.keyevent(4)
                        time.sleep(1)
                        driver.keyevent(4)

                    else:
                        driver = login(False)
                        main_program(driver, 2, BigArea, SmallArea, 0, 0, conti, 0, False)

                    print('W login success')
                    time.sleep(1)

                    # driver = SA(driver, BigArea, SmallArea)

                    while True:
                        if driver.current_activity == 'com.meituan.android.food.homepage.FoodHomePageActivity':
                            break

                        elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
                            driver.keyevent(4)
                            time.sleep(1)

                        elif driver.current_activity == 'com.meituan.android.ugc.review.list.ui.ReviewListActivity':
                            driver.keyevent(4)
                            time.sleep(1)
                            driver.keyevent(4)
                            time.sleep(1)

                        else:
                            print('NO!!!!!!!!!!!!')
                            break

                    if str(r.get('current')) == 'None':
                        pass

                    else:
                        conti = True


                except NoSuchElementException as N:
                    print(N)
                    print('Something wrong twice N')
                    driver = login(True)
                    # driver = SA(driver, BigArea, SmallArea)
                    if str(r.get('current')) == 'None':
                        pass

                    else:
                        conti = True


                except AttributeError as A:
                    print('-----Something wrong twice A-----')
                    print(A)
                    driver = login(True)
                    driver = SA(driver, BigArea, SmallArea)
                    if str(r.get('current')) == 'None':
                        pass

                    else:
                        conti = True

                except Exception as EX:
                    print('\n', EX, '\n')
                    print("It has been kept and restart!")
                    driver = login(True)
                    driver = SA(driver, BigArea, SmallArea)
                    if str(r.get('current')) == 'None':
                        pass

                    else:
                        conti = True

                    workbook.save(r'F:\\python files\\Meituan\\results\\Meituan.xls')

                    workbook = xlrd.open_workbook(r'F:\\python files\\Meituan\\results\\Meituan.xls')

                    workbook = copy(workbook)

                    worksheet = workbook.get_sheet(0)


            elif str(json.loads(state)) == str(str(BigArea) + ' ' + str(SmallArea) + 'S'):
                print('Not matching S')
                break

            else:
                print('Not matching C')
                pass

    workbook.save(r'F:\\python files\\Meituan\\results\\Meituan.xls')
    print('All have done, sir')