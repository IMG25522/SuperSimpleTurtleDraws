import turtle as t
import random as rd
import webcolors as wbc

def get_mix(start_,end_,place_):#place:0~1, it decided where the position between min and max
    return start_+(end_-start_)*place_

def color_words_to_rgb(color):
    try:
        return wbc.name_to_rgb(color)
    except:
        return color

def point_ok(loc,map):
    if loc[0]<0 or loc[1]<0 or loc[0]>=len(map) or loc[1]>=len(map[0]):
        return False
    else:
        if (map[loc[0]][loc[1]]):
            return False
        else:
            return True

def no_way(loc,map,dirs):
    ori_loc = loc.copy()
    for i in dirs:
        loc[0] = ori_loc[0] + i[0]
        loc[1] = ori_loc[1] + i[1]
        if(point_ok(loc,map)):
            return False
    else:
        return True

def maze_step(pen:t.Turtle,map,length,loc,start,dirs,color=None):
    if(color):pen.color(color)
    ori_loc = loc.copy()
    running = True
    if(no_way(loc,map,dirs)):
        running = False
        return loc,map,running
    while 1:
        togo = rd.choice(dirs)
        loc[0] = ori_loc[0] + togo[0]
        loc[1] = ori_loc[1] + togo[1]
        if(point_ok(loc,map)):
            map[loc[0]][loc[1]] = True
            break
    pen.goto(loc[0]*length+start[0],loc[1]*length+start[1])
    return loc,map,running

def maze(pen:t.Turtle,steps:int,map,length,dirs=[(1,0),(-1,0),(0,1),(0,-1)],starting_loc=[0,0],end_color=None):
    ori_color = color_words_to_rgb(pen.color()[0])
    pen.color(ori_color)
    #print(pen.color())
    map[starting_loc[0]][starting_loc[1]] = True
    loc = starting_loc
    start = (t.pos()[0] - starting_loc[0]*length, t.pos()[1] - starting_loc[1]*length)
    for i in range(steps):
        loc,map,running = maze_step(pen,map,length,loc,start,dirs,color=tuple(get_mix(ori_color[j],end_color[j],i/(steps-1)) for j in range(len(pen.color()[0]))) )
        if(not running):
            print(i)
            break
    else:
        print(steps)

def main():
    t.hideturtle()
    wd = t.Screen()
    wd.bgcolor("#ffffff")
    map = [[False for i in range(64)] for i in range(64)]
    a = t.Turtle()
    a.hideturtle()
    a.pencolor("#ffffff")
    a.pensize(5)
    a.pendown()
    #KNIGHT:[(2,1),(1,2),(-1,2),(2,-1),(-2,1),(1,-2),(-1,-2),(-2,-1)]
    #ANCIENT ASIAN WINDOW:[(0,-1),(0,-2),(0,1),(0,2),(1,0),(2,0),(-1,0),(-2,0)]
    #DEFAULT (1 LINE MAZE):[(1,0),(-1,0),(0,1),(0,-1)]
    maze(a,500,map,10,starting_loc=[32,32],end_color=(0,0,0),dirs=[(0,-1),(0,-2),(0,1),(0,2),(1,0),(2,0),(-1,0),(-2,0)])
    a.penup()

    t.done()

if __name__ == "__main__":
    main()