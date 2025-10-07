from .copy_and_replace_dir import copy_and_replace_dir
from .generate_page_recursive import generate_page_recursive


def main() -> None:
    print("Initializing public directory...")
    copy_and_replace_dir(source="static", destination="public")
    print("Public directory initialized!\n")

    print("Generating html page...")
    generate_page_recursive("content", "template.html", "public")
    print("html page generated..! \n")


if __name__ == "__main__":
    main()
