import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self) -> None:
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self) -> None:
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_with_props(self) -> None:
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"class": "para-three", "id": "main-paragraph"},
        )
        self.assertEqual(
            node.to_html(),
            '<p class="para-three" id="main-paragraph"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )


if __name__ == "__main__":
    unittest.main()
