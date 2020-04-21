
def ClickByUi(driver, Keyword):
    poiqweqsd = 1
    while True:
        try:
            print('Click ' + str(poiqweqsd))
            print('Click: ', 'new UiSelector().text("{Keyw}")'.format(Keyw=Keyword))
            driver.find_element_by_android_uiautomator('new UiSelector().text("{Keyw}")'.format(Keyw=Keyword)).click()
            # driver.find_element_by_android_uiautomator('new UiSelector().text("ALLOW")').click()
            print('Click Success')
            break

        except Exception as dsmakld:
            print(dsmakld)
            if poiqweqsd >= 1000:
                raise ValueError

            else:
                poiqweqsd += 1



