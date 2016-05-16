import os.path
import unittest

from   sage.all import SR, matrix
from   fuchsia import (is_fuchsian, fuchsify_by_blocks, transform, _parser)

class Test(unittest.TestCase):
    def assert_fuchsify_by_blocks_works(test, m,b,x,eps):
        test.assertFalse(is_fuchsian(m, x))

        mt, t = fuchsify_by_blocks(m, b, x, eps)
        test.assertTrue((mt-transform(m, x, t)).simplify_rational().is_zero())
        test.assertTrue(is_fuchsian(mt, x))

    def test_fuchsify_by_blocks_01(test):
        x, eps = SR.var("x eps")
        m = matrix([
            [ eps/x,       0,       0],
            [     0, 2*eps/x,  -eps/x],
            [1/x**2,       0, 3*eps/x],
        ])
        b = [(0,1),(1,2)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)

    def test_fuchsify_by_blocks_02(test):
        x, eps = SR.var("x eps")
        m = matrix([
            [ eps/x/(x-1),       0,       0],
            [  1/(x-1)**2, 2*eps/x,  -eps/x],
            [      1/x**2,       0, 3*eps/x],
        ])
        b = [(0,1),(1,2)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)

    def test_fuchsify_by_blocks_03(test):
        x, eps = SR.var("x eps")
        m = matrix([
            [  eps/x,       0,       0],
            [ 1/x**2, 2*eps/x,       0],
            [ 1/x**2,  2/x**2, 3*eps/x],
        ])
        b = [(0,1),(1,1),(2,1)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)

    def test_fuchsify_by_blocks_04(test):
        x, eps = SR.var("x eps")
        m = matrix([
            [     eps/x/(x-1),               0,             0],
            [ 1/x**2/(x-1)**2,   2*eps/x/(x-1),             0],
            [ 1/x**2/(x-1)**2, 2/x**2/(x-1)**2, 3*eps/x/(x-1)],
        ])
        b = [(0,1),(1,1),(2,1)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)

    def test_fuchsify_by_blocks_05(test):
        x, eps = SR.var("x eps")
        m = matrix([
            [ eps/x,       0,       0],
            [     0, 2*eps/x,  -eps/x],
            [  x**2,       0, 3*eps/x],
        ])
        b = [(0,1),(1,2)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)


    def test_fuchsify_by_blocks_06(test):
        x, eps = SR.var("x eps")
        m = matrix([
            [eps/(x - 1), 0, 0],
            [(x**3 + x**2 - 3*x - 3)/(2*x**3 - 2*x**2 - x + 1), 2*eps/(x - 3), 0],
            [-(x**3 + 3*x**2 - 3*x + 2)/(2*x**3 + x**2 - 2*x) + 2*(x**3 - x**2 - x + 1)/(2*x + 1),
                -3*(x**3 + x - 1)/(3*x**3 + x - 2),
                4*eps/(x - 5)]
        ])
        b = [(0,1),(1,1),(2,1)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)

    @unittest.skip("needs more work to pass")
    def test_fuchsify_by_blocks_07(test):
        x, eps = SR.var("x ep")
        #m10 = "-924/5*ep^2 - 154*ep - 1/10*(189728*ep^2 - 12*(8932*ep^2 + 12261*ep)*x + 245347*ep - 9240)/(30*x^2 - 87*x + 77) + 231*(208*(2*ep + 1)*x - 826*ep - 413)/(30*x^2 - 87*x + 77)^2 - 154/5"
        #m10 = "1 + 1/(30*x^2 - 87*x + 77) + 1/(30*x^2 - 87*x + 77)^2"
        m10 = "1/(x^2 - x + 1)^2"
        m = matrix([
            [0,0],
            [1/(x**2-x+1)**2, 0]
        ])
        b = [(0,1),(1,1)]
        test.assert_fuchsify_by_blocks_works(m, b, x, eps)
