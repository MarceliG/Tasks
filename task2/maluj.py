#!/usr/bin/python3

import textwrap
from PIL import Image, ImageDraw
from abc import ABC, abstractmethod
import argparse


class Read:
    """Read some file."""

    def __init__(self, file: str):
        """canvas [W] [H]
        triangle [color] [point A], [point B], [point C]
        point -> (x, y)
        rectangle [color] [point] [size]
        size -> (w, h)
        """
        self.filename = file
        self.properties_to_draw = {
            "canvas": [],
            "triangle": [],
            "rectangle": [],
        }
        self.read_file(file)

    def __str__(self):
        return str(self.filename)

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


def draw_all_form_file(file):

    try:
        width_canvas = int(file.properties_to_draw["canvas"][0])
        height_canvas = int(file.properties_to_draw["canvas"][1])
    except:
        pass

    try:
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
    except:
        pass

    try:
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
    except:
        pass

    try:
        # Create object
        canvas = Canvas(width=width_canvas, height=height_canvas)
    except:
        pass

    try:
        # Create object
        triangle = Triangle(
            canvas=canvas,
            color=triangle_color,
            point_a=triangle_point_A,
            point_b=triangle_point_B,
            point_c=triangle_point_C,
        )
        # Drawing objects
        triangle.draw()
    except:
        pass

    try:
        # Create object
        rectangle = Rectangle(
            canvas=canvas,
            color=rectangle_color,
            start_point=rectangle_start_point,
            size=rectangle_size,
        )
        # Drawing objects
        rectangle.draw()
    except:
        pass

    try:
        # Save image
        canvas.image.save(str(file).split(".")[0] + ".png")
    except:
        pass


def main():
    """Core Script."""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """Draw triangle or rectangle.
            
        First of all prepare file.txt with sample text:
        --- file.txt ---
        canvas size
        triangle color (point_A), (point_B), (point_C)
        rectangle color (point_A), (size)
        ----------------
        Explanation:
        color : str = color_name
        point : tuple = (x, y)
        size : tuple = (width, height)
        """
        ),
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Enter the file.txt for drawing",
    )
    args = parser.parse_args()
    if args.file:
        if "txt" in args.file.split("."):
            read_file = Read(args.file)
            draw_all_form_file(read_file)
        else:
            print("Your file does not have a '.txt' extension.")
    return 0


if __name__ == "__main__":
    main()
