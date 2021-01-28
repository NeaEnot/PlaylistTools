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

def form_playlist(count_files = 100, show_log = False):
    try:
        files = os.listdir(dir_from)
        #files = search(files)    
        playlist = []
        
        for i in range(count_files):
            file = files[random.randint(0, len(files) - 1)]
            files.remove(file)
            playlist.append(file)
            
            if show_log:
                print(file)
            
            if len(files) == 0:
                break

        playlist.sort()

        with open('playlist.txt', 'w', encoding='utf-8') as file:
            for track in playlist:
                file.write(track + '\n')
                
    except Exception as e:
        print(e)
        time.sleep(10)

if __name__ == '__main__':    
    form_playlist(True)
