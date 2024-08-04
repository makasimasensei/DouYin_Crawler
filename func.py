import datetime
import re
import os
import requests

headers = {
    'User-Agent':
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"}


def getUrl(string: str):
    result = re.search(r'http(.*?)\ ', string)
    return result.group(0)


def getVideoID(url: str):
    response = requests.get(url, headers=headers, timeout=3)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        result = re.search(r"video_id=(.*?)\"", text)

        """防止请求响应出错
        如果出错，重新运行"""
        if text is not None and result is None:
            return getVideoID(url)
        else:
            return result.group(0)[:-1]


def is_directory_present(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def videoDownload(url: str, p):
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:

        total_size = int(response.headers.get('content-length', 0))
        datetime_str = str(datetime.datetime.now())
        datetimePureFigure = re.sub(r'\D', '', datetime_str)

        is_directory_present('./video')

        with open('./video/video_{}.mp4'.format(datetimePureFigure), 'wb') as f:
            p.setRange(0, 100)
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
                download_size = os.path.getsize('./video/video_{}.mp4'.format(datetimePureFigure))
                if download_size < total_size:
                    progress_percent = (download_size / total_size) * 100
                    rounded_progress_percent = round(progress_percent, 2)
                    p.setValue(rounded_progress_percent)
        p.setValue(100)
