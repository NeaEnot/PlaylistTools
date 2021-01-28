import os
import shutil
import time

dir_from = 'Все песни'
dir_to = 'Плейлист'

def copy_files(show_log = False):
    try:
        with open('playlist.txt', 'r', encoding='utf-8') as playlist:
            for track in playlist:
                track = track.replace('\n', '')
                shutil.copy(f'{dir_from}\{track}', f'{dir_to}\{track}')
                if show_log:
                    print(track)
    except Exception as e:
        print(e)
        time.sleep(10)

if __name__ == '__main__':     
    copy_files(True)
