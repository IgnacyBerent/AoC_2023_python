class FlipFlop:
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.on = False
        self.outputs = outputs
        self._signal = None
        self.last_signal = None

    def receive(self, signal: str):
        if signal == 'low':
            self.on = not self.on
            if self.on:
                self._signal = 'high'
            else:
                self._signal = 'low'

    def send(self):
        if self._signal is not None:
            self.last_signal = self._signal

        sig = self._signal
        self._signal = None
        return sig

    def __repr__(self):
        return f'{self.name}'