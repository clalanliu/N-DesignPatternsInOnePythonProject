import logging
from abc import ABC, abstractmethod
import sys
import hashlib

import numpy as np


logger = logging.getLogger(__name__)


# Painting.py
class Painting:
    def __init__(self, title, artist, style, medium):
        self.title = title
        self.artist = artist
        self.style = style
        self.medium = medium

        s = f"Title: {self.title}, Artist: {self.artist}, Style: {self.style}, Medium: {self.medium}"
        np.random.seed(int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10**8))
        self.content = np.random.rand(100, 100)

    def display(self):
        logger.info(f"ID {id(self)}")
        logger.info(
            f"Title: {self.title}, Artist: {self.artist}, Style: {self.style}, Medium: {self.medium}, Content Size {sys.getsizeof(self.content)}"
        )
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
