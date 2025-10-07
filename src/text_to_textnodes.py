from textnode import TextType, TextNode
from split_nodes import split_nodes_delimiter, split_nodes_images, split_nodes_links


def text_to_textnodes(text: str) -> list[TextNode]:
    if text is None:
        return []
    list_of_nodes: list[TextNode] = [TextNode(text, TextType.TEXT)]
    list_of_nodes = split_nodes_delimiter(list_of_nodes, "**", TextType.BOLD)
    list_of_nodes = split_nodes_delimiter(list_of_nodes, "_", TextType.ITALIC)
    list_of_nodes = split_nodes_delimiter(list_of_nodes, "`", TextType.CODE)
    list_of_nodes = split_nodes_images(list_of_nodes)
    list_of_nodes = split_nodes_links(list_of_nodes)
    return list_of_nodes


if __name__ == "__main__":
    text = """**This is a bold [link](youtube.com)**"""
    nodes: list[TextNode] = text_to_textnodes(text)
    print(nodes)
