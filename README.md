# KuwoMusicSpider
使用python 爬取酷我音乐的一个简单爬虫，适合自己用，比较简单
需要注意的是，requests使用的参数中有2个是必须的，否则就会报错，
'Cookie': '_ga=GA1.2.376063748.1674008881; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1674008881,1676181375; _gid=GA1.2.859917752.1676181375; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1676187337; kw_token=CBQHDVFFOMD',
 'csrf': 'CBQHDVFFOMD',
 
 这两个参数具体可以通过在页面中F12调试一下，就可以获取了，csrf与cookie中是一致的，
 而页面的中的数量，我具体设置过50，都可以用；
 
 备注：
 QQ音乐总是变来变去，企鹅页面相对复杂，而且VIP的歌曲未登录只能下载的部分，

github有人做了部分工作，提供了源码爬取了相关的信息，但是没有给下载的代码；

https://github.com/yangjianxin1/QQMusicSpider

这里补充一下资源地址分析过程，

企鹅音乐使用该页面播放：https://y.qq.com/n/ryqq/player

F12，在网络调试信息中最缓存文件大小过滤发现：能达到M字节的一般就是了，如下


如果找不到，可以点击左侧任意一个歌曲播放，都是可以的，URL的模式如下：
https://dl.stream.qqmusic.qq.com/C400002B6KcC243dNu.m4a?guid=6585355648&vkey=35BD35C627BEC49855575A245892F4C4EABBA1ABAC26BF040AF611EC6CD74D2716B4BE4C0D9794E51683DDEA148DD51A5AFC1BF6CE60FA85&uin=&fromtag=120032

这个就是下载文件的地址了，可以绕过限制下载的逻辑。

祝大家好运。
