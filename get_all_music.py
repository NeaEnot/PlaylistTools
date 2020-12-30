import os
import random
import time

dir_from = 'Все песни'

try:
    files = os.listdir(dir_from)
    files.sort()

    with open('Музыка.txt', 'w', encoding='utf-8') as file:
        for track in files:
            file.write(track + '\n')
            print(track)
            
except Exception as e:
    print(e)
    time.sleep(10)