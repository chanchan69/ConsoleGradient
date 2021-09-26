from colour import Color
import GradientGen.TermGradient


class PrintGradient(object):
    def __init__(self, start: str, end: str, message: str) -> None:
        self.message = message
        gradient = self.generate_gradient(start, end)
        self.print(gradient)

    def generate_gradient(self, start: str, end: str) -> str:
        gradient = ""

        start = Color(start)
        colors = list(start.range_to(Color(end), len(self.message.split("\n"))))

        for c in colors:
            gradient += f"{int(c.rgb[0] * 256)}:{int(c.rgb[1] * 256)}:{int(c.rgb[2] * 256)}\n"

        return gradient

    def print(self, gradient: str) -> None:
        TermGradient.print_gradient(gradient, self.message)
