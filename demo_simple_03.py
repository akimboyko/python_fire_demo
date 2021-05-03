import fire


def hello_world(name):
    return f"Hello, {name}!"


def salut_le_monde(prenom):
    return f"Salut le monde, c'est moi {prenom}!"


def _ça_va(prenom):
    return f"Salut {prenom}, ça va?"


if __name__ == "__main__":
    fire.Fire()
