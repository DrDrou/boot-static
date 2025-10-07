import unittest

from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_1(self) -> None:
        md: str = "# Title   "
        result: str = extract_title(md)
        self.assertEqual(result, "Title")

    def test_2(self) -> None:
        md: str = "No title"
        with self.assertRaises(Exception):
            result: str = extract_title(md)


if __name__ == "__main__":
    unittest.main()
