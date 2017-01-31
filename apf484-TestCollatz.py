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

from Collatz import collatz_read, calc_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "100 90\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 90)

    def test_read_3(self):
        s = "-100 90\n"
        result = collatz_read(s)
        self.assertFalse(result)

    # ----
    # calc_cycle_length
    # ----

    def test_calc_cycle_length_1(self):
        v = calc_cycle_length(1)
        self.assertEqual(v, 1)

    def test_calc_cycle_length_2(self):
        v = calc_cycle_length(654321)
        self.assertEqual(v, 186)

    def test_calc_cycle_length_3(self):
        v = calc_cycle_length(12345)
        self.assertEqual(v, 51)

    def test_calc_cycle_length_4(self):
        v = calc_cycle_length(999999)
        self.assertEqual(v, 259)

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
        v = collatz_eval(1101, 1011)
        self.assertEqual(v, 169)

    def test_eval_6(self):
        v = collatz_eval(123456, 654321)
        self.assertEqual(v, 509)
 
    def test_eval_7(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)
 
    def test_eval_8(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 2000, 100, 182)
        self.assertEqual(w.getvalue(), "2000 100 182\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 10\n11 100\n101 1000\n1001 10000\n10001 100000\n100001 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n11 100 119\n101 1000 179\n1001 10000 262\n10001 100000 351\n100001 999999 525\n")
 
    def test_solve_3(self):
        r = StringIO("1 2\n1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 2 2\n1 999999 525\n")
 
    def test_solve_4(self):
        r = StringIO("999999 1\n1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "999999 1 525\n1 999999 525\n")

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