#!/usr/bin/env python3

import unittest


class TrieTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        from greekutils.trie import Trie
        super(TrieTest, self).__init__(*args, **kwargs)
        self.t = Trie()

    def test_1(self):
        self.t.add("foo", "bar")
        self.assertEqual(self.t.find_prefix("fo"), ("", None, "fo"))
        self.assertEqual(self.t.find_prefix("foo"), ("foo", "bar", ""))
        self.assertEqual(self.t.find_prefix("food"), ("foo", "bar", "d"))

    def test_2(self):
        self.t.add("a", "yes")
        self.t.add("abc", "yes")
        self.assertEqual(self.t.find_prefix("abdc"), ("a", "yes", "bdc"))


class Beta2UnicodeTest(unittest.TestCase):

    def test_1(self):
        from greekutils.beta2unicode import convert
        self.assertEqual(convert("LO/GOS\n"), "λόγος")

    def test_2(self):
        from greekutils.beta2unicode import convert
        with self.assertRaises(KeyError):
            convert("(@)")


class TrigramTest(unittest.TestCase):

    def test_1(self):
        from greekutils.trigrams import trigrams
        self.assertEqual(list(trigrams("ABC")), [
            (None, "A", "B"),
            ("A", "B", "C"),
            ("B", "C", None),
        ])


class VerseRefTest(unittest.TestCase):

    def test_1(self):
        from greekutils.verse_ref import bcv_to_verse_ref
        self.assertEqual(bcv_to_verse_ref("010101"), "Matt 1:1")
        self.assertEqual(bcv_to_verse_ref("610101", start=61), "Matt 1:1")
        self.assertEqual(bcv_to_verse_ref("010101", separator="."), "Matt 1.1")


if __name__ == "__main__":
    unittest.main()
