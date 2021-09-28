from colour import Color
from GradientGen.utils import linear_gradient


class PrintGradient(object):
    def __init__(self, start: str, end: str, message: str) -> None:
        self.message = message
        gradient = self.generate_gradient(start, end)
        print(gradient)

    def generate_gradient(self, start: str, end: str) -> str:
        gradient = ""
        start = Color(start)
        colors = list(start.range_to(Color(end), count_real_characters(self.message)))

        for m in list(self.message):
            if m == "\n":
                gradient += "\n"
            elif m == "\r":
                gradient += "\r"
            elif m == " ":
                gradient += " "
            else:
                c = colors[0]
                r = int(c.rgb[0] * 256)
                g = int(c.rgb[1] * 256)
                b = int(c.rgb[2] * 256)
                gradient += f"\033[38;2;{r};{g};{b}m{m}"
                colors.remove(c)

        return gradient


class PrintLinearGradient(object):
    def __init__(self, start: str, end: str, message: str) -> None:
        self.message = message
        gradient = self.generate_gradient(start, end)
        print(gradient)

    def generate_gradient(self, start: str, end: str) -> str:
        gradient = ""
        colors = linear_gradient(start, end, count_real_characters(self.message))
        c = 0

        for m in list(self.message):
            if m == "\n":
                gradient += "\n"
            elif m == "\r":
                gradient += "\r"
            elif m == " ":
                gradient += " "
            else:
                r = int(colors["r"][c])
                g = int(colors["g"][c])
                b = int(colors["b"][c])
                gradient += f"\033[38;2;{r};{g};{b}m{m}"
                c += 1

        return gradient


def count_real_characters(message: str) -> int:
    count = 0

    split = list(message)

    for c in split:
        if c != " " and c != "\n" and c != "\r":
            count += 1

    return count
