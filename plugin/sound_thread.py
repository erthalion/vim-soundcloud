#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import shlex
import threading
from client import SoundcloudClient

class SoundThread():
    def __init__(self, script_path):
        self.thread = None
        self.process = None
        self.client = SoundcloudClient()
        self.client.upload_random_track_portion()

        self.play_next_track = True
        self.script_path = script_path

    def thread_function(self, callback, track):
        popen_args = shlex.split("/bin/sh {script} {track}".format(script=self.script_path, track=track))
        self.process = subprocess.Popen(popen_args,
                preexec_fn=os.setsid,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        self.process.communicate()[0]

        if self.play_next_track:
            callback()

    def play(self):
        track = self.client.get_track()
        self.thread = threading.Thread(
                target=self.thread_function,
                args=(self.play, track)
                )
        self.thread.start()

    def next(self):
        os.killpg(self.process.pid, signal.SIGTERM)

    def stop(self):
        self.play_next_track = False
        os.killpg(self.process.pid, signal.SIGTERM)

    def get_info(self):
        return self.client.get_info()

    def is_playing(self):
        return self.thread.is_alive()

    def set_genres(self, *args):
        self.client.set_genres(*args)
        self.client.upload_random_track_portion()
