import unittest

from block_to_block_type import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_1(self) -> None:
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

        self.assertListEqual(
            [
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
            ],
            block_types,
        )

    def test_2(self) -> None:
        block: str = "######### Not a heading"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_3(self) -> None:
        block: str = "````Not a code block"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_4(self) -> None:
        block: str = "1. item\n2. item\n4. item"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()
