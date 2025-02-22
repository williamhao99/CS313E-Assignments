"""Big O Test Suite"""

import unittest

from bigo import (
    length_of_longest_substring_n3,
    length_of_longest_substring_n2,
    length_of_longest_substring_n,
)


class TestLongestSubstringN3(unittest.TestCase):
    """Test O(N^3) implementation."""

    def test_1(self):
        """O(N^3) approach with 'bevo', answer is 4."""
        actual = length_of_longest_substring_n3("bevo")
        expected = 4
        self.assertEqual(actual, expected)

    def test_2(self):
        """O(N^3) approach with empty string, answer is 0."""
        actual = length_of_longest_substring_n3("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_3(self):
        """O(N^3) approach with 'Longhorns', answer is 6."""
        actual = length_of_longest_substring_n3("Longhorns")
        expected = 6
        self.assertEqual(actual, expected)

    def test_4(self):
        """O(N^3) approach with 'abcdefghijk', answer is 11."""
        actual = length_of_longest_substring_n3("abcdefghijk")
        expected = 11
        self.assertEqual(actual, expected)

    def test_5(self):
        """O(N^3) approach with 'cs313e', answer is 4."""
        actual = length_of_longest_substring_n3("cs313e")
        expected = 4
        self.assertEqual(actual, expected)

    def test_6(self):
        """O(N^3) approach with 'bevoBits', answer is 8."""
        actual = length_of_longest_substring_n3("bevoBits")
        expected = 8
        self.assertEqual(actual, expected)

    def test_7(self):
        """O(N^3) approach with 'UTTower', answer is 5."""
        actual = length_of_longest_substring_n3("UTTower")
        expected = 5
        self.assertEqual(actual, expected)

    def test_8(self):
        """O(N^3) approach with 'CompSci', answer is 7."""
        actual = length_of_longest_substring_n3("CompSci")
        expected = 7
        self.assertEqual(actual, expected)

    def test_9(self):
        """O(N^3) approach with 'abcda', answer is 4."""
        actual = length_of_longest_substring_n3("abcda")
        expected = 4
        self.assertEqual(actual, expected)

    def test_10(self):
        """O(N^3) approach with 'anviaj', answer is 5."""
        actual = length_of_longest_substring_n3("anviaj")
        expected = 5
        self.assertEqual(actual, expected)


class TestLongestSubstringN2(unittest.TestCase):
    """Test O(N^2) implementation."""

    def test_1(self):
        """O(N^2) approach with 'bevo', answer is 4."""
        actual = length_of_longest_substring_n2("bevo")
        expected = 4
        self.assertEqual(actual, expected)

    def test_2(self):
        """O(N^2) approach with empty string, answer is 0."""
        actual = length_of_longest_substring_n2("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_3(self):
        """O(N^2) approach with 'Longhorns', answer is 6."""
        actual = length_of_longest_substring_n2("Longhorns")
        expected = 6
        self.assertEqual(actual, expected)

    def test_4(self):
        """O(N^2) approach with 'abcdefghijk', answer is 11."""
        actual = length_of_longest_substring_n2("abcdefghijk")
        expected = 11
        self.assertEqual(actual, expected)

    def test_5(self):
        """O(N^2) approach with 'cs313e', answer is 4."""
        actual = length_of_longest_substring_n2("cs313e")
        expected = 4
        self.assertEqual(actual, expected)

    def test_6(self):
        """O(N^2) approach with 'bevoBits', answer is 8."""
        actual = length_of_longest_substring_n2("bevoBits")
        expected = 8
        self.assertEqual(actual, expected)

    def test_7(self):
        """O(N^2) approach with 'UTTower', answer is 5."""
        actual = length_of_longest_substring_n2("UTTower")
        expected = 5
        self.assertEqual(actual, expected)

    def test_8(self):
        """O(N^2) approach with 'CompSci', answer is 7."""
        actual = length_of_longest_substring_n2("CompSci")
        expected = 7
        self.assertEqual(actual, expected)

    def test_9(self):
        """O(N^2) approach with 'abcda', answer is 4."""
        actual = length_of_longest_substring_n2("abcda")
        expected = 4
        self.assertEqual(actual, expected)

    def test_10(self):
        """O(N^2) approach with 'anviaj', answer is 5."""
        actual = length_of_longest_substring_n2("anviaj")
        expected = 5
        self.assertEqual(actual, expected)

    def test_11(self):
        """O(N^2) approach with 'tmmzuxt', answer is 5."""
        actual = length_of_longest_substring_n2("tmmzuxt")
        expected = 5
        self.assertEqual(actual, expected)

    def test_12(self):
        """O(N^2) approach with 'qrstuqr', answer is 5."""
        actual = length_of_longest_substring_n2("qrstuqr")
        expected = 5
        self.assertEqual(actual, expected)

    def test_13(self):
        """O(N^2) approach with 'UTCS!rocks4EVER', answer is 13."""
        actual = length_of_longest_substring_n2("UTCS!rocks4EVER")
        expected = 13
        self.assertEqual(actual, expected)

    def test_14(self):
        """O(N^2) approach with 'hooked on coding!', answer is 8."""
        actual = length_of_longest_substring_n2("hooked on coding!")
        expected = 8
        self.assertEqual(actual, expected)

    def test_15(self):
        """O(N^2) approach with 'longsubstring', answer is 8."""
        actual = length_of_longest_substring_n2("longsubstring")
        expected = 8
        self.assertEqual(actual, expected)

    def test_16(self):
        """O(N^2) approach with 'abcd1234abcd', answer is 8."""
        actual = length_of_longest_substring_n2("abcd1234abcd")
        expected = 8
        self.assertEqual(actual, expected)

    def test_17(self):
        """O(N^2) approach with 'abcdefghijklmnopqrstuvwxyz', answer is 26."""
        actual = length_of_longest_substring_n2("abcdefghijklmnopqrstuvwxyz")
        expected = 26
        self.assertEqual(actual, expected)

    def test_18(self):
        """O(N^2) approach with '1!2@3#4$5%6^7&8*9(0)', answer is 20."""
        actual = length_of_longest_substring_n2("1!2@3#4$5%6^7&8*9(0)")
        expected = 20
        self.assertEqual(actual, expected)

    def test_19(self):
        """O(N^2) approach with 'thequickbrownfoxjumpsover', answer is 14."""
        actual = length_of_longest_substring_n2("thequickbrownfoxjumpsover")
        expected = 14
        self.assertEqual(actual, expected)

    def test_20(self):
        """O(N^2) approach with '   ', answer is 1."""
        actual = length_of_longest_substring_n2("   ")
        expected = 1
        self.assertEqual(actual, expected)


class TestLongestSubstringN(unittest.TestCase):
    """Test O(N) implementation."""

    def test_1(self):
        """O(N) approach with 'bevo', answer is 4."""
        actual = length_of_longest_substring_n("bevo")
        expected = 4
        self.assertEqual(actual, expected)

    def test_2(self):
        """O(N) approach with empty string, answer is 0."""
        actual = length_of_longest_substring_n("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_3(self):
        """O(N) approach with 'Longhorns', answer is 6."""
        actual = length_of_longest_substring_n("Longhorns")
        expected = 6
        self.assertEqual(actual, expected)

    def test_4(self):
        """O(N) approach with 'abcdefghijk', answer is 11."""
        actual = length_of_longest_substring_n("abcdefghijk")
        expected = 11
        self.assertEqual(actual, expected)

    def test_5(self):
        """O(N) approach with 'cs313e', answer is 4."""
        actual = length_of_longest_substring_n("cs313e")
        expected = 4
        self.assertEqual(actual, expected)

    def test_6(self):
        """O(N) approach with 'bevoBits', answer is 8."""
        actual = length_of_longest_substring_n("bevoBits")
        expected = 8
        self.assertEqual(actual, expected)

    def test_7(self):
        """O(N) approach with 'UTTower', answer is 5."""
        actual = length_of_longest_substring_n("UTTower")
        expected = 5
        self.assertEqual(actual, expected)

    def test_8(self):
        """O(N) approach with 'CompSci', answer is 7."""
        actual = length_of_longest_substring_n("CompSci")
        expected = 7
        self.assertEqual(actual, expected)

    def test_9(self):
        """O(N) approach with 'abcda', answer is 4."""
        actual = length_of_longest_substring_n("abcda")
        expected = 4
        self.assertEqual(actual, expected)

    def test_10(self):
        """O(N) approach with 'anviaj', answer is 5."""
        actual = length_of_longest_substring_n("anviaj")
        expected = 5
        self.assertEqual(actual, expected)

    def test_11(self):
        """O(N) approach with 'tmmzuxt', answer is 5."""
        actual = length_of_longest_substring_n("tmmzuxt")
        expected = 5
        self.assertEqual(actual, expected)

    def test_12(self):
        """O(N) approach with 'qrstuqr', answer is 5."""
        actual = length_of_longest_substring_n("qrstuqr")
        expected = 5
        self.assertEqual(actual, expected)

    def test_13(self):
        """O(N) approach with 'UTCS!rocks4EVER', answer is 13."""
        actual = length_of_longest_substring_n("UTCS!rocks4EVER")
        expected = 13
        self.assertEqual(actual, expected)

    def test_14(self):
        """O(N) approach with 'hooked on coding!', answer is 8."""
        actual = length_of_longest_substring_n("hooked on coding!")
        expected = 8
        self.assertEqual(actual, expected)

    def test_15(self):
        """O(N) approach with 'longsubstring', answer is 8."""
        actual = length_of_longest_substring_n("longsubstring")
        expected = 8
        self.assertEqual(actual, expected)

    def test_16(self):
        """O(N) approach with 'abcd1234abcd', answer is 8."""
        actual = length_of_longest_substring_n("abcd1234abcd")
        expected = 8
        self.assertEqual(actual, expected)

    def test_17(self):
        """O(N) approach with 'abcdefghijklmnopqrstuvwxyz', answer is 26."""
        actual = length_of_longest_substring_n("abcdefghijklmnopqrstuvwxyz")
        expected = 26
        self.assertEqual(actual, expected)

    def test_18(self):
        """O(N) approach with '1!2@3#4$5%6^7&8*9(0)', answer is 20."""
        actual = length_of_longest_substring_n("1!2@3#4$5%6^7&8*9(0)")
        expected = 20
        self.assertEqual(actual, expected)

    def test_19(self):
        """O(N) approach with 'thequickbrownfoxjumpsover', answer is 14."""
        actual = length_of_longest_substring_n("thequickbrownfoxjumpsover")
        expected = 14
        self.assertEqual(actual, expected)

    def test_20(self):
        """O(N) approach with '   ', answer is 1."""
        actual = length_of_longest_substring_n("   ")
        expected = 1
        self.assertEqual(actual, expected)

    def test_21(self):
        """O(N) approach with 'abc abc abc ', answer is 4."""
        actual = length_of_longest_substring_n("abc abc abc ")
        expected = 4
        self.assertEqual(actual, expected)

    def test_22(self):
        """O(N) approach with 'aaaaaaaaaaaaaaaaaaaaaa', answer is 1."""
        actual = length_of_longest_substring_n("aaaaaaaaaaaaaaaaaaaaaa")
        expected = 1
        self.assertEqual(actual, expected)

    def test_23(self):
        """O(N) approach with '   checking...   ', answer is 8."""
        actual = length_of_longest_substring_n("   checking...   ")
        expected = 8
        self.assertEqual(actual, expected)

    def test_24(self):
        """O(N) approach with 'aaabcdefghabcdefghijklmno', answer is 15."""
        actual = length_of_longest_substring_n("aaabcdefghabcdefghijklmno")
        expected = 15
        self.assertEqual(actual, expected)

    def test_25(self):
        """O(N) approach with 'aabbccddeeffgghh', answer is 2."""
        actual = length_of_longest_substring_n("aabbccddeeffgghh")
        expected = 2
        self.assertEqual(actual, expected)

    def test_26(self):
        """O(N) approach with 'hellohibye_123456' repeated 30 times, answer is 14."""
        actual = length_of_longest_substring_n("hellohibye_123456" * 30)
        expected = 14
        self.assertEqual(actual, expected)

    def test_27(self):
        """O(N) approach with long numeric string repeated 6 times, answer is 10."""
        actual = length_of_longest_substring_n(
            "123456789101112131415161718192021222324252627282930" * 6
        )
        expected = 10
        self.assertEqual(actual, expected)

    def test_28(self):
        """O(N) approach with with numbers symbols and letters repeated 8 times, answer is 62."""
        actual = length_of_longest_substring_n(
            "AbCdEfGhIjKlMnOpQrStUvWxYz_aBcDeFgHiJkLmNoPqRsTuVwXyZ_123456789" * 8
        )
        expected = 62
        self.assertEqual(actual, expected)

    def test_29(self):
        """O(N) approach with long numeric string repeated 10 times, answer is 10."""
        actual = length_of_longest_substring_n(
            "123456789101112131415161718192021222324252627282930" * 10
        )
        expected = 10
        self.assertEqual(actual, expected)

    def test_30(self):
        """O(N) approach with long alphabetical and symbol string repeated 5 times, answer is 54."""
        actual = length_of_longest_substring_n(
            "abcdefghijklmnoPQRSTUVWXYZabcdefgHIJKLMNOPQRSTuvwxYz0123456789!@#$%^&*()"
            * 5
        )
        expected = 54
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
