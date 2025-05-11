
"""36) Napište program, ve kterém naplníte množinu planety jmény několika planet naší sluneční soustavy. Na objektu
planety vyzkoušejte několik metod, které Python nabízí pro práci s množinami (přidání jednoho prvku k množině, přidání
více prvků k množině, odstranění prvku z množiny, zjištění počtu prvků množiny, stanovení, zda prvek leží v množině)."""

"""37) Naplňte jmény zvířat množiny ZOO_Brno a ZOO_Praha. Na ně aplikujte operace průniku, sjednocení a rozdílu množin."""
zoo_prague = {"panda",    "meerkat",    "penguin",    "ostrich",    "crocodile",    "lemur",    "peacock"}
zoo_brno = {   "elephant",    "giraffe",    "meerkat",    "lion",    "peacock",    "kangaroo",}
print(f"Průnik: {zoo_brno & zoo_prague} \n"
      f"Sjednocení: {zoo_brno | zoo_prague} \n"
      f"Rozdíl: {zoo_brno ^ zoo_prague} \n")
