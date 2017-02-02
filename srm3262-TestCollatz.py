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

    def test_read_1 (self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2 (self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3 (self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

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
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_6(self):
        v = collatz_eval(50, 42)
        self.assertEqual(v, 105)

    # -----
    # print
    # -----

    def test_print_1 (self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3 (self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self):
        r = StringIO("2 12\n5 15\n30 60\n40 78\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2 12 20\n5 15 20\n30 60 113\n40 78 116\n")

    def test_solve_3 (self):
        r = StringIO("300 350\n300 400\n300 500\n501 503\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "300 350 144\n300 400 144\n300 500 144\n501 503 111\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
...............
----------------------------------------------------------------------
Ran 15 tests in 0.011s

OK



% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
...............
----------------------------------------------------------------------
Ran 15 tests in 0.011s

OK

Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          30      0     12      0   100%
TestCollatz.py      66      0      0      0   100%
------------------------------------------------------------
TOTAL               96      0     12      0   100%
"""
