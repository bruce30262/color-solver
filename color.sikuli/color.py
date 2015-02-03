from java.awt import Robot
from java.awt import Color
from java.awt import Rectangle
from time import time

def getListColor(SCREEN): #pass a Region and get pixel (r,g,b)    
    i = Robot().createScreenCapture(Rectangle(SCREEN.getX(),
                SCREEN.getY(), SCREEN.getW(), SCREEN.getH()))
   
    c = Color(i.getRGB(0, 0))
    return c.getRed(), c.getGreen(), c.getBlue()


def setdict(cur_x, cur_y):
    global d, multi
    key = getListColor( Region(cur_x, cur_y, 10, 10) )

    if key in d:
        d.get(key).append((cur_x, cur_y))
        multi=True
    else:
        d[key] = [(cur_x, cur_y)]
        
        
def solve(num, cur_offset, cur_start_x, cur_start_y):
    global d, multi 
    d, multi = {}, False

    for i in range(num):
        cur_x = cur_start_x + i*cur_offset
        for j in range(num):
            cur_y = cur_start_y + j*cur_offset
            setdict(cur_x, cur_y) # record {(r,g,b):(x,y)}
           
            if multi == True: # more than 1 square has same color
                for value in d.values():
                    if len(value) == 1: #return answer
                        return value[0]
                        
def play():
    start_time = time()

    # start point might be different (browser, screen....)
    start_x, start_y = 775, 340 
            
    level_length = [2, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8]
    cnt=1
    
    for i in range(150): 
        level_length.append(9)
    
    for i in level_length:
        
        end_time = time()
        time_taken = end_time - start_time # time_taken is in seconds
        if(time_taken >= 60): # game end
            break
        
        print "solving level", cnt
        cnt += 1
        cur_offset = 500/i
        cur_start_x , cur_start_y = start_x + cur_offset/2, start_y + cur_offset/2

        hover( Location(cur_start_x, cur_start_y) )

        x, y = solve(i, cur_offset, cur_start_x, cur_start_y)
        click( Location(x, y) )


openApp("firefox http://game.ioxapp.com/color")
wait(3)
Settings.MoveMouseDelay = 0.01

if exists("start.png"):
    click("start.png")
    play()
    
else:
    print "timeout"