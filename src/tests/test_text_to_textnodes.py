import unittest

from src.textnode import TextType, TextNode
from src.text_to_textnodes import text_to_textnodes


class TestTextToTextnodes(unittest.TestCase):
    def test_1(self) -> None:
        text: str = """This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"""
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_2(self) -> None:
        text = """**This is a bold [link](youtube.com)**"""
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a bold ", TextType.BOLD),
                TextNode("link", TextType.LINK, "youtube.com"),
            ],
            nodes,
        )

    def test_3(self) -> None:
        text: str = "This is ![an image](imgur.com) and text in italic _cool cool_"
        nodes: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("an image", TextType.IMAGE, "imgur.com"),
                TextNode(" and text in italic ", TextType.TEXT),
                TextNode("cool cool", TextType.ITALIC),
            ],
            nodes,
        )
