# credit to https://gist.github.com/RoboDonut for 99.99% of this code
# https://gist.github.com/RoboDonut/83ec5909621a6037f275799032e97563


def hex_to_rgb(hex_code: str) -> list:
    return [int(hex_code[i:i + 2], 16) for i in range(1, 6, 2)]


def rgb_to_hex(rgb: list) -> str:
    rgb = [int(x) for x in rgb]
    return "#" + "".join(["0{0:x}".format(v) if v < 16 else
                          "{0:x}".format(v) for v in rgb])


def color_dict(gradient: list):
    return {"hex": [rgb_to_hex(rgb) for rgb in gradient],
            "r": [rgb[0] for rgb in gradient],
            "g": [rgb[1] for rgb in gradient],
            "b": [rgb[2] for rgb in gradient]}


def linear_gradient(start_hex: str, finish_hex: str, n: int) -> dict:
    s = hex_to_rgb(start_hex)
    f = hex_to_rgb(finish_hex)
    rgb_list = [s]
    for t in range(1, n):
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j]))
            for j in range(3)
        ]
        rgb_list.append(curr_vector)

    return color_dict(rgb_list)
