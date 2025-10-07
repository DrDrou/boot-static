from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md_block: str) -> BlockType:
    match: list[str] = re.findall(r"^#{1,6}\s", md_block)
    if len(match) > 0:
        return BlockType.HEADING

    if md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE

    lines: list[str] = md_block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    lines_processed: list[tuple[str, str]] = [
        line.split(". ", maxsplit=1) for line in lines
    ]
    if all(
        line[0].startswith(str(index + 1)) for index, line in enumerate(lines_processed)
    ):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


if __name__ == "__main__":
    blocks: list[str] = [
        "#### Rest of the owl",
        "```Code block```",
        ">quote line 1\n>quote line 2\n>quote line 3",
        "- list 1\n- list 2",
        "1. ordered list 1\n2. ordered list 2",
        "paragraph",
    ]

    block_types: list[BlockType] = []
    for md in blocks:
        block_types.append(block_to_block_type(md))

    print(block_types)
