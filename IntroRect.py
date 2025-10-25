import numpy as np
import latex
from MF_Tools import *
from manim.utils.color.BS381 import DARK_GREEN

config.background_color = WHITE

class IntroRect3(Scene):
    def construct(self):
        #Starting Scene: Set up rectangle for edits
        rectangle = Rectangle(height=9, width=16, color=BLACK).scale(0.7)
        self.play(Create(rectangle))
        self.wait(2)

        #Part 1: Binding Energy
        text = Text("Part 1: Binding Energy", color = BLACK).shift(UP * 2)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text, reverse=False, run_time=1), Uncreate(rectangle, run_time=1))
        self.wait(2)

#  python3 -m manim -pqh --fps 30 IntroRect.py Introrect3
