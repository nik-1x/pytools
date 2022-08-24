from dataclasses import dataclass


@dataclass
class Style:
    section: str

    styles = {}

    def add(self, style, value):
        self.styles[style] = value
        return self

    def set(self, styles):
        self.styles = styles
        return self


class BuildStyle:

    def __init__(self, *args: Style):
        self.build = args

    def build(self):
        return "TODO"
