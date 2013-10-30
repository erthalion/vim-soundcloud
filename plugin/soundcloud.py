#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from client import SoundcloudClient

def play():
    client = SoundcloudClient()
    client.upload_tracks()
    for track in client.get_track():
        os.system("wget --quiet {} -O - | mplayer2 - > /dev/null".format(track))


if __name__ == '__main__':
    play()
