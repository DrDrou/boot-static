class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list = None,
        props: dict[str] = None,
    ) -> None:
        self.tag: str = tag
        self.value: str = value
        self.children: list[HTMLNode] = children
        self.props: dict[str] = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> None:
        if self.props is None:
            return ""
        attr_strings: list[str] = [
            f'{key}="{value}"' for key, value in self.props.items()
        ]
        return " " + " ".join(attr_strings)
