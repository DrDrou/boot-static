from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode


def markdown_to_html_node(md: str) -> ParentNode:
    if not md:
        return None

    block_parent_nodes: list[ParentNode] = []
    blocks: list[str] = markdown_to_blocks(md)
    for block in blocks:
        block_type: BlockType = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children: list[TextNode] = text_to_textnodes(block)
            children_html: list[LeafNode] = [
                text_node_to_html_node(child) for child in children
            ]
            block_parent_node: ParentNode = ParentNode(
                tag="p", children=children_html, props=None
            )
            block_parent_nodes.append(block_parent_node)

        elif block_type == BlockType.HEADING:
            header_type, block_content = block.split(" ", maxsplit=1)
            header_tag: str = f"h{len(header_type)}"

            children: list[TextNode] = text_to_textnodes(block_content)
            children_html: list[LeafNode] = [
                text_node_to_html_node(child) for child in children
            ]
            block_parent_node: ParentNode = ParentNode(
                tag=header_tag, children=children_html, props=None
            )
            block_parent_nodes.append(block_parent_node)

        elif block_type == BlockType.CODE:
            content: str = block[3:-3]
            content_node = LeafNode(tag="code", value=content)
            block_parent_node = ParentNode(tag="pre", children=[content_node])
            block_parent_nodes.append(block_parent_node)

        elif block_type == BlockType.QUOTE:
            quote_parent_nodes: list[ParentNode] = []
            quotes: list[str] = [quote.strip(">") for quote in block.split("\n")]
            for quote in quotes:
                quote_nodes: list[TextNode] = text_to_textnodes(quote)
                quote_nodes_html: list[LeafNode] = [
                    text_node_to_html_node(textnode) for textnode in quote_nodes
                ]
                quote_parent_node: ParentNode = ParentNode("p", quote_nodes_html)
                quote_parent_nodes.append(quote_parent_node)

            block_parent_node: ParentNode = ParentNode(
                tag="blockquote", children=quote_parent_nodes
            )
            block_parent_nodes.append(block_parent_node)

        elif block_type == BlockType.UNORDERED_LIST:
            item_parent_nodes: list[ParentNode] = []
            items: list[str] = [line.strip("- ") for line in block.split("\n")]
            for item in items:
                item_nodes: list[TextNode] = text_to_textnodes(item)
                item_nodes_html: list[LeafNode] = [
                    text_node_to_html_node(item_node) for item_node in item_nodes
                ]
                item_parent_node: ParentNode = ParentNode("li", item_nodes_html)
                item_parent_nodes.append(item_parent_node)
            block_parent_node: ParentNode = ParentNode("ul", item_parent_nodes)
            block_parent_nodes.append(block_parent_node)

        elif block_type == BlockType.ORDERED_LIST:
            item_parent_nodes: list[ParentNode] = []
            items: list[str] = block.split("\n")
            for index, item in enumerate(items):
                _, item_content = item.split(". ", maxsplit=1)
                item_nodes: list[TextNode] = text_to_textnodes(item_content)
                item_nodes_html: list[LeafNode] = [
                    text_node_to_html_node(item_node) for item_node in item_nodes
                ]
                item_parent_node: ParentNode = ParentNode("li", item_nodes_html)
                item_parent_nodes.append(item_parent_node)
            block_parent_node: ParentNode = ParentNode("ol", item_parent_nodes)
            block_parent_nodes.append(block_parent_node)

        else:
            raise ValueError("Block Type not implemented yet")

    main_parent_node: ParentNode = ParentNode("div", block_parent_nodes)
    return main_parent_node


if __name__ == "__main__":
    md_1 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    html_node_1: ParentNode = markdown_to_html_node(md_1)
    print(html_node_1.to_html())

    print("------------\n")

    md_2 = "```some _italic_ code```"
    html_node_2: ParentNode = markdown_to_html_node(md_2)
    print(html_node_2.to_html())

    print("------------\n")

    md_3 = "## Heading 2 title\n\n### Heading 3\n\n\n\n\n\n\nBolded paragrpah: **coolcoolcol**\n\n>quote we love **big cats**"
    html_node_3: ParentNode = markdown_to_html_node(md_3)
    print(html_node_3.to_html())

    print("------------\n")

    md_4 = "- list 1 **bold text**\n- list 2 _italic_"
    html_node_4: ParentNode = markdown_to_html_node(md_4)
    print(html_node_4.to_html())

    print("------------\n")

    md_5 = "1. list 1\n2. list2 **bold**"
    html_node_5: ParentNode = markdown_to_html_node(md_5)
    print(html_node_5.to_html())
