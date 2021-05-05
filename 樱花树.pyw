try:
    from time import sleep
    import random
    from turtle import *
    from random import *
    from math import *
    from random import randint
    r = randint(0, 3)
    if r == 0:
        class Tree:
            def __init__(self):
                setup(1000, 700)
                bgcolor(1, 1, 1)  # 背景色
                hideturtle()
                speed(0)  # 速度 1-10渐进，0 最快
                tracer(1, 0)    # 设置绘图屏幕刷新频率，参数1设置在正常刷新频次的第参数1次刷新，参数2设置每次刷新的时延
                #tracer(0, 0)
                pu()  # 抬笔
                backward(100)
                # 保证笔触箭头方向始终不向下，此处使其左转90度，而不是右转
                left(90)  # 左转90度
                backward(300)  # 后退300

            def tree(self, n, l):
                pd()  # 下笔
                # 阴影效果
                t = cos(radians(heading() + 45)) / 8 + 0.25
                pencolor(t, t, t)
                pensize(n / 1.2)
                forward(l)  # 画树枝
                if n > 0:
                    b = random() * 15 + 10  # 右分支偏转角度
                    c = random() * 15 + 10  # 左分支偏转角度
                    d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
                    # 右转一定角度,画右分支
                    right(b)
                    self.tree(n - 1, d)
                    # 左转一定角度，画左分支
                    left(b + c)
                    self.tree(n - 1, d)
                    # 转回来
                    right(c)
                else:
                    # 画叶子
                    right(90)
                    n = cos(radians(heading() - 45)) / 4 + 0.5
                    pencolor(n, n * 0.8, n * 0.8)
                    fillcolor(n, n * 0.8, n * 0.8)
                    begin_fill()
                    circle(3)
                    left(90)
                    end_fill()
                    # 添加0.3倍的飘落叶子
                    if random() > 0.7:
                        pu()
                        # 飘落
                        t = heading()
                        an = -40 + random() * 40
                        setheading(an)
                        dis = int(800 * random() * 0.5 + 400 * random()
                                  * 0.3 + 200 * random() * 0.2)
                        forward(dis)
                        setheading(t)
                        # 画叶子
                        pd()
                        right(90)
                        n = cos(radians(heading() - 45)) / 4 + 0.5
                        pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
                        fillcolor(n, n * 0.8, n * 0.8)
                        begin_fill()
                        circle(2)
                        left(90)
                        end_fill()
                        pu()
                        # 返回
                        t = heading()
                        setheading(an)
                        backward(dis)
                        setheading(t)
                        # pass
                pu()
                backward(l)  # 退回

        if __name__ == '__main__':
            tree = Tree()
            tree.tree(12, 100)  # 递归7层
            done()
    elif r == 1:
        import turtle
        # 画樱花的躯干(60,t)

        def tree(branchLen, t):
            if branchLen > 3:
                if 8 <= branchLen <= 12:
                    if random.randint(0, 2) == 0:
                        t.color('snow')  # 白
                    else:
                        t.color('lightcoral')  # 淡珊瑚色
                    t.pensize(branchLen / 3)
                elif branchLen < 8:
                    if random.randint(0, 1) == 0:
                        t.color('snow')
                    else:
                        t.color('lightcoral')  # 淡珊瑚色
                    t.pensize(branchLen / 2)
                else:
                    t.color('sienna')  # 赭(zhě)色
                    t.pensize(branchLen / 10)  # 6
                t.forward(branchLen)
                a = 1.5 * random.random()
                t.right(20 * a)
                b = 1.5 * random.random()
                tree(branchLen - 10 * b, t)
                t.left(40 * a)
                tree(branchLen - 10 * b, t)
                t.right(20 * a)
                t.up()
                t.backward(branchLen)
                t.down()
        # 掉落的花瓣

        def petal(m, t):
            for i in range(m):
                a = 200 - 400 * random.random()
                b = 10 - 20 * random.random()
                t.up()
                t.forward(b)
                t.left(90)
                t.forward(a)
                t.down()
                t.color('lightcoral')  # 淡珊瑚色
                t.circle(1)
                t.up()
                t.backward(a)
                t.right(90)
                t.backward(b)

        def main():
            # 绘图区域
            t = turtle.Turtle()
            # 画布大小
            w = turtle.Screen()
            t.speed(0)
            t.hideturtle()  # 隐藏画笔
            t.getscreen().tracer(5, 0)
            w.screensize(bg='wheat')  # wheat小麦
            t.left(90)
            t.up()
            t.backward(150)
            t.down()
            t.color('sienna')
            # 画樱花的躯干
            tree(60, t)
            # 掉落的花瓣
            petal(200, t)
            done()

        main()
    elif r == 2:
        from turtle import *
        from random import *
        from math import *

        def tree(n, l):
            pd()  # 下笔
            # 阴影效果
            t = cos(radians(heading() + 45)) / 8 + 0.25
            pencolor(t, t, t)
            pensize(n / 4)
            forward(l)  # 画树枝
            if n > 0:
                b = random() * 15 + 10  # 右分支偏转角度
                c = random() * 15 + 10  # 左分支偏转角度
                d = l * (random() * 0.35 + 0.6)  # 下一个分支的长度
                # 右转一定角度，画右分支
                right(b)
                tree(n - 1, d)
                # 左转一定角度，画左分支
                left(b + c)
                tree(n - 1, d)
                # 转回来
                right(c)
            else:
                # 画叶子
                right(90)
                n = cos(radians(heading() - 45)) / 4 + 0.5
                pencolor(n, n, n)
                circle(2)
                left(90)
            pu()
            backward(l)  # 退回

        bgcolor(0.5, 0.5, 0.5)  # 背景色
        hideturtle()  # 隐藏turtle
        speed(0)  # 速度，1-10渐进，0最快
        tracer(0, 0)
        left(90)  # 左转90度
        pu()  # 抬笔
        backward(300)  # 后退300
        tree(13, 100)  # 递归7层
        done()
    else:
        from random import *
        from math import *

        def tree(n, l):
            setup(1000, 800)
            pd()  # 下笔
            # 阴影效果
            t = cos(radians(heading() + 45)) / 8 + 0.25
            pencolor(t, t, t)
            pensize(n / 3)
            forward(l)  # 画树枝
            if n > 0:
                b = random() * 15 + 10  # 右分支偏转角度
                c = random() * 15 + 10  # 左分支偏转角度
                d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
                # 右转一定角度，画右分支
                right(b)
                tree(n - 1, d)
                # 左转一定角度，画左分支
                left(b + c)
                tree(n - 1, d)
                # 转回来
                right(c)
            else:
                # 画叶子
                right(90)
                n = cos(radians(heading() - 45)) / 4 + 0.5
                pencolor(n, n * 0.8, n * 0.8)
                circle(3)
                left(90)
                # 添加0.3倍的飘落叶子
                if (random() > 0.7):
                    pu()
                    # 飘落
                    t = heading()
                    an = -40 + random() * 40
                    setheading(an)
                    dis = int(800 * random() * 0.5 + 400 * random()
                              * 0.3 + 200 * random() * 0.2)
                    forward(dis)
                    setheading(t)
                    # 画叶子
                    pd()
                    right(90)
                    n = cos(radians(heading() - 45)) / 4 + 0.5
                    pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
                    circle(2)
                    left(90)
                    pu()
                    # 返回
                    t = heading()
                    setheading(an)
                    backward(dis)
                    setheading(t)
            pu()
            backward(l)  # 退回

        bgcolor(0.5, 0.5, 0.5)  # 背景色
        hideturtle()  # 隐藏turtle
        speed(0)  # 速度，1-10渐进，0最快
        tracer(0, 0)
        pu()  # 抬笔
        backward(100)
        left(90)  # 左转90度
        pu()  # 抬笔
        backward(300)  # 后退300
        tree(12, 100)  # 递归7层
        done()
except Exception as e:
    print(e)
