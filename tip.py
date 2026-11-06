def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):
    p = p.replace("%", "")
    return float(p) / 100

dollars = dollars_to_float(input("Bữa ăn của bạn bao nhiêu:  "))
percent = percent_to_float(input("Tip tối thiểu bạn cần tip:  "))
tip = dollars * percent
print(f"Tip ${tip:.2f}")
