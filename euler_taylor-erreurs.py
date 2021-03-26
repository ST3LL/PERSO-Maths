import pandas as pd
from math import exp, cos, sin


def euler(h, list_t):
    l = [[0, 1, 1, 0]]
    w = 1
    for t in list_t:
        # y = ((t+0.1) ** 2) + (2 * exp(-3 * (t+0.1)))
        # w = w + (h * ((-3 * w) + (3 * (t ** 2)) + (2 * t)))
        y = exp(sin(t))
        w = w + h * w * cos(t)
        e = abs(w - y)
        l.append([t+0.5, y, w, e])
    return l


def taylor(h, list_t):
    l = [[0, 2, 2, 0]]
    w = 2
    for t in list_t:
        y = ((t+0.1) ** 2) + (2 * exp(-3 * (t+0.1)))
        w = w + (h * ((-3 * w) + (3 * (t ** 2)) + (2 * t)) + ((h ** 2) / 2) * ((9 * w) - (9 * (t ** 2)) + 2))
        e = abs(w - y)
        l.append([t + 0.5, y, w, e])
    return l


if __name__ == "__main__":
    pas = 0.5
    intervalle = [0.0, 0.5, 1]
    eul = euler(pas, intervalle)
    # tay = taylor(pas, intervalle)
    print("METHODE EULER")
    # print(pd.DataFrame(columns=['ti', 'y(ti)', 'wi', 'e = |wi - y(ti)|'], index=None, data=eul))
    print()
    print("METHODE TAYLOR")
    # print(pd.DataFrame(columns=['ti', 'y(ti)', 'wi', 'e = |wi - y(ti)|'], index=None, data=tay))
