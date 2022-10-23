from PIL import Image, ImageDraw
from abc import ABC, abstractmethod


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


class Draw(ABC):
    """Abstract class"""

    @abstractmethod
    def draw(self):
        """Figure must be able to draw."""
        pass


class Triangle(Draw):
    """Create triangle with 3 point and color.

    Args:
        point_A (tuple(int)): Cartesian point(x,y)
        point_B (tuple(int)): Cartesian point(x,y)
        point_C (tuple(int)): Cartesian point(x,y)
        color (str): fille color
    """

    def __init__(
        self,
        canvas: Canvas,
        color: str,
        point_a: tuple,
        point_b: tuple,
        point_c: tuple,
    ):
        self.canvas: Canvas = canvas
        self.color: str = color
        self.point_a: tuple = point_a
        self.point_b: tuple = point_b
        self.point_c: tuple = point_c

    def draw(self):
        """Draw triangle."""
        self.canvas.draw.polygon(
            xy=[self.point_a, self.point_b, self.point_c],
            fill=self.color,
        )


class Rectangle(Draw):
    """Create rectangle with 1 point, size and color.

    Args:
        start_point (tuple(int)): Cartesian point(x,y)
        size (tuple(int)): width x height
        color (str): color
    """

    def __init__(
        self,
        canvas: Canvas,
        color: str,
        start_point: tuple,
        size: tuple,
    ):
        self.canvas: Canvas = canvas
        self.color: str = color
        self.start_point: tuple = start_point
        self.size: tuple = size

    def draw(self):
        """Draw rectangle."""
        self.canvas.draw.rectangle(
            xy=[self.start_point, self.size],
            fill=self.color,
        )


def main():
    """Core Script."""
    file = Read("plik.txt")

    width_canvas = int(file.properties_to_draw["canvas"][0])
    height_canvas = int(file.properties_to_draw["canvas"][1])

    # Triangle
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

    # Rectangle
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

    # Create objects
    canvas = Canvas(width=width_canvas, height=height_canvas)

    triangle = Triangle(
        canvas=canvas,
        color=triangle_color,
        point_a=triangle_point_A,
        point_b=triangle_point_B,
        point_c=triangle_point_C,
    )

    rectangle = Rectangle(
        canvas=canvas,
        color=rectangle_color,
        start_point=rectangle_start_point,
        size=rectangle_size,
    )

    # Drawing objects
    triangle.draw()
    rectangle.draw()

    # Save image
    canvas.image.save("image.png")


if __name__ == "__main__":
    main()
