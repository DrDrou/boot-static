import os
from .extract_title import extract_title
from .markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"\nGenerating page from {from_path} to {dest_path} using {template_path}")

    if os.path.exists(from_path):
        with open(from_path, "r") as f:
            md: str = f.read()
    else:
        raise ValueError("from_path does not exist")

    if os.path.exists(template_path):
        with open(template_path, "r") as f:
            template: str = f.read()
    else:
        raise ValueError("template_path does not exist")

    html_string: str = markdown_to_html_node(md).to_html()
    page_title: str = extract_title(md)

    updated_html: str = template.replace("{{ Title }}", page_title, 1).replace(
        "{{ Content }}", html_string, 1
    )

    # check destination path dir and create it if necessary
    dest_dir: str = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    # create the destination file
    with open(dest_path, "w") as f:
        f.write(updated_html)
        f.close()
