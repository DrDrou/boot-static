from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text_node_type: TextType = text_node.text_type

    match text_node_type:
        case TextType.TEXT:
            tag = None
            value = text_node.text
            props = None
        case TextType.BOLD:
            tag = "b"
            value: str = text_node.text
            props = None
        case TextType.ITALIC:
            tag = "i"
            value: str = text_node.text
            props = None
        case TextType.CODE:
            tag = "code"
            value: str = text_node.text
            props = None
        case TextType.LINK:
            tag = "a"
            value: str = text_node.text
            props = {"href": text_node.url}
        case TextType.IMAGE:
            tag = "img"
            value = ""
            props = {"src": text_node.url, "alt": text_node.text}
        case _:
            raise Exception("Unrecognized text type")

    return LeafNode(tag, value, props)


if __name__ == "__main__":
    text_node = TextNode("click here", TextType.LINK, "youtube.com")
    print(text_node)
    html_node: LeafNode = text_node_to_html_node(text_node)
    print(html_node.to_html())
