import fire


def hello_world(name: str, smile: str="ツ", exclamation: bool = False) -> str:
    """Let's say hello to someone and add a smile
    args:
        name: someone's name
        smile: optional smile to add to the message
        exclamation: add an exclamation mark

    """
    return f"Hello, {name}{'!' if exclamation else ''} {smile}"


if __name__ == "__main__":
    fire.Fire(hello_world)
