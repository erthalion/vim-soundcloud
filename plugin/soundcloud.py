#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import SoundcloudClient
from sound_thread import SoundThread
import __builtin__

def play(script_path):
    sound_client = SoundcloudClient()
    thread = SoundThread(sound_client, script_path)
    sound_client.upload_random_track_portion()
    thread.play()

    # FIXME: Ugly hack?
    __builtin__.thread = thread

def next():
    __builtin__.thread.next()

def stop():
    __builtin__.thread.stop()

if __name__ == '__main__':
    play("play.sh")
    import time
    time.sleep(10)
    __builtin__.thread.stop()
