from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from json.decoder import JSONDecodeError
from program.settings import CheckSlec
import time
import json
import re



def DownloadStore(driver, BigArea, SmallArea, workbook, r, conti, worksheettwo):
    Over = False
    OverTimes = 0
    current_page = str()
    save_name_list = list()

    try:
        save_name_list = json.loads(r.get('list'))

    except JSONDecodeError:
        pass

    while True:
        if driver.current_activity == 'com.meituan.android.pt.homepage.activity.MainActivity':
            driver.swipe(514, 600, 514, 1600, 900)
            driver.find_element_by_accessibility_id('美食').click()

        elif driver.current_activity == 'com.meituan.android.food.homepage.FoodHomePageActivity':
            break

        elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
            driver.keyevent(4)
            time.sleep(0.5)

        elif driver.current_activity == 'com.meituan.android.ugc.review.list.ui.ReviewListActivity':
            driver.keyevent(4)
            time.sleep(1)
            driver.keyevent(4)

        else:
            driver.keyevent(4)

    CheckSlec(driver, BigArea, SmallArea)

    print(r.get('current'))
    if 'None' in str(r.get('current')):
        pass

    else:
        if conti:
            print("It will be continue.")
            currnet_name = json.loads(r.get('current'))
            print('currnet_name:', currnet_name)
            # driver.swipe(514, 600, 514, 1600, 900)
            save_name_list = json.loads(r.get('list'))

        else:
            pass

    while True:
        noSwipe = False

        if '销量最高' in driver.page_source:
            pass

        else:
            driver.find_element_by_id('com.sankuai.meituan:id/sort').click()
            time.sleep(0.3)
            driver.find_element_by_android_uiautomator('new UiSelector().text("销量最高")').click()

        filter_tab_texts = driver.find_elements_by_xpath('//*[@resource-id="com.sankuai.meituan:id/food_filter_category_module"]/android.widget.LinearLayout/android.widget.FrameLayout')
        for filter_tab_text in filter_tab_texts:
            try:
                current_tab = filter_tab_text.find_element_by_id('com.sankuai.meituan:id/filter_tab_text').get_attribute('text')
                print('current_tab:', current_tab)

                filter_tab_text.find_element_by_id('com.sankuai.meituan:id/filter_tab_big_indicator').get_attribute('resourceId')

                if current_tab == '小吃快餐':
                    break

                else:
                    current_select = False

            except Exception as Se:
                print('Se:', Se)
                current_select = True

            if current_select:
                pass

            else:
                print('Begin change the Select.')
                driver.find_element_by_id('com.sankuai.meituan:id/sort').click()
                driver.find_element_by_android_uiautomator('new UiSelector().text("销量最高")').click()
                time.sleep(0.5)
                driver.find_element_by_android_uiautomator('new UiSelector().text("小吃快餐")').click()
                print('Change finished')
                break


        if Over:
            print('Over:', Over)
            break

        else:
            pass

        StoreItem = driver.find_elements_by_id("com.sankuai.meituan:id/food_dealpoi_food_item_layout")

        sqo = list()
        for lkjhga in StoreItem:
            try:
                print(lkjhga.find_element_by_id("com.sankuai.meituan:id/poi_name").get_attribute('text'))
                sqo.append(lkjhga.find_element_by_id("com.sankuai.meituan:id/poi_name").get_attribute('text'))

            except Exception:
                pass

        if current_page == sqo:
            print('Match success')
            break

        else:
            pass

        for Store in StoreItem:
            try:
                print('Begin locate')
                if Store.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan:id/third_line_single_tag"]/android.widget.TextView[2]').get_attribute('text') == SmallArea:
                    try:
                        # 店铺名字
                        Store_Name = Store.find_element_by_id("com.sankuai.meituan:id/poi_name").get_attribute('text')
                        # 保存当前正在保存中店铺

                        print("Store_Name:\t", Store_Name)

                        if Store_Name not in save_name_list:
                            print(Store_Name, 'not in save_name_list')
                            r.set('current', json.dumps(Store_Name))
                            noSwipeTimes = 0

                        else:
                            print('\n')
                            print('current store name list:\t', sqo)
                            print('save store name list   :\t', save_name_list)
                            print('\n')

                            for sqoa in sqo:
                                if sqoa not in save_name_list:
                                    tiaoguo = True

                                    noSwipeTimes = 0

                                    break

                                else:
                                    tiaoguo = False

                            if tiaoguo:
                                noSwipeTimes = 0
                                continue

                            else:
                                # 当页面内任意一个店铺名字在已保存名单里时就重定位
                                print(Store_Name, 'in save_name_list')

                                try:
                                    print('list     \t', save_name_list)

                                    CheckSlec(driver, BigArea, SmallArea)

                                    while True:
                                        print('Begin Check')
                                        Items = driver.find_elements_by_id("com.sankuai.meituan:id/food_dealpoi_food_item_layout")

                                        lkdo = list()
                                        for lkdsaoj in Items:
                                            try:
                                                print(lkdsaoj.find_element_by_id("com.sankuai.meituan:id/poi_name").get_attribute('text'))
                                                lkdo.append(lkdsaoj.find_element_by_id("com.sankuai.meituan:id/poi_name").get_attribute('text'))

                                            except Exception:
                                                pass

                                        try:
                                            if current_check_names == lkdo:
                                                print('Check Match success')
                                                break

                                            else:
                                                pass

                                        except Exception:
                                            pass

                                        breaka = str()
                                        for lkd in lkdo:
                                            if lkd not in save_name_list:
                                                breaka = True

                                            else:
                                                breaka = False

                                        if breaka:
                                            break

                                        else:
                                            current_check_names = lkdo
                                            print("It's swipe 1600 to 600")
                                            driver.swipe(514, 1600, 514, 600, 900)

                                    print('Check finished')
                                    noSwipeTimes += 1
                                    noSwipe = True
                                    break

                                except Exception as Eq:
                                    print("Eq's wrong:\t", Eq)
                                    break

                        # 店铺评分
                        try:
                            Store_poi = Store.find_element_by_id(
                                "com.sankuai.meituan:id/food_poi_item_evaluate").get_attribute('text')

                        except:
                            save_name_list.append(Store_Name)
                            r.set('list', json.dumps(save_name_list))

                            continue

                        # 人均消费
                        try:
                            Store_avg_price = Store.find_element_by_id(
                                "com.sankuai.meituan:id/avg_price").get_attribute('text')

                        except:
                            save_name_list.append(Store_Name)
                            r.set('list', json.dumps(save_name_list))

                            continue

                        # 食品类型
                        try:
                            Store_tag = Store.find_element_by_xpath(
                                '//*[@resource-id="com.sankuai.meituan:id/third_line_single_tag"]/android.widget.TextView[1]').get_attribute(
                                'text')

                        except:
                            save_name_list.append(Store_Name)
                            r.set('list', json.dumps(save_name_list))

                            continue

                        # 季度销量
                        try:
                            Store_xiaol = Store.find_element_by_id(
                                "com.sankuai.meituan:id/label_content").get_attribute('text')
                            print(Store_xiaol)

                        except NoSuchElementException:
                            print('季度销量未找到!')
                            Store_xiaol = 'None'

                        while True:
                            try:
                                driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(Store_Name)).click()
                                print('Click Store success')
                                break

                            except Exception:
                                print('Click Store failed')
                                print("It's swipe 900 to 1200")
                                driver.swipe(514, 900, 514, 1200, 1000)

                        # Test wheather or not click into Search input
                        if driver.current_activity == 'com.meituan.android.food.search.search.FoodSearchActivity':
                            driver.find_element_by_class_name('android.widget.ImageButton').click()
                            time.sleep(0.5)
                            driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(Store_avg_price)).click()
                            print('Reclick store success')

                        elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
                            pass

                        else:
                            save_name_list.append(Store_Name)
                            r.set('list', json.dumps(save_name_list))

                            raise NoSuchElementException

                        time.sleep(2)

                        # 查看是否有外卖
                        try:
                            driver.find_element_by_id('com.sankuai.meituan:id/food_poi_wai_mai_label')
                            Store_waimai = '是'

                        except NoSuchElementException:
                            Store_waimai = '否'

                        # 查看店铺是否为连锁
                        try:
                            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView').get_attribute('checkable')
                            Store_liansuo = '是'

                        except:
                            Store_liansuo = '否'

                        try:
                            Store_bussiness_time = driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan:id/food_poi_business_time"]/android.support.v4.view.ViewPager/android.widget.TextView').get_attribute('text')

                        except NoSuchElementException:
                            Store_bussiness_time = '没有'

                        driver.find_element_by_android_uiautomator('new UiSelector().text("评价")').click()

                        time.sleep(1)

                        # driver.wait_activity('com.meituan.android.food.poi.FoodPoiDetailActivity', 10)

                        driver.find_element_by_id('com.sankuai.meituan:id/food_poi_comment_total').click()

                        time.sleep(2)

                        driver.wait_activity('com.meituan.android.ugc.review.list.ui.ReviewListActivity', 10)

                        tab_comments = driver.find_elements_by_id('android:id/title')

                        for tab_comment in tab_comments:
                            try:
                                if tab_comment.get_attribute('text')[0:2] == '全部':
                                    Store_comment_quanbu = re.findall('\((.*?)\)', str(tab_comment.get_attribute('text')))[0]

                                else:
                                    pass

                            except IndexError:
                                Store_comment_quanbu = 0

                            try:
                                if tab_comment.get_attribute('text')[0:2] == '低分':
                                    difen = re.findall('\((.*?)\)', str(tab_comment.get_attribute('text')))[0]
                                    difenlv = int(difen) / int(Store_comment_quanbu)

                                else:
                                    pass


                            except Exception:
                                difen = 0
                                difenlv = 0

                            try:
                                if tab_comment.get_attribute('text')[0:2] == '晒图':
                                    shaitu = re.findall('\((.*?)\)', str(tab_comment.get_attribute('text')))[0]
                                    shaitulv = int(shaitu) / int(Store_comment_quanbu)

                                else:
                                    pass

                            except:
                                shaitulv = 0
                                shaitu = 0

                        rowcount = r.get('count')

                        print('\n已保存数量:\t{}'.format(int(rowcount)))
                        print('list:' + ' ', save_name_list, '\n')
                        workbook.write(int(rowcount), 0, Store_Name)
                        print('店铺名字', Store_Name)
                        workbook.write(int(rowcount), 1, Store_tag)
                        print('店铺标签', Store_tag)
                        workbook.write(int(rowcount), 2, Store_poi)
                        print('店铺评分', Store_poi)
                        workbook.write(int(rowcount), 3, Store_xiaol)
                        print('店铺销量', Store_xiaol)
                        workbook.write(int(rowcount), 4, Store_avg_price)
                        print('人均消费', Store_avg_price)
                        workbook.write(int(rowcount), 5, Store_waimai)
                        print('店铺外卖', Store_waimai)
                        workbook.write(int(rowcount), 6, Store_liansuo)
                        print('连锁店铺', Store_liansuo)
                        workbook.write(int(rowcount), 7, Store_bussiness_time.replace('明日', ''))
                        print('营业时间', Store_bussiness_time.replace('明日', ''))
                        workbook.write(int(rowcount), 8, ('%.3f' % difenlv))
                        print('单低分率', ('%.3f' % difenlv))
                        workbook.write(int(rowcount), 9, ('%.3f' % shaitulv))
                        print('单晒图率', ('%.3f' % shaitulv))
                        workbook.write(int(rowcount), 10, BigArea)
                        print('区域名称', BigArea)
                        workbook.write(int(rowcount), 11, SmallArea)
                        print('商圈名称', SmallArea)
                        workbook.write(int(rowcount), 12, difen)
                        print('低分总数', difen)
                        workbook.write(int(rowcount), 13, shaitu)
                        print('晒图总数', shaitu)
                        workbook.write(int(rowcount), 14, Store_comment_quanbu)
                        print('评论总数', Store_comment_quanbu)
                        print('\n')

                        r.set('count', (int(rowcount) + 1))

                        save_name_list.append(Store_Name)
                        r.set('list', json.dumps(save_name_list))

                        driver.tap([(540, 814)], 100)
                        time.sleep(0.5)

                        if driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan:id/action_bar"]/android.widget.TextView').get_attribute('text') == '评价详情':
                            driver.find_element_by_accessibility_id("转到上一层级").click()
                            time.sleep(1)

                        else:
                            pass

                        comment_label_list = [i.get_attribute('text') for i in driver.find_elements_by_id('com.sankuai.meituan:id/comment_label')]
                        label_count_list = [i.get_attribute('text') for i in driver.find_elements_by_id('com.sankuai.meituan:id/lable_count')]

                        for comment_label, label_count in zip(comment_label_list, label_count_list):
                            count = r.get('counttwo')
                            worksheettwo.write(int(count), 0, comment_label)
                            worksheettwo.write(int(count), 1, label_count)
                            r.set('counttwo', (int(count) + 1))

                        driver.find_element_by_class_name('android.widget.ImageButton').click()

                        driver.wait_activity('com.meituan.android.food.poi.FoodPoiDetailActivity', 10)
                        time.sleep(1)

                        driver.find_element_by_class_name('android.widget.ImageButton').click()

                        driver.wait_activity('com.meituan.android.food.homepage.FoodHomePageActivity', 10)

                    except NoSuchElementException:
                        try:
                            save_name_list.append(Store_Name)
                            r.set('list', json.dumps(save_name_list))

                        except:
                            pass

                        print('Not Found')

                        # Test for the activity
                        while True:
                            if driver.current_activity == 'com.meituan.android.pt.homepage.activity.MainActivity':
                                driver.swipe(514, 600, 514, 1600, 900)
                                driver.find_element_by_accessibility_id('美食').click()

                            elif driver.current_activity == 'com.meituan.android.food.homepage.FoodHomePageActivity':
                                break

                            elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
                                driver.keyevent(4)
                                time.sleep(0.5)

                            elif driver.current_activity == 'com.meituan.android.ugc.review.list.ui.ReviewListActivity':
                                driver.keyevent(4)
                                time.sleep(1)
                                driver.keyevent(4)

                            else:
                                driver.keyevent(4)

                        pass

                else:
                    if OverTimes >= 3:
                        Over = True
                        break

                    else:
                        OverTimes += 1

                    continue

            except NoSuchElementException as NS:
                print('locate failed Nos')
                print(NS)
                noSwipe = False

                while True:
                    if driver.current_activity == 'com.meituan.android.pt.homepage.activity.MainActivity':
                        driver.swipe(514, 600, 514, 1600, 900)
                        driver.find_element_by_accessibility_id('美食').click()

                    elif driver.current_activity == 'com.meituan.android.food.homepage.FoodHomePageActivity':
                        break

                    elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
                        driver.keyevent(4)
                        time.sleep(0.5)

                    elif driver.current_activity == 'com.meituan.android.ugc.review.list.ui.ReviewListActivity':
                        driver.keyevent(4)
                        time.sleep(1)
                        driver.keyevent(4)

                    else:
                        driver.keyevent(4)

                continue

            except StaleElementReferenceException as Sta:
                print('locate failed Sta')
                print(Sta)
                noSwipe = False

                while True:
                    if driver.current_activity == 'com.meituan.android.pt.homepage.activity.MainActivity':
                        driver.swipe(514, 600, 514, 1600, 900)
                        driver.find_element_by_accessibility_id('美食').click()

                    elif driver.current_activity == 'com.meituan.android.food.homepage.FoodHomePageActivity':
                        break

                    elif driver.current_activity == 'com.meituan.android.food.poi.FoodPoiDetailActivity':
                        driver.keyevent(4)
                        time.sleep(0.5)

                    elif driver.current_activity == 'com.meituan.android.ugc.review.list.ui.ReviewListActivity':
                        driver.keyevent(4)
                        time.sleep(1)
                        driver.keyevent(4)

                    else:
                        driver.keyevent(4)

                continue

        if noSwipe:
            current_page = 'noSwipe'
            print('noSwipe')

            while True:
                try:
                    if noSwipeTimes >= 10:
                        print('noSwipeTimes too much!')
                        current_page = sqo
                        break

                    else:
                        break

                except Exception as esx:
                    print(esx)
                    noSwipeTimes = 0

        else:
            current_page = sqo
            print('driver swipe 1600 into 650')
            driver.swipe(514, 1600, 514, 650, 1000)

    with open('F:/python files/Meituan/TimeSave/process.txt', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(str(BigArea) + ' ' + str(SmallArea) + 'S'))
