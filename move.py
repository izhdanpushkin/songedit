# Walk every subdirectory in start dir, move every '.mp3' to destination dir
import os
import shutil

moveTo = '/home/azuny/Desktop/123/'
moveFrom = '/home/azuny/Desktop/test/Music'
for root, dirs, files in os.walk(moveFrom):
    for file in files:
        print(file)
        if root + '/' + file == moveTo + file:
            continue
        if file.find('.mp3') != -1:
            shutil.copyfile(root + '/' + file, moveTo + file)
