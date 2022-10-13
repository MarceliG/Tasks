# - program rysujący kształty do pliku png
#   biblioteka do smarowania: PIL
#   plik wynikowy png, o tej samej nazwie co wejściowy plik txt
#   polecenia:
#     - canvas [W] [H]
#     - triangle [color] [point A], [point B], [point C]
#         - point -> (x, y)
#     - rectangle [color] [point] [size]
#         - size -> (w, h)
#   przykładowy plik wejściowy plik.txt:
#     canvas 256 256
#     triangle red (10, 10), (110, 10), (60, 100)
#     rectangle blue (100, 100), (100, 100)

#   uruchomienie:
#     $ ./maluj plik.txt
