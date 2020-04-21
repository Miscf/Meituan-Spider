import requests
from threading import Thread
import time


def req(urlx, inxx, timess):
    print(urlx + inxx)
    ressss = requests.get(urlx + inxx)
    with open('F:/python/av1/{}.ts'.format(timess), 'wb') as fp:
        fp.write(ressss.content)


url = 'https://qq.com-ixx-youku.com/20200104/10329_5a549a5e/1000k/hls/'
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

with open('F:/python/6.ts', 'wb') as f:
    for w in range(times + 1):
        while True:
            try:
                with open('F:/python/av1/{}.ts'.format(w), 'rb') as fpa:
                    f.write(fpa.read())
                    break

            except FileNotFoundError:
                time.sleep(3)
