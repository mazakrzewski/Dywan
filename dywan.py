#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# dywan.py
#
#  program tworzy plik dywan.svg zawierajacy dywan sierpinskiego
#

import random


class Dywan:
    """opisujefraktal."""

    def __init__(self, punkt1, punkt2, punkt3, punkt4, stopien):
        """Tworzy fraktal."""
        self.p1 = punkt1
        self.p2 = punkt2
        self.p3 = punkt3
        self.p4 = punkt4
        self.stopien = stopien

    def __str__(self):
        """Tworzy polecenia.svg."""
        return (r'<polygon points="{},{} {},{} {},{} {},{}"'
                ' style="fill:rgb({}, {}, {});"/>').format(
                    self.p1[0], self.p1[1],
                    self.p2[0], self.p2[1],
                    self.p3[0], self.p3[1],
                    self.p4[0], self.p4[1],
                    random.randint(0, self.stopien * 20 + 100),
                    random.randint(0, self.stopien * 20 + 100),
                    random.randint(0, self.stopien * 20 + 100))

    def podziel(self):
        """dzieli_figure."""

        def punkt_podzialu(p1, p2):
            """obliczapunkty podzialu."""
            return [(2 * p1[0] + p2[0]) / 3,
                    (2 * p1[1] + p2[1]) / 3]

        q1 = punkt_podzialu(self.p1, self.p4)
        q2 = punkt_podzialu(self.p1, self.p3)
        q3 = punkt_podzialu(self.p1, self.p2)

        q4 = punkt_podzialu(self.p2, self.p1)
        q5 = punkt_podzialu(self.p2, self.p4)
        q6 = punkt_podzialu(self.p2, self.p3)

        q7 = punkt_podzialu(self.p3, self.p2)
        q8 = punkt_podzialu(self.p3, self.p1)
        q9 = punkt_podzialu(self.p3, self.p4)

        q10 = punkt_podzialu(self.p4, self.p3)
        q11 = punkt_podzialu(self.p4, self.p2)
        q12 = punkt_podzialu(self.p4, self.p1)

        return [Dywan(self.p1, q1, q2, q3, self.stopien + 1),
                Dywan(q3, q4, q5, q2, self.stopien + 1),
                Dywan(self.p2, q4, q5, q6, self.stopien + 1),
                Dywan(q6, q5, q8, q7, self.stopien + 1),
                Dywan(self.p3, q7, q8, q9, self.stopien + 1),
                Dywan(q9, q10, q11, q8, self.stopien + 1),
                Dywan(q10, q11, q12, self.p4, self.stopien + 1),
                Dywan(q1, q2, q11, q12, self.stopien + 1)]


czworokaty = {Dywan([0.0, 0.0], [0.0, 1000.0], [1000.0, 1000.0],
                    [1000.0, 0.0], 0)}

for i in range(6):
    nowe = []
    for t in czworokaty:
        nowe += t.podziel()
    czworokaty = nowe


def list_to_svgc(figury):
    """ tworzy text gotowy dozapisania w pliku."""
    res = '''<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n'''
    res += "\n".join([str(linia) for linia in figury])
    return res + '\n</svg>'


with open('dywan.svg', 'w') as tf:
    tf.write(list_to_svgc(czworokaty))
__author__ = 'mz'