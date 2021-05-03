import fire


class PhrasesGenerator():
    def __init__(self, smile="ツ"):
        self._smile = smile

    def hello_world(self, name):
        print(f"Hello {name}! {self._smile}")
        return self

    def salut_le_monde(self, name):
        print(f"Salut le monde, c\'est moi {name}! {self._smile}")
        return self

    def ça_va(self, prenom):
        print(f"Salut {prenom}, ça va? {self._smile}")
        return self

    def farwell_everyone(self):
        print("Farewell everyone")
        return self

    def adieu_le_monde(self):
        print("Adieu tout le monde")
        return self

    def end_here(self):
        pass


if __name__ == "__main__":
    fire.Fire(PhrasesGenerator)
