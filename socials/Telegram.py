from dataclasses import dataclass


@dataclass
class TextComponent:
    string: str

    changed = False
    original = ""

    def style(self, style):
        styles = {
            "bold": "**",
            "italic": "*",
            "mono": "`",
            "strike": "~~",
            "underline": "_"
        }
        self.changed = True
        self.original = self.string
        self.string = styles[style] + str(self.string) + styles[style]
        return self


class BuildComponent:

    def __init__(self, *args: [str or TextComponent]):
        result = ""
        for arg in args:
            if type(arg) == TextComponent:
                result += arg.string
            else:
                result += arg
        self.result = result

    def get(self):
        return self.result
