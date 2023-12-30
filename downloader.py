# coding: utf-8

from pytube import YouTube

from status import Status
from download_result import DownloadResult
from timer import Timer

class Downloader:

    def download(self, link):
        timer = Timer()
        timer.start()
        status = Status.OK
        exception_message = ""

        try:
            youtube = YouTube(link)
            streams = youtube.streams
            highest_resolution_stream = streams.get_highest_resolution()
            highest_resolution_stream.download()
        except Exception as exception:
            exception_message = exception
            status = Status.ERROR

        timer.end()
        time_duration = timer.get_duration()
        result = DownloadResult(status, exception_message, time_duration)
        return result
