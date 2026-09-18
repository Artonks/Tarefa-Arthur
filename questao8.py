import sys

for linha in sys.stdin:
    N = int(linha)

    if N == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")