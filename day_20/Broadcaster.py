class Broadcaster:
    def __init__(self):
        self.outputs = []

    def register_outputs(self, outputs: list[str]):
        self.outputs = outputs

    def __repr__(self):
        return f'Broadcaster'