from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str = None, props: dict[str] = None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Leaf nodes must have a value.")
        if self.tag is None:
            return self.value

        html_props: str = self.props_to_html()
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"


if __name__ == "__main__":
    # Example usage
    node = LeafNode("p", "Hello, world!")
    print(node.to_html())

    node_with_props = LeafNode("a", "Click me", {"href": "https://example.com"})
    print(node_with_props.to_html())
