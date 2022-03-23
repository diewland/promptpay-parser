if __name__ == "__main__":

    from pprint import pprint as pp
    from parser import parse

    sample = (
        "00020101021129370016A000000677010111011300668912345675303764540599.995802TH630459F8",
    )

    for s in sample:
        obj = parse(s)
        print(s)
        pp(obj)
