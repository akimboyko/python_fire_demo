import fire


def hello_world(name):
    return f"Hello {name}!"


def salut_le_monde(name):
    return f"Salut le monde, c'est moi {name}!"


def ça_va(prenom):
    return f"Salut {prenom}, ça va?"


if __name__ == "__main__":
    fire.Fire({
        "hello_world": hello_world,
        "salut_le_monde": salut_le_monde
    })
