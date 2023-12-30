# coding: utf-8

class DownloadResult:
    def __init__(self, status, exception_message, time_duration):
        self.status = status
        self.exception_message = exception_message
        self.time_duration = time_duration
