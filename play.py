import requests
from threading import Thread
import time


def req(urlx, inxx, timess):
    print(urlx + inxx)
    ressss = requests.get(urlx + inxx)
    with open('F:/python/av/{}.ts'.format(timess), 'wb') as fp:
        fp.write(ressss.content)


url = 'https://cdn.35zycdn.com/20190413/YURdB5UP/720kb/hls/'
index = requests.get(url + 'index.m3u8').text

index_list = index.split('\n')


mac = str()
times = 0
treads = list()
for inx in index_list:
    if inx[-2:] == 'ts':
        times += 1
        treads.append(Thread(target=req, args=(url, inx, times)))


print('treads finished')
for thread, ti in zip(treads, range(len(treads))):
    thread.start()
    thread.join(1)

with open('F:/python/5.ts', 'wb') as f:
    for w in range(1, times + 1):
        while True:
            try:
                with open('F:/python/av/{}.ts'.format(w), 'rb') as fpa:
                    f.write(fpa.read())
                    break

            except Exception as E:
                print(E)
                time.sleep(3)
