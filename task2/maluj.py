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


def main():
    draw = Read()
    draw.read_file()


if __name__ == "__main__":
    main()
