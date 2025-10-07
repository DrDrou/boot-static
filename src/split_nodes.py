from textnode import TextNode, TextType
from extraction_functions import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_texts: list[str] = node.text.split(delimiter)
            for index, subtext in enumerate(split_texts):
                if subtext != "":
                    if index & 1:
                        new_nodes.append(TextNode(subtext, text_type))
                    else:
                        new_nodes.append(TextNode(subtext, node.text_type))

        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        matches: list[tuple[str]] = extract_markdown_images(node.text)
        if len(matches) > 0:
            text: str = node.text
            for match in matches:
                matched_string: str = f"![{match[0]}]({match[1]})"
                pre, text = text.split(matched_string, maxsplit=1)
                if pre:
                    new_nodes.append(TextNode(pre, node.text_type))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            if text != "":
                new_nodes.append(TextNode(text, node.text_type))

        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        matches: list[tuple[str]] = extract_markdown_links(node.text)
        if len(matches) > 0:
            text: str = node.text
            for match in matches:
                matched_string: str = f"[{match[0]}]({match[1]})"
                pre, text = text.split(matched_string, maxsplit=1)
                if pre:
                    new_nodes.append(TextNode(pre, node.text_type))
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if text != "":
                new_nodes.append(TextNode(text, node.text_type))

        else:
            new_nodes.append(node)

    return new_nodes


if __name__ == "__main__":
    print(" test split_nodes_delimiter() ")
    node_1 = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes: list[TextNode] = split_nodes_delimiter([node_1], "`", TextType.CODE)
    for node in new_nodes:
        print(node)
    print()

    print(" test split_node_images() ")
    node_2 = TextNode(
        "This is text with an image ![to boot dev](https://www.boot.dev) and not much else.",
        TextType.TEXT,
    )
    print("input: ", node_2.text)
    new_nodes_2 = split_nodes_images([node_2])
    for node in new_nodes_2:
        print(node)
    print()

    print(" test split_nodes_links() ")
    node_3 = TextNode(
        "This a [link](youtube.com) and this is also a [linkkk](reddit.com)",
        TextType.TEXT,
    )
    node_4 = TextNode(
        "This a another [link](youtubjj.com) and s not **a link.**",
        TextType.TEXT,
    )
    print("input: ", node_3.text, node_4.text)
    new_nodes_3: list[TextNode] = split_nodes_links([node_3, node_4])
    for node in new_nodes_3:
        print(node)
    print()
