import re
import requests
import urllib.parse #解码的汉字转换成字符串
# name = input('请输入歌手的名字:')
# p = input('下载第几页：')
# k = input('多少首歌曲：')# 总共有30首歌曲
name = '谪仙'
p=1
k = 1
name = urllib.parse.quote(name)
url =f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={name}&pn={p}&rn={k}'
#cookie会过期 下次再爬可能不能使用了。
headers={
 'Cookie': '_ga=GA1.2.376063748.1674008881; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1674008881,1676181375; _gid=GA1.2.859917752.1676181375; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1676187337; kw_token=CBQHDVFFOMD',
 'csrf': 'CBQHDVFFOMD',
 'Host': 'www.kuwo.cn',
 'Pragma': 'no-cache',
 'Referer': f'http://www.kuwo.cn/search/list?key={name}',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
response = requests.get(url=url ,headers=headers)
json_data = response.json()
data_list = json_data['data']['list']
for data in data_list:
    song_name = data['name']
    singer = data['artist']
    album_name = data['album']
    rid = data['rid']
    music_info_url = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=convert_url3'#重要的接口其他都类似
    music_json = requests.get(url=music_info_url,headers=headers).json()
    music_url = music_json['data']['url']
    print(music_json['data'])
    # print(music_url)
    music_data = requests.get(music_url).content
    
    song_name = re.sub(r'[\/:"<>|*?]','',song_name)
    song_name = song_name.replace("&nbsp;", "")
    singer = singer.replace("&nbsp;", "")
    with open(f'd:/mp3/{song_name}-{singer}.mp3', mode='wb') as f:#保存数据的地方
        f.write(music_data)
        print(song_name, '爬取成功')
