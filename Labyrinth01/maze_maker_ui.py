#UI of MazeMaker PY

from tkinter import simpledialog as spd
from tkinter import colorchooser as cls
from tkinter import messagebox as msg
import maze_maker as mm
import turtle as t

def draw_maze(steps=500,pensize=10,endcolor=(0,0.5,0),start_color=(0,0,0),length=10,bgcolor=(0,0,0),dirs=[(0,-1),(0,-2),(0,1),(0,2),(1,0),(2,0),(-1,0),(-2,0)]):
    t.hideturtle()
    wd = t.Screen()
    wd.bgcolor(bgcolor)
    map = [[False for i in range(64)] for i in range(64)]
    a = t.Turtle()
    a.hideturtle()
    a.pencolor(start_color)
    a.pensize(pensize)
    a.pendown()
    #KNIGHT:[(2,1),(1,2),(-1,2),(2,-1),(-2,1),(1,-2),(-1,-2),(-2,-1)]
    #ANCIENT ASIAN WINDOW:[(0,-1),(0,-2),(0,1),(0,2),(1,0),(2,0),(-1,0),(-2,0)]
    #DEFAULT (1 LINE MAZE):[(1,0),(-1,0),(0,1),(0,-1)]
    mm.maze(pen=a,steps=steps,map=map,starting_loc=[32,32],end_color=endcolor,dirs=dirs,length=length)
    a.penup()

    t.done()

def whole_muti(tup,fac):
    ori_type = type(tup)
    l = list(tup)
    for i in range(len(l)):
        l[i] *= fac
    return ori_type(l)
    

def main():
    title = "Maze (Labyrinth) Maker\n"
    steps = spd.askinteger(title="IN...",prompt=f"{title}How many Steps (Possible MAX)?")
    if not steps:
        return
    length = spd.askinteger(title="IN...",prompt=f"{title}How long the grid side is?")
    if not length:
        return
    pen_size = spd.askinteger(title="IN...",prompt=f"{title}How large the pen is?")
    if not pen_size:
        return

    while 1:
        bg_color = cls.askcolor(title="Background Color?")
        if(bg_color[1]):
            break
        else:
            msg.showinfo(message="Please Select a Starting Color!")
    bg_color = whole_muti(bg_color[0],1/255)

    while 1:
        s_color = cls.askcolor(title="Starting Color?")
        if(s_color[1]):
            break
        else:
            msg.showinfo(message="Please Select a Starting Color!")
    s_color = whole_muti(s_color[0],1/255)

    while 1:
        e_color = cls.askcolor(title="Ending Color?")
        if(e_color[1]):
            break
        else:
            msg.showinfo(message="Please Select a Ending Color!")
    e_color = whole_muti(e_color[0],1/255)
    try:
        with open("./dirs.txt","rt",encoding="utf-8") as f:
            f_cleared = []
            for i in f.readlines():
                if(i and i != "\n" and not("#" in i)):f_cleared.append(i)
            dirs = [tuple([int(j) for j in i.split(",")]) for i in f_cleared]
    except Exception as e:
        msg.showwarning(title="ERROR",message="Rule Sheet Reading Error\nPlease check if it doesn't exist(dirs.txt) or written with error.")
    try:
        draw_maze(steps=steps,pensize=pen_size,endcolor=e_color,start_color=s_color,length=length,dirs=dirs,bgcolor=bg_color)
    except:
        msg.showwarning(title="ERROR",message="Drawing Error\nPlease check if the Rule Sheet(dirs.txt) contains bad prompts.")

if __name__ == "__main__":
    main()