import os
import random
import time

dir_from = 'Все песни'

def get_all_music(show_log = False):
    try:
        files = os.listdir(dir_from)
        files.sort()

        with open('Музыка.txt', 'w', encoding='utf-8') as file:
            for track in files:
                file.write(track + '\n')
                if show_log:
                    print(track)
                
    except Exception as e:
        print(e)
        time.sleep(10)

if __name__ == '__main__':
    get_all_music(True)
