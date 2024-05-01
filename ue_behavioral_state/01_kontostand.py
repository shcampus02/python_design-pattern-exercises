"""
Übung 1 - Kontostand

In dieser Übung wird das State-Muster verwendet, um den Zustand eines Bankkontos zu verwalten.
Ein Konto kann sich in verschiedenen Zuständen befinden, z.B. positiver Saldo, 0 Saldo oder negativer Saldo.

Implementieren Sie die Klassen 'AccountState', 'PositiveBalanceState', 'ZeroBalanceState', 'NegativeBalanceState' und 'Account'.
"""


class AccountState:
    pass


class PositiveBalanceState(AccountState):
    pass


class ZeroBalanceState(AccountState):
    pass


class NegativeBalanceState(AccountState):
    pass


class Account:
    pass


if __name__ == "__main__":
    account = Account(1000)
    print(account.get_state())  # Output: PositiveBalanceState
    account.withdraw(1000)
    print(account.get_state())  # Output: ZeroBalanceState
    account.withdraw(10)
    print(account.get_state())  # Output: NegativeBalanceState