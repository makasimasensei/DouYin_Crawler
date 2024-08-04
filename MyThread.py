from PyQt5.QtCore import QThread
from func import *


class MyThread(QThread):
    def __init__(self, le, pb):
        super().__init__()
        self.le = le
        self.pb = pb

    def run(self):
            s = self.le.text()
            baseurl = getUrl(s)
            suffix = getVideoID(baseurl)
            newUrl = 'https://m.douyin.com/aweme/v1/playwm/?' + suffix
            videoDownload(newUrl, self.pb)

