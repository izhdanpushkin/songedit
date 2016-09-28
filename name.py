# This Python file uses the following encoding: utf-8
# Change .mp3 names into more readable ones
import os, eyed3
myPath       = './'
songlist     = os.listdir(myPath)
songlistCopy = songlist[:]
songlistNew  = []

for song in range(0, len(songlist)):
    songlistNew.append('')
    counter = 0
    spacing = ' '

    if songlist[song].find('.mp3') == -1: # only change .mp3 files
        continue
    if songlistCopy[song].count('-') != 0 and songlistCopy[song].count(' - ') == 0:
        # make sure artist and song name are divided by whitespaced dash
        songlistCopy[song] = songlistCopy[song].replace('-', ' - ')

    # replace dumb characters
    if songlistCopy[song].find('_') != -1:
        songlistCopy[song] = songlistCopy[song].replace('_', ' ')
    if songlistCopy[song].find('—') != -1:
        songlistCopy[song] = songlistCopy[song].replace('—', '-')


    for word in songlistCopy[song].split():
        counter += 1
        # remove "lyrics" from the name
        if word.lower().find('lyrics') != -1 and word.find('.mp3') != -1:
            songlistNew[song] = songlistNew[song].strip() + '.mp3'
            continue
        elif word.lower().find('lyrics') != -1:
            continue
        if counter == len(songlistCopy[song].split()):
            # dumb way not to place space in the end of the name
            spacing = ''
        # capitalize lowercase words
        if len(word) != 0 and word.capitalize() == word.replace(word[0], word[0].upper(), 1):
            songlistNew[song] += word.capitalize() + spacing
        else:
            songlistNew[song] += word + spacing

    os.rename(myPath + songlist[song], myPath + songlistNew[song].strip())

    if songlist[song] != songlistNew[song]:
        print('Was: ' + songlist[song] + '\n' + 'Now: ' + songlistNew[song].strip() + '\n')
