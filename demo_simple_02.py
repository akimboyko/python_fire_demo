import fire


def hello_world(name, smile="ツ"):
    """Let's say hello to someone and add a smile
    args:
        name: someone's name
        smile: optional smile to add to the message

    """
    return f"Hello, {name}! {smile}"


if __name__ == "__main__":
    fire.Fire(hello_world)
