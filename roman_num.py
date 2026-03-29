import sys, argparse

VALS = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
        (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

def to_roman(n):
    if n <= 0 or n > 3999:
        return "?"
    r = []
    for v, s in VALS:
        while n >= v:
            r.append(s)
            n -= v
    return "".join(r)

def from_roman(s):
    rmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    for i, c in enumerate(s.upper()):
        v = rmap.get(c, 0)
        if i + 1 < len(s) and v < rmap.get(s[i+1].upper(), 0):
            total -= v
        else:
            total += v
    return total

def main():
    p = argparse.ArgumentParser(description="Roman numeral converter")
    p.add_argument("action", choices=["encode", "decode"])
    p.add_argument("value")
    args = p.parse_args()
    if args.action == "encode":
        print(to_roman(int(args.value)))
    else:
        print(from_roman(args.value))

if __name__ == "__main__":
    main()
