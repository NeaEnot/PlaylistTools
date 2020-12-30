import os
import random
import time

dir_from = 'Все песни'

def search(files):
    keys = [
        'Otto Dix',
        'DEFORM',
        'The Meto',
        'Елена Войнаровская'
    ]
    search = []
    
    for key in keys:
        for file in files:
            if file.find(key) >= 0:
                search.append(file)
            
    return search

try:
    files = os.listdir(dir_from)
    #files = search(files)    
    playlist = []
    
    for i in range(100):
        file = files[random.randint(0, len(files) - 1)]
        files.remove(file)
        playlist.append(file)
        
        print(file)
        
        if len(files) == 0:
            break

    playlist.sort()

    with open('playlist.txt', 'w') as file:
        for track in playlist:
            file.write(track + '\n')
            
except Exception as e:
    print(e)
    time.sleep(10)