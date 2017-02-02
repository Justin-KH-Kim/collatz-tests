#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "125 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 125)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "310 400\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 310)
        self.assertEqual(j, 400)

    def test_read_4(self):
        s = "888 999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 888)
        self.assertEqual(j, 999)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(15, 30)
        self.assertEqual(v, 112)

    def test_eval_6(self):
        v = collatz_eval(350, 415)
        self.assertEqual(v, 134)

    def test_eval_7(self):
        v = collatz_eval(500, 700)
        self.assertEqual(v, 145)

    def test_eval_7(self):
        v = collatz_eval(1010, 2050)
        self.assertEqual(v, 182)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 350, 415, 134)
        self.assertEqual(w.getvalue(), "350 415 134\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 500, 700, 145)
        self.assertEqual(w.getvalue(), "500 700 145\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1010, 2050, 182)
        self.assertEqual(w.getvalue(), "1010 2050 182\n")


    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 5\n1000 2000\n2110 2222\n9000 10000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 5 8\n1000 2000 182\n2110 2222 170\n9000 10000 260\n")

    def test_solve_3(self):
        r = StringIO("5 20\n300 400\n450 460\n555 666\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5 20 21\n300 400 144\n450 460 129\n555 666 145\n")

    




# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""