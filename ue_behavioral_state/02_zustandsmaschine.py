"""
Übung 2 - Zustandsmaschine

In dieser Übung wird eine einfache Zustandsmaschine erstellt, die zwischen verschiedenen Zuständen wechseln kann.

Implementieren Sie die Klassen 'State', 'StateA', 'StateB', 'StateC' und 'StateMachine'.
"""


class State:
    pass


class StateA(State):
    pass


class StateB(State):
    pass


class StateC(State):
    pass


class StateMachine:
    pass


if __name__ == "__main__":
    machine = StateMachine()
    machine.set_state(StateA())
    machine.handle()
    machine.set_state(StateB())
    machine.handle()
    machine.set_state(StateC())
    machine.handle()