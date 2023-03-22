import re
import requests
import urllib.parse #解码的汉字转换成字符串
import os.path

headers1={
 'Host': 'www.ximalaya.com',
 'Pragma': 'no-cache',
 'Referer': f'https://www.ximalaya.com/',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

def getMusicInfo(track_id):
    global headers1
    url1 = "https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1".format(track_id)
    response = requests.get(url=url1 ,headers=headers1)
    #print(response.headers)
    json_data = response.json()
    src = json_data["data"]["src"]
    return src

def downloadMusic(src, dir, name):
    #保存数据的地方
    music_data = requests.get(src).content
    with open(f'd:/mp3/{name}', mode='wb') as f:
        f.write(music_data)
        print(name, '爬取成功')

'''
入口，搜索某个专辑
'''
album = f'https://www.ximalaya.com/album/21722321'
albumId = album.split('/')[-1]
def search():
    # name = input('请输入歌手的名字:')
    # p = input('下载第几页：')
    # k = input('多少首歌曲：')# 总共有30首歌曲
    name = '黄诗扶 楚风起'
    p=1
    k = 2

    name = urllib.parse.quote(name)
    url =f'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={albumId}&pageNum=1&pageSize=50'


    response = requests.get(url=url ,headers=headers1)
    print(response.headers)
    json_data = response.json()
    #print(json_data)
    data = json_data['data']
    print(len(data))
    tracklist = data['tracks']
    if (tracklist and len(tracklist) > 0):
        for i in range(0, len(tracklist)):
            track = tracklist[i]
            track_id = track["trackId"]
            title = track["title"]
            url = track["url"]
            src = getMusicInfo(track_id)
            name = title + "." + src.split(".")[-1] 
            print("{} {} {} {} {}".format(track_id, title, url, src, name))
            downloadMusic(src, f"d:/mp3", name)
            
    return 

search()
