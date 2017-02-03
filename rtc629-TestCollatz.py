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

from Collatz import collatz_read, do_bin, bin_collatz, check_meta, max_collatz, collatz_eval, collatz_print, collatz_solve

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
        v = collatz_eval(1000, 1200)
        self.assertEqual(v, 182)

    def test_eval_5 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # ----
    # do_bin
    # ----

    def test_do_bin_1 (self):
        b = do_bin(3)
        self.assert_(b == "11")

    def test_do_bin_1 (self):
        b = do_bin(2344)
        self.assert_(b == "100100101000")

    def test_do_bin_1 (self):
        b = do_bin(777)
        self.assert_(b == "1100001001")

    # ----
    # bin_collatz
    # ----
    
    def test_bin_collatz_1 (self):
        c = bin_collatz(9)
        self.assert_(c == 20)
        
    def test_bin_collatz_2 (self):
        c = bin_collatz(871)
        self.assert_(c == 179)
        
    def test_bin_collatz_3 (self):
        c = bin_collatz(999999)
        self.assert_(c == 259)

    # ----
    # check_meta
    # ----
    def test_check_meta_1 (self):
        m = check_meta(range(1, 10))
        self.assert_(m == 20)
        
    def test_check_meta_2 (self):
        m = check_meta(range(23443, 48230))
        self.assert_(m == 324)
        
    def test_check_meta_3 (self):
        m = check_meta(range(1, 999999))
        self.assert_(m == 525)

    # ----
    # max_collatz
    # ----
    def dummy_function (num):
        return 123
    
    def test_max_collatz_1 (self):
        x = max_collatz(dummy_function, 1, 1)
        self.assert_(x == 123)

    def test_max_collatz_1 (self):
        x = max_collatz(dummy_function, 1, 10)
        self.assert_(x == 9)

    def test_max_collatz_1 (self):
        x = max_collatz(bin_collatz, 1, 999999)
        self.assert_(x == 525)        
    

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "34 0 234\n")    

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 7, 7, 7)
        self.assertEqual(w.getvalue(), "7 7 7\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999999, 235, 132)
        self.assert_(w.getvalue() == "999999 235 132\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n1000 1200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n1000 1200 182\n")

    def test_solve_2(self) :
        r = StringIO("100 200\n201 210\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 200 125\n201 210 89\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_solve_4 (self) :
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")

# ----
# main
# ----

if __name__ == "__main__":
    main()

''' #pragma: no cover
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

'''
