# coding=utf-8

import requests
import pyglet
from wbd.conf import setting,path_conf

# 项目参考
# 参考: https://www.cnblogs.com/xe2011/p/11583645.html
# 参考: https://www.cnblogs.com/xe2011/p/4315879.html

# 1 获取输入查询的字
input_char = "你"
img_one_file_path = path_conf.GIFTS_DIR_PATH + "/" + input_char + ".png"
# print(img_one_file_path)

# 2 获取字的img文件
img_one_file_res = requests.get(setting.url_1.format(input_char))
with open(img_one_file_path, "wb")as f:
    f.write(img_one_file_res.content)

# 3 查询字的编码
print(setting.query_char_url.format(char_name=input_char))
# query_char_res = requests.get(setting.query_char_url.format(char_name=input_char))
# print(query_char_res.text)

# 4 显示文字和编码
'''
# pick an animated gif file you have in the working directory
animation = pyglet.resource.animation(img_one_file_path)
sprite = pyglet.sprite.Sprite(animation)
# create a window and set it to the image size
win = pyglet.window.Window(width=sprite.width, height=sprite.height)
# set window background color = r, g, b, alpha
# each value goes from 0.0 to 1.0
green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)
@win.event
def on_draw():
    win.clear()
    sprite.draw()
pyglet.app.run()
'''
print("finish")
