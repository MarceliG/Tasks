from PIL import Image, ImageDraw


class Read:
    def __init__(self):
        """canvas [W] [H]
        triangle [color] [point A], [point B], [point C]
        point -> (x, y)
        rectangle [color] [point] [size]
        size -> (w, h)
        """
        self.properties_to_draw = {
            "canvas": [],
            "triangle": [],
            "rectangle": [],
        }

    def _give_pure_line(self, line: str):
        return [x.strip(" (),") for x in line.split()[1:]]

    def read_file(self, file_name):
        with open(file_name) as f:
            for line in f.readlines():
                if "canvas" in line:
                    self.properties_to_draw["canvas"] = self._give_pure_line(
                        line
                    )
                elif "triangle" in line:
                    self.properties_to_draw["triangle"] = self._give_pure_line(
                        line
                    )
                elif "rectangle" in line:
                    self.properties_to_draw[
                        "rectangle"
                    ] = self._give_pure_line(line)


class Draw:
    def __init__(self, width, height):
        self.im = Image.new("RGB", (width, height))
        self.draw = ImageDraw.Draw(self.im)

    def create_canvas(self):
        pass

    def create_triangle(
        self,
        point_A: tuple,
        point_B: tuple,
        point_C: tuple,
        color: str,
    ):
        self.draw.polygon(xy=[point_A, point_B, point_C], fill=color)

    def create_rectangle(self, start_point: tuple, size: tuple, color: str):
        self.draw.rectangle(xy=[start_point, size], fill=color)


def main():
    file = Read()
    file.read_file("plik.txt")

    width = int(file.properties_to_draw["canvas"][0])
    height = int(file.properties_to_draw["canvas"][1])

    im = Draw(width, height)  # draw canvas

    triangle_point_A = (
        int(file.properties_to_draw["triangle"][1]),
        int(file.properties_to_draw["triangle"][2]),
    )
    triangle_point_B = (
        int(file.properties_to_draw["triangle"][3]),
        int(file.properties_to_draw["triangle"][4]),
    )

    triangle_point_C = (
        int(file.properties_to_draw["triangle"][5]),
        int(file.properties_to_draw["triangle"][6]),
    )
    triangle_color = file.properties_to_draw["triangle"][0]
    im.create_triangle(  # draw triangle
        triangle_point_A, triangle_point_B, triangle_point_C, triangle_color
    )

    rectangle_start_point = (
        int(file.properties_to_draw["rectangle"][1]),
        int(file.properties_to_draw["rectangle"][2]),
    )
    rectangle_size = (
        int(file.properties_to_draw["rectangle"][1])
        + int(file.properties_to_draw["rectangle"][3]),
        int(file.properties_to_draw["rectangle"][2])
        + int(file.properties_to_draw["rectangle"][4]),
    )
    rectangle_color = file.properties_to_draw["rectangle"][0]

    im.create_rectangle(rectangle_start_point, rectangle_size, rectangle_color)
    im.im.save("pillow_imagedraw.png")


if __name__ == "__main__":
    main()
