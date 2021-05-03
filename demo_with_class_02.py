import fire


class GreetingsGenerator():
    def __init__(self, smile="ツ"):
        self._smile = smile

    def hello_world(self, name):
        return f"Hello {name}! {self._smile}"

    def salut_le_monde(self, name):
        return f"Salut le monde, c\'est moi {name}! {self._smile}"

    def ça_va(self, prenom):
        return f"Salut {prenom}, ça va? {self._smile}"


class FarwellGenerator():
    def farwell_everyone(self):
        return "Farewell everyone"

    def adieu_le_monde(self):
        return "Adieu tout le monde"


class Pipeline():
    def __init__(self, smile="ツ"):
        self.greetings = GreetingsGenerator(smile=smile)
        self.farwell = FarwellGenerator()


if __name__ == "__main__":
    fire.Fire(Pipeline)
