"""
Übung 2 - Backrezepte

Das Template-Methoden-Muster kann verwendet werden, um ein allgemeines Backrezept zu erstellen und
die genauen Schritte in den Unterklassen zu definieren.

Implementieren Sie die Klassen 'BakingRecipe', 'CookieRecipe' und 'CakeRecipe'.
"""


class BakingRecipe:
    pass


class CookieRecipe(BakingRecipe):
    pass


class CakeRecipe(BakingRecipe):
    pass


if __name__ == "__main__":
    cookie_recipe = CookieRecipe()
    cookie_recipe.bake()
    cake_recipe = CakeRecipe()
    cake_recipe.bake()