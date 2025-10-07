import sys
from .copy_and_replace_dir import copy_and_replace_dir
from .generate_page_recursive import generate_page_recursive

basepath: str = sys.argv[1] if len(sys.argv) > 1 else "/"


def main() -> None:
    print("Initializing public directory...")
    copy_and_replace_dir(source="static", destination="docs")
    print("Public directory initialized!\n")

    print("Generating html page...")
    generate_page_recursive("content", "template.html", "docs", basepath)
    print("html page generated..! \n")


if __name__ == "__main__":
    main()
