# This Python file uses the following encoding: utf-8
# Create metadata from song file name
import os
import eyed3

myPath = './'
songlist = os.listdir(myPath)

def name():
    '''Clean filenames of all mp3 files in current working directory to be
    somewhat uniform.
    '''
    songlistCopy = songlist[:]
    songlistNew = []

    for song in range(0, len(songlist)):
        songlistNew.append('')
        counter = 0
        spacing = ' '

        if songlist[song].find('.mp3') == -1:  # only change .mp3 files
            continue
        if (songlistCopy[song].count('-') != 0 and
            songlistCopy[song].count(' - ') == 0):
            # make sure artist and song name are separated by whitespaced dash
            songlistCopy[song] = songlistCopy[song].replace('-', ' - ')

        # replace dumb characters
        if songlistCopy[song].find('_') != -1:
            songlistCopy[song] = songlistCopy[song].replace('_', ' ')
        if songlistCopy[song].find('—') != -1:
            songlistCopy[song] = songlistCopy[song].replace('—', '-')

        for word in songlistCopy[song].split():
            counter += 1
            # remove "lyrics" from the name
            if 'lyrics' in word.lower() and '.mp3' in word:
                songlistNew[song] = songlistNew[song].strip() + '.mp3'
                continue
            elif 'lyrics' in word.lower():
                continue
            # dumb way not to place space in the end of the name
            if counter == len(songlistCopy[song].split()):
                spacing = ''
            # capitalize lowercase words
            if word == word.lower():
                songlistNew[song] += word.capitalize() + spacing
            else:
                songlistNew[song] += word + spacing

        os.rename(myPath + songlist[song], myPath + songlistNew[song].strip())

        if songlist[song] != songlistNew[song]:
            print('Was: ' + songlist[song] + '\n' + 'Now: ' +
                  songlistNew[song].strip() + '\n')
    return

def meta():
    '''Create metadata for artist and song name if none present for all mp3
     files in current working directory.
    '''
    for song in range(0, len(songlist)):
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
            # change metadata of the song if none present
            if eyed3.load(songlist[song]).tag.title is None:
                # file.tag.title = songTitle[0:(len(songTitle) - 4)]
                file.tag.title = songTitle[0:-4]
                file.tag.save()
            if eyed3.load(songlist[song]).tag.artist is None:
                file.tag.artist = songArtist
                file.tag.save()
            print songlist[song]
        except NotImplementedError:
            file.initTag()
            # file.tag.title = u'%s' % songTitle[0:(len(songTitle) - 4)]
            file.tag.title = u'%s' % songTitle[0:-4]
            file.tag.artist = u'%s' % songArtist
            file.tag.save()
            print songlist[song]
        return

def meta_to_name():
    '''Change filenames of all mp3 files in current working directory
    according to their metadata.
    '''
    songlistNew = []
    for song in range(0, len(songlist)):
        songlistNew.append('')
        if songlist[song].find('.mp3') == -1:  # only change .mp3 files
            continue
        file = eyed3.load(songlist[song])

        # check if tag is present
        try:
            songArtist = file.tag.artist
            songTitle = file.tag.title
        except:
            continue

        # try to create a new filename
        if file.tag.artist is not None and file.tag.title is not None:
            songName = str(songArtist.encode('utf-8') + ' - ' +
                           songTitle.encode('utf-8') + '.mp3')
            songlistNew[song] = songName
        else:
            continue

        if '/' in songlistNew[song]:
            songlistNew[song] = songlistNew[song].replace('/', ' ')

        # make changes and print them out
        if songlist[song] != songlistNew[song]:
            print('Was: ' + songlist[song] + '\n' + 'Now: ' +
                  songlistNew[song].strip() + '\n')
            os.rename(myPath + songlist[song], myPath + songlistNew[song])
        return
# meta()
# meta_to_name()
# name()
print 'Oi matey!'
print('Type "n" to clean names, "m" to create metadata or "mn" to rename' +
    ' accordingly to metadata')
print('Separate arguments with spaces to run multiple operations at once')
task = raw_input('Type what to do here:\n')
for word in task.split():
    if word.lower() == 'n':
        name()
    elif word.lower() == 'm':
        meta()
    elif word.lower() == 'mn':
        meta_to_name()