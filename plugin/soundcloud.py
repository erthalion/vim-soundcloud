#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import SoundcloudClient
from sound_thread import SoundThread
import __builtin__ as builtin

def play(script_path):
    if not hasattr(builtin, "thread"):
        sound_client = SoundcloudClient()
        thread = SoundThread(sound_client, script_path)
        sound_client.upload_random_track_portion()
    thread.play()

    # FIXME: Ugly hack?
    builtin.thread = thread

def next():
    if hasattr(builtin, "thread"):
        builtin.thread.next()
    else:
        print "There are no tracks"

def stop():
    if hasattr(builtin, "thread") and builtin.thread.is_playing():
        builtin.thread.stop()

def get_info():
    if hasattr(builtin, "thread"):
        info = builtin.thread.get_info()
        print "Title: {title}, Genre: {genre}, Url: {url}".format(
                title=info.get("title"),
                genre=info.get("genre"),
                url=info.get("url"),)
    else:
        print "There are no tracks"

def set_genres(genres):
    if hasattr(builtin, "thread"):
        builtin.thread.set_genres(genres)
    else:
        print "There are no tracks"

if __name__ == '__main__':
    play("play.sh")
    import time
    time.sleep(10)
    builtin.thread.stop()
