from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str] = None
    ) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Parent node should have a tag")
        if self.children is None:
            raise ValueError("Parent node should have at least one child")

        children_content = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}{self.props_to_html()}>{children_content}</{self.tag}>"


if __name__ == "__main__":
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
    output: str = node.to_html()
    print(output)
