#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "d", "l", "p"}
    b = {"b", "d", "e", "l", "p", "x"}
    c = {"k", "l", "p", "t"}
    d = {"d", "k", "o", "p", "q", "u", "v"}

    x = (a.difference(b)).union(c.intersection(d))
    print(f"x = {x}")

    da = u.difference(a)
    db = u.difference(b)
    y = (da.intersection(db)).difference(c.union(d))
    print(f"y = {y}")