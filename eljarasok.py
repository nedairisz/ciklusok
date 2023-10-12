
def hanyados(a: int=1, b: int=1):
    if b==0:
        print("0-val nem lehet osztani!")
    else:
        # eredmeny = int(szam1 / szam2)
        c: float = a / b
        print(f"{a} / {b} = {c:.2f}")

