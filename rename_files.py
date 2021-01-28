import os
import shutil
import time

dir_music = 'Все песни'
dir_tmp = 'tmp'

search_str = 'UNREAL'
replace_str = 'Unreal'

def rename_files(show_log = False):
    try:
        os.makedirs(dir_tmp)
        
        files = [file for file in os.listdir(dir_music) if file.find(search_str) >= 0]
        for file in files:
            new_file = file.replace(search_str, replace_str)
            shutil.copy(f'{dir_music}\{file}', f'{dir_tmp}\{new_file}')
            os.remove(f'{dir_music}\{file}')
            shutil.copy(f'{dir_tmp}\{new_file}', f'{dir_music}\{new_file}')
            if show_log:
                print(f'{file} => {new_file}')
                
        shutil.rmtree(dir_tmp)
    except Exception as e:
        print(e)
        time.sleep(10)

if __name__ == '__main__':     
    rename_files(True)
