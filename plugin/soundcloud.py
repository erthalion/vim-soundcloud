#!/usr/bin/python
# -*- coding: utf-8 -*-

from sound_thread import SoundThread
import __builtin__ as builtin

def play(script_path):
    if not hasattr(builtin, "thread"):
        thread = SoundThread(script_path)

        # FIXME: Ugly hack?
        builtin.thread = thread

    builtin.thread.play()

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

def set_genres(*args):
    if hasattr(builtin, "thread"):
        builtin.thread.set_genres(*args)
    else:
        print "There are no tracks"

if __name__ == '__main__':
    play("play.sh")
    import time
    time.sleep(10)
    builtin.thread.stop()
