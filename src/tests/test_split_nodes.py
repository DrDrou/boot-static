import unittest

from src.textnode import TextType, TextNode
from src.split_nodes import split_nodes_delimiter, split_nodes_images, split_nodes_links


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_1(self) -> None:
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def test_2(self) -> None:
        node = TextNode("This is **bold text** and this is normal text.", TextType.TEXT)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_3(self) -> None:
        node = TextNode("This is _italic text_ and this is normal text.", TextType.TEXT)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_4(self) -> None:
        node = TextNode(
            "This is _italic text_ and this is _also italic text._", TextType.TEXT
        )
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)

    def test_5(self) -> None:
        node = TextNode("**bold text**", TextType.TEXT)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)


class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self) -> None:
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes: list[TextNode] = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_2(self) -> None:
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another [link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes: list[TextNode] = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    " and another [link](https://i.imgur.com/3elNhQu.png)",
                    TextType.TEXT,
                ),
            ],
            new_nodes,
        )

    def test_split_links(self) -> None:
        node = TextNode(
            "This is text with a [link](youtube.com) and another [link2](youtube.com)",
            TextType.TEXT,
        )
        new_nodes: list[TextNode] = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "youtube.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "youtube.com"),
            ],
            new_nodes,
        )

    def test_split_link_2(self) -> None:
        node = TextNode(
            "This is text with a [link](youtube.com) and an image ![image](youtube.com)",
            TextType.TEXT,
        )
        new_nodes: list[TextNode] = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "youtube.com"),
                TextNode(" and an image ![image](youtube.com)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_3(self) -> None:
        node = TextNode(
            "[link](youtube.com)",
            TextType.TEXT,
        )
        new_nodes: list[TextNode] = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "youtube.com"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
