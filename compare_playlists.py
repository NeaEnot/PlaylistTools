import time

list_old = []
list_new = []

def compare_playlists():
    try:
        with open('Музыка old.txt', 'r', encoding='utf-8') as playlist:
            for track in playlist:
                track = track.replace('\n', '')
                list_old.append(track)
        list_old.sort()
        
        with open('Музыка.txt', 'r', encoding='utf-8') as playlist:
            for track in playlist:
                track = track.replace('\n', '')
                list_new.append(track)
        list_new.sort()
        
        new_files = list(set(list_new) - set(list_old))
        new_files.sort()
        deleted_files = list(set(list_old) - set(list_new))
        deleted_files.sort()
        
        with open('changes.txt', 'w') as file:
            for track in deleted_files:
                file.write('-' + track + '\n')
            for track in new_files:
                file.write('+' + track + '\n')
    except Exception as e:
        print(e)
        time.sleep(10)

if __name__ == '__main__':    
    compare_playlists()
