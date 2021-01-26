from pymouse import PyMouse
from pykeyboard import PyKeyboard

import random
import time

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size() # get the screen parameter

#print(x_dim)
#print(y_dim)

cycle_index = int(input("PLease input the cycle index:"))
i = 1 
time.sleep(10)
while i <= cycle_index :
    if i % 10 == 1:
        print("This is the %dst cycle" % i)
    elif i % 10 == 2:
        print("This is the %dnd cycle" % i)
    elif i % 10 == 3:
        print("This is the %drd cycle" % i)
    else:
        print("This is the %dth cycle" % i)
    x1 = random.randint(int(1377*x_dim/1920)+1,int(1618*x_dim/1920))
    y1 = random.randint(int(828*y_dim/1080)+1,int(879*y_dim/1080))
    m.click(x1, y1, 1)
    delay2 = random.uniform(90,95)
    time.sleep(delay2)
    m.click(x1, y1, 1)#random area is ok
    delay1 = random.uniform(1,3)
    time.sleep(delay1)
    x2 = random.randint(int(1434*x_dim/1920)+1,int(1705*x_dim/1920))
    y2 = random.randint(int(910*y_dim/1080)+1,int(964*y_dim/1080))
    m.click(x2, y2, 1)#“再次挑战”
    
    delay0 = random.uniform(1,6)
    time.sleep(delay0)
    i+=1
