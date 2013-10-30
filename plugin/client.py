#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, urllib
import simplejson

TIMEOUT = 20

class SoundcloudClient():
    """
    https://api.soundcloud.com/tracks.json?genres=metall,post+rock&client_id=8c2772150284a782b5009d77535dd1e5
    https://api.soundcloud.com/tracks/{track_id}/stream?client_id=8c2772150284a782b5009d77535dd1e5
    """
    def __init__(self):
        self.genres = ["metall", "post rock",]
        self.genres = [g.replace(" ", "+") for g in self.genres]

        self.soundcloud_url = "https://api.soundcloud.com/tracks.json"
        self.client_id = "8c2772150284a782b5009d77535dd1e5"

        self.url = "{soundcloud}?genres={genres}&client_id={client_id}".format(
                soundcloud=self.soundcloud_url,
                genres=",".join(self.genres),
                client_id=self.client_id,
                )

        self.current_track_index = 0

    def set_genres(self, genres):
        self.genres=genres

    def get_info(self):
        """ Get dictionary, that contains info about current track:
                :name
                :author
                :genre
                :description
                :tags
        """
        pass

    def upload_tracks(self):
        """ Set first track as current
        """
        self.url = self.url.format(genres=self.genres)

        request = urllib2.Request(self.url, None, {'user-agent':'vim-soundcloud'})
        opener = urllib2.build_opener()
        json_stream = opener.open(request, timeout=TIMEOUT)

        """ #TODO: Restore tracks after error
        """
        self.tracks = simplejson.load(json_stream)
        self.current_track_index = 0

    def get_track(self):

        stream = self.tracks[self.current_track_index].get("stream_url", None)
        if stream:
            stream = "{stream}?client_id={client_id}".format(stream=stream, client_id=self.client_id)

        self.current_track_index += 1
        yield stream


if __name__ == '__main__':
    client = SoundcloudClient()
    client.upload_tracks()
    print client.get_track()
