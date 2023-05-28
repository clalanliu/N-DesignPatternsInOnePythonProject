import logging
from dataclasses import dataclass
import hashlib

import numpy as np


logger = logging.getLogger(__name__)


# Painting.py
@dataclass
class Painting:
    title: str
    artist: str
    style: str
    medium: str

    def __post_init__(self):
        s = f"Title: {self.title}, Artist: {self.artist}, Style: {self.style}, Medium: {self.medium}"
        np.random.seed(int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10**8))
        self.content = np.random.rand(100, 100)

    def display(self):
        logger.info(f"ID {id(self)}")
        logger.info(self.__repr__())
        logger.info(f"Painting Content (first 3 elements) {self.content[0,:3]}")


# PaintingFactory.py
class PaintingFactory:
    def __init__(self):
        self.paintings = {}

    def get_painting(self, title, artist, style, medium):
        key = f"{title}_{artist}_{style}_{medium}"
        if key not in self.paintings:
            self.paintings[key] = Painting(title, artist, style, medium)
        return self.paintings[key]
