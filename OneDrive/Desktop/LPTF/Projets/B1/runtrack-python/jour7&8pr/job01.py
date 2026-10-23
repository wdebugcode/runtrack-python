def draw_rectangle(width, height):

    haut_bas = "|" + "-" * (width - 2) + "|"

    milieu = "|" + " " * (width - 2) + "|"

    print(haut_bas)

    for _ in range(height - 2):
        print(milieu)

    print(haut_bas)

draw_rectangle(10, 3)