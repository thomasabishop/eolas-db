import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="eolas-db", description="Eolas database manager."
    )
    parser.add_argument("command", choices=["parse"], help="Command to execute")
    parser.add_argument("--path", help="Path to Zettelkasten directory")
    args = parser.parse_args()

    print("Welcome to eolas-db")

    if args.command == "parse":
        pass


if __name__ == "__main__":
    main()
