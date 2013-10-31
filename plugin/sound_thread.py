#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import shlex
import threading

class SoundThread():
    def __init__(self, sound_client):
        self.thread = None
        self.process = None
        self.client = sound_client
        self.play_next_track = True

    def thread_function(self, callback, track):
        popen_args = shlex.split("/bin/sh play.sh {track}".format(track=track))
        self.process = subprocess.Popen(popen_args, preexec_fn=os.setsid)
        self.process.wait()

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
