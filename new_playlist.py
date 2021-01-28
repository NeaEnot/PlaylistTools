import os
import time

from get_all_music import get_all_music
from form_playlist import form_playlist
from copy_files import copy_files

def clear_playlist_files():
    dir_playlist = 'Плейлист' # ВНИМАНИЕ
    files = os.listdir(dir_playlist)
    for file in files:
        os.remove(f'{dir_playlist}\{file}')

def new_playlist():
    try:
        clear_playlist_files()
        
        print('=========== ФОРМИРУЕМ ПЛЕЙЛИСТ ==========')
        form_playlist(count_files = 50)
        print('============= КОПИРУЕМ ФАЙЛЫ ============')
        copy_files(True)
        print('=========================================')
    except Exception as e:
        print(e)
        time.sleep(10)

if __name__ == '__main__':      
    new_playlist()
