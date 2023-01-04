import requests
from urllib.parse import urljoin, quote

from backend.models.video import Video
from settings import API_BASE, VIDEO_NAME


class FrameX:

    @staticmethod
    def get_video(video: str = VIDEO_NAME) -> Video:
        rq = requests.get(urljoin(API_BASE, f"video/{quote(video)}/")).json()
        return Video(**rq)

    @staticmethod
    def get_video_frame(video: str = VIDEO_NAME, frame: int = 0):
        rq = requests.get(urljoin(API_BASE, f"video/{quote(video)}/frame/{frame}/"))
        return rq.content
