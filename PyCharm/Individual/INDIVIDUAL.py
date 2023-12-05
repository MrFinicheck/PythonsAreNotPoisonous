#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество.
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "d", "f", "g", "l", "u"}
    b = {"d", "e", "f", "m", "n", "z"}
    c = {"h", "i", "r", "x", "y"}
    d = {"a", "e", "f", "k", "r", "s", "x"}

    x = (a.difference(b)).intersection(c.union(d))
    print(f"x = {x}")

    # Найдём дополнения множеств.
    an = u.difference(a)

    y = (an.intersection(d)).union(c.difference(b))
    print(f"y = {y}")

