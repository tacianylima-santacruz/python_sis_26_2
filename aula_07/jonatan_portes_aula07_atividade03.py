def total_distance(*segments):
    total = 0
    for length, unit in segments:
        if unit.lower() == "M":
            total += length
        elif unit == "km":
            total += length / 1000

    print("Total distance:", total, "meters")

total_distance(
    (2.5, "km"),
    (400, "M"),
    (1.0, "km"),
    (800, "m"),
    (1.3, "KM"),
    (900, "m "),
    (1.1, "km")
)

"""Existem 2 problemas no código, o primeiro é que o if unit.lower() == "M" vai ser False para algumas distancias, pois o .lower() converte tudo para minusculo (M -> m) e m = M e False. A segunda é que em (900, "m ") exsite um espacço, esse espaço faz com que "m " != "m". Para ajustar, adicionei um .strip() antes do for para remover espaços e alterei M para m."""

def total_distance(*segments):
    total = 0
    for length, unit in segments:
        unit = unit.lower().strip()

        if unit == "m":
            total += length
        elif unit == "km":
            total += length / 1000

    print("Total distance:", total, "meters")

total_distance(
    (2.5, "km"),
    (400, "M"),
    (1.0, "km"),
    (800, "m"),
    (1.3, "KM"),
    (900, "m "),
    (1.1, "km")
)