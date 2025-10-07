import os
from .generate_page import generate_page


def generate_page_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
) -> None:
    if not os.path.exists(dir_path_content):
        raise ValueError("Invalid source directory")
    if not os.path.isdir(dir_path_content):
        raise ValueError("dir_path_content should be the path to a directory")

    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)

    dir_path_content_list: list[str] = os.listdir(dir_path_content)
    for item in dir_path_content_list:
        item_path: str = os.path.join(dir_path_content, item)
        item_dest_path: str = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path) and item_path[-3:] == ".md":
            print(f"index.md file found at {item_path}")
            item_dest_path_html: str = item_dest_path.replace(".md", ".html")
            generate_page(item_path, "template.html", item_dest_path_html)
        elif os.path.isdir(item_path):
            print(f"dir found at {item_path}")
            generate_page_recursive(item_path, "template.html", item_dest_path)
        else:
            print("\n\nPROBLEM WITH THIS ITEM:", item_path)
            raise ValueError(f"Invalid file type found in {dir_path_content}")
