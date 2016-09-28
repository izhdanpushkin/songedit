# Rename songs from their metadata
import os, eyed3
myPath       = './'
songlist     = os.listdir(myPath)
songlistCopy = songlist[:]
songlistNew  = []

for song in range(0, len(songlist)):
    songlistNew.append('')
    counter    = 0
    spacing    = ' '
    songArtist = ''
    songTitle  = ''
    if songlist[song].find('.mp3') == -1: # only change .mp3 files
        continue

    file = eyed3.load(songlist[song])

    songArtist = file.tag.artist
    songTitle  = file.tag.title

    if not file.tag is None and not file.tag.artist is None and not file.tag.title is None:
        songName          = str(songArtist.encode('utf-8') + ' - ' + songTitle.encode('utf-8') + '.mp3')
        songlistNew[song] = songName
    else:
        songName = songlist[song]
        songlistNew[song] = songName

    for char in songName:
        if char == '/':
            songName = songName.replace('/', ' ')

    if songlist[song] != songlistNew[song]:
        print('Was: ' + songlist[song] + '\n' + 'Now: ' + songlistNew[song].strip() + '\n')
    # print songlist[song]
    os.rename(myPath + songlist[song], myPath + songName)