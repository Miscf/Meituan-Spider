from program.settings import drivers
from program.SaveAllAreas import DownloadAreaNames
from program.Store.SelectArea import SelectArea
from program.Store.DownloadStoreMessage import DownloadStore


def main_program(driver, step, BigArea, SmallArea, workbook, r, cont, workbooktwo, wrong):
    if step == 1:
        DownloadAreaNames(driver=driver)

    elif step == 2:
        SelectArea(driver=driver, BigArea=BigArea, SmallArea=SmallArea)

    elif step == 3:
        DownloadStore(driver, BigArea, SmallArea, workbook, r, cont, workbooktwo)

    else:
        driver = drivers(Wrong=wrong)
        return driver
