import random
import pygame
from PIL import Image
import os

font_size = 20  # 字体大小
text = '0'  # 字体内容
# 每张图缩放的尺寸（后面用的）
size = 500
img_name = 'new_img.jpg'  # 生成文件的文件名

# 初始化，pygame使用必须
pygame.init()

# 这里是利用pygame来创造字体
font = pygame.font.Font('simkai.ttf', font_size)  # 这是字体文件，啥都行
# RGB值，白色背景，黑色字体
font_text = font.render(text, True, (0, 0, 0), (255, 255, 255))  # 字的内容为text， 有锯齿， 字体黑，背景白
height = font_text.get_height()
width = font_text.get_width()

# 转成二维列表
image_row_list = []
for y in range(height):
    image_col_list = []
    for x in range(width):
        # 是字体的像素就变成1，白色变成0，后续会在1贴图
        if font_text.get_at((x, y))[0] == 1:
            image_col_list.append(1)
        else:
            image_col_list.append(0)
    image_row_list.append(image_col_list)

# 中间效果图展示
# for row in image_row_list:
#     for col in row:
#         if col == 1:
#             print('1', end='')
#         else:
#             print(' ', end='')
#     print()

# 获取二维列表高度和宽度
width = len(image_row_list[0])
height = len(image_row_list)

# 贴图
new_image = Image.new('RGB', (width*size, height*size), (255, 255, 255))  # 白色背景

print('正在装载图片...')
# 注意这里要有imgs文件夹，图片全放里面
img_li = os.listdir('imgs')
for row in range(height):
    for col in range(width):
        if image_row_list[row][col] == 1:
            source_image = Image.open('imgs\\' + random.choice(img_li))
            # 这里是将每个图片变成统一大小，相当于新图的像素
            source_image = source_image.resize((size, size), Image.ANTIALIAS)  # 使用抗锯齿
            new_image.paste(source_image, (col*size, row*size))

print('正在保存图像...')
new_image.save(img_name)
print('生成完毕')
