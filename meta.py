# Create metadata from song file name
import os
import eyed3

myPath = './'
songlist = os.listdir(myPath)
songlistNew = []

for song in range(0, len(songlist)):
    songlistNew.append('')
    counter = 0
    spacing = ' '
    songArtist = ''
    songTitle = ''
    if songlist[song].find('.mp3') == -1:  # only change .mp3 files
        continue

    if songlist[song].find(' - ') != -1:
        songArtist = songlist[song].split(' - ')[0].decode('utf-8', 'replace')
        songTitle = songlist[song].split(' - ')[1].decode('utf-8', 'replace')
    else:
        continue

    file = eyed3.load(songlist[song])
    if eyed3.load(songlist[song]).tag is None:
        file.initTag()
        file.tag.save()

    # tags are weird, this seem to work
    try:
        print songlist[song], songArtist
        if eyed3.load(songlist[song]).tag.title is None:
            # changing metadata of the song if none present
            file.tag.title = songTitle[0:(len(songTitle) - 4)]
            file.tag.save()
        if eyed3.load(songlist[song]).tag.artist is None:
            file.tag.artist = songArtist
            file.tag.save()
    except NotImplementedError:
        file.initTag()
        file.tag.title = u'%s' % songTitle[0:(len(songTitle) - 4)]
        file.tag.artist = u'%s' % songArtist
        file.tag.save()

    if eyed3.load(songlist[song]).tag.title is None:
        # changing metadata of the song if none present
        file.tag.title = u'%s' % songTitle[0:(len(songTitle) - 4)]
        file.tag.save()
    if eyed3.load(songlist[song]).tag.artist is None:
        file.tag.artist = u'%s' % songArtist
        file.tag.save()

    # if songlist[song] != songlistNew[song]:     print('Was: ' +
    # songlist[song] + '\n' + 'Now: ' + songlistNew[       4 song].strip() +
    # '\n')
