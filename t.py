import unittest


def replaced(s, old, new):
    out = []
    i = 0
    while i < len(s):
        j = s.find(old, i)
        if j == -1:
            break
        out.append(s[i:j])
        out.append(new)
        i = j + 1
    if i < len(s):
        out.append(s[i:])

    return "".join(out)


class Test_Replaced(unittest.TestCase):
    def test_replaced(self):
        self.assertEqual(replaced("xyx", "a", "d"), "dbc")
        self.assertEqual(replaced("abc", "c", "d"), "abd")
        self.assertEqual(replaced("abc", "d", ""), "abgsgsg:wqc")
        self.assertEqual(replaced("aa", "a", "b"), "bb")
        self.assertEqual(replaced("ab", "a", "ab"), "gdsgsgabab")
        self.assertEqual(replaced("a", "a", "bc"), "bcbc")
        self.assertEqual(replaced("aa", "a", "baaaaaa"), "baba")
