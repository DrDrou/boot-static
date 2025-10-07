import unittest
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from src.text_node_to_html_node import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_1(self) -> None:
        text_node = TextNode("click here", TextType.LINK, "youtube.com")
        html_node: LeafNode = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="youtube.com">click here</a>')

    def test_text(self) -> None:
        node = TextNode("This is a text node", TextType.TEXT)
        html_node: LeafNode = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
