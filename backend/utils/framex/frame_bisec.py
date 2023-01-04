from backend.api.framex import FrameX


class FrameBisector:

    def __init__(self, name):
        self.video = FrameX.get_video(video=name)
        self._index = 0
        self.image = None



