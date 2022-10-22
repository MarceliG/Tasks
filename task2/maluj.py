from PIL import Image, ImageDraw


class Read:
    """Read some file."""

    def __init__(self, file: str):
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
        self.read_file(file)

    def _give_pure_line(self, line: str):
        """Returns list withaut ' (),' from string.

        Args:
            line (str): Input string to clean from whitesigns

        Returns:
            (list): list with pure text.
        """
        return [x.strip(" (),") for x in line.split()[1:]]

    def read_file(self, file_name: str):
        """Read file, find line with 'canvas', 'triangle', 'rectangle'.

        Args:
            file_name (str): filename
        """
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


class Canvas:
    """Create canvas."""

    def __init__(self, width: int, height: int):
        """Prepare canvas with proper size.

        Args:
            width (int): width canvas
            height (int): height canvas
        """
        self.image = Image.new("RGB", (width, height))
        self.draw = ImageDraw.Draw(self.image)


class Triangle(Canvas):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.color: str = "red"
        self.point_a
        self.point_b
        self.point_c


class Rectangle(Canvas):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)


class Draw:
    """Draw some figures."""

    def __init__(self, width: int, height: int):
        """Create canvas

        Args:
            width (int): width canvas
            height (int): height canvas
        """
        self.im = Image.new("RGB", (width, height))
        self.draw = ImageDraw.Draw(self.im)

    def create_triangle(
        self,
        point_A: tuple,
        point_B: tuple,
        point_C: tuple,
        color: str = "red",
    ):
        """Create triangle with 3 point and color.

        Args:
            point_A (tuple(int)): Cartesian point(x,y)
            point_B (tuple(int)): Cartesian point(x,y)
            point_C (tuple(int)): Cartesian point(x,y)
            color (str): fille color
        """
        self.draw.polygon(xy=[point_A, point_B, point_C], fill=color)

    def create_rectangle(
        self, start_point: tuple, size: tuple, color: str = "red"
    ):
        """Create rectangle with 1 point, size and color.

        Args:
            start_point (tuple(int)): Cartesian point(x,y)
            size (tuple(int)): width x height
            color (str): color
        """
        self.draw.rectangle(xy=[start_point, size], fill=color)


def main():
    """Core Script."""
    file = Read("plik.txt")
    # file.read_file("plik.txt")

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

    im.create_rectangle(
        rectangle_start_point, rectangle_size, rectangle_color
    )  # draw rectangle

    im.im.save("pillow_imagedraw.png")  # save file to png


if __name__ == "__main__":
    main()
