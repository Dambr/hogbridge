# coding: utf-8

import threading

from downloader import Downloader

class GuiLauncher:

    def __init__(self, downloader):
        self.__downloader = downloader
        self.presenter = None

    def launch(self):
        self.presenter.show_gui()

    def start_downloading(self, link, end_downloading_callback):
        download_procedure = DownloadProcedure(self.__downloader, link, end_downloading_callback)
        thread = threading.Thread(target=download_procedure.run)
        thread.start()

class DownloadProcedure:
    def __init__(self, downloader, link, end_downloading_callback):
        self.__downloader = downloader
        self.__link = link
        self.__end_downloading_callback = end_downloading_callback

    def run(self):
        download_result = self.__downloader.download(self.__link)
        self.__end_downloading_callback(download_result)
