from controllers.drawing import Drawing
from db import photography

class Photography(Drawing):
    NAME = "photography"
    DB = photography.Photography()
    