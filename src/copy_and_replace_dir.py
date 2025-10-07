import os
import shutil


def copy_and_replace_dir(source: str = "static", destination: str = "public") -> None:
    if not os.path.exists(source):
        raise ValueError("Invalid source directory")

    # reset destination content
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)

    # copy tree
    source_dir_content: list[str] = os.listdir(source)
    for item in source_dir_content:
        item_path: str = os.path.join(source, item)
        if os.path.isfile(item_path):
            shutil.copy(src=item_path, dst=destination)
        else:
            destination_path: str = os.path.join(destination, item)
            copy_and_replace_dir(source=item_path, destination=destination_path)
