# This Python file uses the following encoding: utf-8
# Create metadata from song file name
import os
import eyed3

myPath = './'
songlist = os.listdir(myPath)
songlistNew = []

def meta():
    '''Create metadata for artist and song name if none present.'''
    for song in range(0, len(songlist)):
        songlistNew.append('')
        songArtist = ''
        songTitle = ''
        if songlist[song].find('.mp3') == -1:  # only change .mp3 files
            continue

        # check if possible to extract name and artist
        if songlist[song].find(' - ') != -1:
            songArtist = songlist[song].split(' - ')[0].decode(
                'utf-8', 'replace')
            songTitle = songlist[song].split(' - ')[1].decode(
                'utf-8', 'replace')
        else:
            continue

        file = eyed3.load(songlist[song])
        if eyed3.load(songlist[song]).tag is None:
            file.initTag()
            file.tag.save()

        # tags are weird, this seems to work
        try:
            # changing metadata of the song if none present
            if eyed3.load(songlist[song]).tag.title is None:
                file.tag.title = songTitle[0:(len(songTitle) - 4)]
                file.tag.save()
            if eyed3.load(songlist[song]).tag.artist is None:
                file.tag.artist = songArtist
                file.tag.save()
            print songlist[song]
        except NotImplementedError:
            file.initTag()
            file.tag.title = u'%s' % songTitle[0:(len(songTitle) - 4)]
            file.tag.artist = u'%s' % songArtist
            file.tag.save()
            print songlist[song]
        return
meta()