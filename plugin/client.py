#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, urllib
import random
import simplejson

TIMEOUT = 20

class SoundcloudClient():
    def __init__(self, random=True):
        self.genres = ["metall", "post rock",]
        self.genres = [g.replace(" ", "+") for g in self.genres]

        self.soundcloud_url = "https://api.soundcloud.com/tracks.json"
        self.client_id = "8c2772150284a782b5009d77535dd1e5"
        self.max_offset = 1000

        self.url = "{soundcloud}?genres={genres}&client_id={client_id}".format(
                soundcloud=self.soundcloud_url,
                genres=",".join(self.genres),
                client_id=self.client_id,
                )

        self.random_tracks = random
        self.current_track_index = 0
        self.portion_size = 100
        self.portion_index = 0

    def set_genres(self, *args):
        self.genres = list(args)

    def get_info(self):
        """ Get dictionary, that contains info about current track:
                :title
                :genre
                :url
        """
        track = self.tracks[self.current_track_index]
        return {
                "title": track.get("title", "No title"),
                "genre": track.get("genre", "No genre"),
                "url": track.get("permalink_url", "No url"),
                }

    def upload_track_portion(self, offset=None, limit=None):
        """ Set first track as current
        """
        self.url = self.url.format(genres=self.genres)

        if offset is None:
            offset = self.portion_index * self.portion_size

        if limit is None:
            limit = self.portion_size

        self.url = "{url}&offset={offset}&limit={limit}".format(url=self.url, offset=offset, limit=limit)

        request = urllib2.Request(self.url, None, {'user-agent':'vim-soundcloud'})
        opener = urllib2.build_opener()
        json_stream = opener.open(request, timeout=TIMEOUT)

        """ #TODO: Restore tracks after error
        """
        self.tracks = simplejson.load(json_stream)
        self.current_track_index = 0

    def upload_random_track_portion(self):
        offset = random.randint(0, self.max_offset)
        self.upload_track_portion(offset=offset)

    def get_track(self):

        def get_stream(self):
            stream = self.tracks[self.current_track_index].get("stream_url", None)
            if stream:
                stream = "{stream}?client_id={client_id}".format(stream=stream, client_id=self.client_id)

            return stream

        if self.random_tracks is True:
            self.current_track_index = random.randint(0, len(self.tracks))
            stream = get_stream(self)

        else:
            stream = get_stream(self)
            self.current_track_index += 1

        return stream


if __name__ == '__main__':
    client = SoundcloudClient()
    client.upload_track_portion()
    print client.get_track()
