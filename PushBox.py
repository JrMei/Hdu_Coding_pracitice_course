
import turtle

import level


ms = turtle.Screen()

ms.setup(900, 650, 200, 0)


ms.title('推箱子小游戏')

ms.register_shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\wall.gif')
ms.register_shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\o.gif')          # 正确箱子位置标识图片
ms.register_shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\p.gif')          # 小人
ms.register_shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\box.gif')        # 箱子
ms.register_shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\boxc.gif')       # 推到正确位置，箱子变色



ms.tracer(0)        #追踪 屏幕刷新


levels = level.level_list()




class Pen(turtle.Turtle):   
   
    def __init__(self, pic):
        super().__init__()
        self.shape(pic)     
        self.penup()       

  
    def move(self, x, y, px, py):
        gox, goy = x+px, y+py
   
        if (gox, goy) in go_space:
            self.goto(gox, goy)
 
        if (gox+px, goy+py) in go_space and (gox, goy) in box_space:

            for i in box_list:
                if i.pos() == (gox, goy):            
                
                    go_space.append(i.pos())
                    
                    box_space.remove(i.pos())

                    i.goto(gox+px, goy+py)              
                    self.goto(gox, goy)                 


                    go_space.remove(i.pos())
                    
                    box_space.append(i.pos())

                    if i.pos() in correct_box_space:    

                        i.shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\boxc.gif')
                    else:

                        i.shape('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\box.gif')

                    if set(box_space) == set(correct_box_space):    #列表变成集合
                        text.show_win()                             #提示游戏赢了


    def go_up(self):            #上
        self.move(self.xcor(), self.ycor(), 0, 50)
    def go_down(self):          #下
        self.move(self.xcor(), self.ycor(), 0, -50)
    def go_left(self):          #左
        self.move(self.xcor(), self.ycor(), -50, 0)
    def go_right(self):         #右
        self.move(self.xcor(), self.ycor(), 50, 0)




class Game():
    def paint(self):    #定义一个画的方法

        i_date = len(levels[num-1])         #行
        j_date = len(levels[num-1][0])      #列


        for i in range(i_date):

            for j in range(j_date):

                x = -j_date*25+25+j*50 + sister_x
                y = i_date*25-25-i*50

                if levels[num-1][i][j] == 'O':
                    correct_box.goto(x, y)
                    correct_box.stamp()         #设置正确箱子的位置不需要移动，盖个章
                    go_space.append((x, y))
                    correct_box_space.append((x, y))
        for i in range(i_date):
            for j in range(j_date):


                x = -j_date*25+25+j*50 + sister_x       #-175+j*50      x增加
                y = i_date*25-25-i*50                   #175-i*50       y减少


                if levels[num-1][i][j] == ' ':
                    go_space.append((x, y))

                if levels[num-1][i][j] == 'X':
                    wall.goto(x, y)

                    wall.stamp()

                if levels[num-1][i][j] == 'P':
                    player.goto(x, y)
                    go_space.append((x, y))

                if levels[num-1][i][j] == 'B':
                    box = Pen('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\box.gif')            #画箱子
                    box.goto(x, y)
                    box_list.append(box)
                    box_space.append((x, y))




class ShowMessage(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('blue')
        self.ht()       #隐藏海龟鼠标


    def message(self):
        self.goto(0+sister_x, 290)
        self.write(f'第{num}关', align='center', font=('仿宋', 20, 'bold'))
        self.goto(0+sister_x, 270)
        self.write('重新开始本关请按回车键', align='center', font=('仿宋', 15, 'bold'))
        self.goto(0+sister_x, 250)
        self.write('选择关卡请按Q', align='center', font=('仿宋', 15, 'bold'))


    def show_win(self):
        global num  #全局变量
        if num == len(levels):  #走到了最后一关
            num = 1
            self.goto(0, 0)
            self.write('你已全部过关', align='center', font=('黑体', 30, 'bold'))
            self.goto(0, -50)
            self.write('返回第一关轻按空格键', align='center', font=('黑体', 30, 'bold'))
        else:                   #继续自动进入下一关
            num = num+1
            self.goto(0, 0)
            self.write('恭喜过关', align='center', font=('黑体', 30, 'bold'))
            self.goto(0, -50)
            self.write('进入下一关请按空格键', align='center', font=('黑体', 30, 'bold'))




def init():

    text.clear()

    wall.clear()

    correct_box.clear()

    for i in box_list:
        i.ht()      #隐藏海龟
        del(i)      #删除海龟
    box_list.clear()

    box_space.clear()

    go_space.clear()

    correct_box_space.clear()


    game.paint()

    text.message()





def choose():
    global num
    a = ms.numinput('选择关卡', '你的选择（请输入1-5）', 1)
    if a is None:
        a = num
    num = int(a)    #确定输入的关卡
    init()          #初始化
    ms.listen()     #屏幕监听




sister_x = 225              #游戏地图显示的位置右移距离，给左边照片让出位置
num = 1                     #默认从第1关开始
correct_box_space = []      #正确的箱子列表（正确箱子位置标识图片）
box_list = []               #设置有箱子海龟的列表
box_space = []              #箱子移动所在位置的坐标列表
go_space = []               #人的列表


wall = Pen('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\wall.gif')          # 画墙
correct_box = Pen('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\o.gif')      # 画箱子应该去的正确位置：O代表
player = Pen('D:\\python代码文件\\Turtle_pushbox-main\\推箱子Turtle\\p.gif')           # 画：玩家所在的位置P代表


game = Game()
game.paint()


text = ShowMessage()        # 创建对象
text.message()              # 调用message() 方法


ms.listen()
ms.onkey(player.go_up, 'Up')                #上
ms.onkey(player.go_down, 'Down')            #下
ms.onkey(player.go_left, 'Left')            #左
ms.onkey(player.go_right, 'Right')          #右
ms.onkey(init, 'Return')                    #回车 开始当前
ms.onkey(init, 'space')                     #空格 开始下一关
ms.onkey(choose, 'Q')                       #Q键退出


while True:
    ms.update()


ms.mainloop()
