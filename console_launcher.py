# coding: utf-8

from timer import Timer
from downloader import Downloader
from status import Status

class ConsoleLauncher:

    def __init__(self, link, downloader):
        self.__link = link
        self.__downloader = downloader

    def launch(self):
        print("Downloading...")

        download_result = self.__downloader.download(self.__link)
        
        status = download_result.status
        exception_message = download_result.exception_message
        time_duration = download_result.time_duration

        print("Completed with status", status.name)

        if status == Status.ERROR:
            print(exception_message)

        print("Execution time", time_duration, "sec")
