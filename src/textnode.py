from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"  # [anchor text](url)
    IMAGE = "image"  # ![alt text](url)


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None) -> None:
        if not isinstance(text_type, TextType):
            raise ValueError(f"text_type must be a TextType enum, got {type(text_type).__name__}")
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str = url

    def __eq__(self, target) -> bool:
        return (
            self.text == target.text
            and self.text_type == target.text_type
            and self.url == target.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
