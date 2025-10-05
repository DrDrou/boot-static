import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self) -> None:
        node = HTMLNode(
            "a",
            "This is a link node",
            props={"href": "http://youtube.com", "alt": "youtube"},
        )
        text: str = node.props_to_html()
        result = 'href="http://youtube.com" alt="youtube"'
        self.assertIn(result, text)

    def test_init(self) -> None:
        node = HTMLNode("a", "link node")
        self.assertEqual("a", node.tag)

    def test_props(self) -> None:
        node = HTMLNode(
            "a",
            "link node",
            props={"href": "coucou", "prop2": "prop2value", "prop3": "prop3value"},
        )
        self.assertEqual(3, len(node.props))


if __name__ == "__main__":
    unittest.main()
