import os
import os.path
import shutil

colors = [
"red", 
"green", 
"blue", 
"purple"
]
for color in colors:
	print(color)
    dir = os.path.join('/',color)
    #dir = 'colors'
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    #print(color)