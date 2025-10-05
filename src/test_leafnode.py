import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_1(self) -> None:
        node = LeafNode("p", "Hello, world!")
        result = "<p>Hello, world!</p>"
        self.assertEqual(result, node.to_html())

    def test_2(self) -> None:
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        result = '<a href="https://example.com">Click me</a>'
        self.assertEqual(result, node.to_html())

    def test_none(self) -> None:
        result = "No tag test"
        node = LeafNode(tag=None, value=result)
        self.assertEqual(result, node.to_html())


if __name__ == "__main__":
    unittest.main()
