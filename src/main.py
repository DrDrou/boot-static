from copy_and_replace_dir import copy_and_replace_dir


def main() -> None:
    print("Initializing public directory...")
    copy_and_replace_dir(source="static", destination="public")
    print("Public directory initialized!\n")


if __name__ == "__main__":
    main()
