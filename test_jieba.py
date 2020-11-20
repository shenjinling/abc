import jieba  #分词
from matplotlib import pyplot as plt  #绘图，数据可视化
from wordcloud import WordCloud  #词云
from PIL import Image  #图片处理
import numpy as np #矩阵运算
import sqlite3  #数据库


#准备词云所准备的文字
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select instrodution from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
    #print(item)
#print(text)

cur.close()
con.close()


#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))


#生成好遮罩的图片
img = Image.open(r'./static/assets/images/tree.jpg')  #打开遮罩图片
img_arrag = np.array(img)  #将图片转换为数组
wc = WordCloud(#词云
    background_color='white',#输出图片的背景颜色
    mask=img_arrag,#遮罩的图片
    font_path="msyhl.ttc"   #字体所在位置：C:/Windows/Fonts

)
wc.generate_from_text(string)#把切好的词放进去


#绘制图片
fig = plt.figure(1)
plt.imshow(wc)#按照词云规则显示出来
plt.axis('off')  #是否显示坐标轴

#plt.show()      #显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'./static/assets/images/tree1.jpg')