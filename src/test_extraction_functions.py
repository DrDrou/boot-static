import unittest

from extraction_functions import extract_markdown_images, extract_markdown_links


class TestExtractionFunctions(unittest.TestCase):
    def test_extract_images_1(self) -> None:
        matches: list[tuple[str]] = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_images_2(self) -> None:
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches: list[tuple[str]] = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_links_1(self) -> None:
        matches: list[tuple[str]] = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_links_2(self) -> None:
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches: list[tuple[str]] = extract_markdown_links(text)
        self.assertEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_no_result(self) -> None:
        matches: list[tuple[str]] = extract_markdown_images(
            "This is text without an image or link"
        )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
