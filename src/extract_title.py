def extract_title(md: str) -> str:
    if md.startswith("# "):
        if md.find("\n\n") > 0:
            title, _ = md.split("\n\n", maxsplit=1)
        else:
            title: str = md
        return title[2:].strip()
    else:
        raise ValueError("no h1 title found")


if __name__ == "__main__":
    string1 = "# Hello "
    print(extract_title(string1))
