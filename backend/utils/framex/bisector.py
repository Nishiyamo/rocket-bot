from backend.api.framex import FrameX
from backend.models.video import Video


class Bisector:

    def __init__(self, name):
        self.api = FrameX
        self.video: Video = self.api.get_video(video=name)
        self.index: int = 0
        self.total_frames: int = self.video.frames
        self.left_frame: int = 0
        self.right_frame: int = self.total_frames - 1
        self.calculed_frame: int = self.get_half_frames()
        self.image = self.api.get_video_frame(self.video.name, self.calculed_frame)

    @property
    def set_current_frame(self):
        return self.calculed_frame

    def get_half_frames(self):
        return round((self.right_frame - self.left_frame) / 2)

    def bisect(self, pass_mid: bool) -> None:
        midle = self.get_half_frames()
        if pass_mid:
            self.right_frame = midle
        else:
            self.left_frame = midle
