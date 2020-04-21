from manage import program
from xlutils.copy import copy
from program.main import main_program
import redis
import xlrd
import json


def login(wrong):
    while True:
        try:
            print('logining...')
            driver = main_program(driver=0, step=0, BigArea=0, SmallArea=0, workbook=0, r=0, cont=0, workbooktwo=0,
                                  wrong=wrong)

            return driver

        except:
            pass


with open('TimeSave/process.txt', 'w', encoding='utf-8') as f:
    f.write('0Step')

oldOBJ = xlrd.open_workbook(r'F:\\python files\\Meituan\\results\\Meituan.xls')
workbook = copy(oldOBJ)
worksheet = workbook.get_sheet(0)

oldOBJTWO = xlrd.open_workbook(r'F:\\python files\\Meituan\\results\\pl.xls')
workbooktwo = copy(oldOBJTWO)
worksheettwo = workbooktwo.get_sheet(0)

# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('sheet', cell_overwrite_ok=True)
#
# workbooktwo = xlwt.Workbook(encoding='utf-8')
# worksheettwo = workbooktwo.add_sheet('sheet', cell_overwrite_ok=True)

conti = False

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
print('Connection success')

# r.set('current', 'None')
# r.set('list', 'None')
# r.set('counttwo', 0)
# r.set('count', 1)

while True:
    try:
        with open('F:/python files/Meituan/TimeSave/process.txt', 'r', encoding='utf-8') as f:
            if str(f.read()) == '0Step':
                print('Get AreasList succss')
                break

            else:
                print('Match Failed')
                main_program(driver, 1, 0, 0, 0, 0, 0, 0, False)

    except:
        print('Something wrong')
        driver = login(False)

with open('F:/python files/Meituan/TimeSave/DownloadAreas.txt', 'r', encoding='utf-8') as op:
    AreasList = json.loads(op.read())


print('AreasList : ', AreasList)
for Areas in AreasList:
    BigArea = Areas[0]

    for SmallArea in Areas[1]:

        sheets = oldOBJ.sheets()[0]

        Areass = sheets.col_values(11)

        sheetstwo = oldOBJTWO.sheets()[0]

        Pl = sheetstwo.col_values(0)

        if SmallArea in Areass:
            print('next')
            continue

        else:
            pass

        print('Areass', len(Areass))
        r.set('count', int(len(Areass) + 1))

        print('Pl:', len(Pl))
        r.set('counttwo', int(len(Pl) + 1))

        print(BigArea, SmallArea)
        conti = False

        while True:
            try:
                program(BigArea, SmallArea, workbook, worksheet, workbooktwo, worksheettwo, conti, r)
                break

            except Exception as Es:
                print('------------------------------')
                print(Es)
                print('------------------------------')
                workbook.save(r'F:\\python files\\Meituan\\results\\Meituan.xls')
                workbooktwo.save(r'F:\\python files\\Meituan\\results\\pl.xls')

                oldOBJ = xlrd.open_workbook(r'F:\\python files\\Meituan\\results\\Meituan.xls')
                workbook = copy(oldOBJ)
                worksheet = workbook.get_sheet(0)

                oldOBJTWO = xlrd.open_workbook(r'F:\\python files\\Meituan\\results\\pl.xls')
                workbooktwo = copy(oldOBJTWO)
                worksheettwo = workbooktwo.get_sheet(0)

                conti = True
