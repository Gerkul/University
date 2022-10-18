def deg_to_gms(deg, formats='string'):
    d = int(deg)
    m = int((deg - d) * 60)
    s = int(((deg - d) * 60 - m) * 60)

    if format == "string":
        return f"{d}° {m}′ {s}″"
    else:
        return d, m, s


def gms_to_deg(d, m, s):
    m = m / 60
    s = (m + s) / 60

    return d + m + s


def deg_to_rad(deg):
    rad = deg * (3.14 / 180)
    return rad


def rad_to_deg(rad):
    deg = rad * (180 / 3.14)
    return deg


print(deg_to_gms(36.97))
dms = deg_to_gms(36.97)
print(gms_to_deg(dms[0], dms[1], dms[2]))
print(deg_to_rad(10))
print(rad_to_deg(deg_to_rad(10)))