from typing import List, NamedTuple, Text


class Video(NamedTuple):
    name: Text
    width: int
    height: int
    frames: int
    frame_rate: List[int]
    url: Text
    first_frame: Text
    last_frame: Text
