from textnode import TextNode


def main() -> None:
    node = TextNode("This is some text", "link", "http://youtube.com")
    print(node)


if __name__ == "__main__":
    main()
