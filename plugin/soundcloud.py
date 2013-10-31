#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import SoundcloudClient
from sound_thread import SoundThread
import time

def play():
    sound_client = SoundcloudClient()
    sound_client.upload_random_track_portion()
    thread = SoundThread(sound_client)
    thread.play()
    time.sleep(10)
    thread.next()
    time.sleep(10)
    thread.stop()

if __name__ == '__main__':
    play()
