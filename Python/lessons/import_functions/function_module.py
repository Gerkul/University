def deg_to_gms(deg, formats='string'):
    """
    The function returns deg, min, sec
    :param deg: degrees
    :param formats: returns str format
    :return: deg, min, sec
    """

    d = int(deg)
    m = int((deg - d) * 60)
    s = int(((deg - d) * 60 - m) * 60)

    if formats == "string":
        return f"{d}° {m}′ {s}″"
    else:
        return d, m, s


def gms_to_deg(d, m, s):
    """
    Returns degree
    :param d:
    :param m:
    :param s:
    :return: d + m + s
    """
    m = m / 60
    s = s / 3600

    return d + m + s


def deg_to_rad(deg):
    """
    Returns rad
    :param deg:
    :return: rad
    """
    rad = deg * (3.14 / 180)
    return rad


def rad_to_deg(rad):
    """
    Returns degrees
    :param rad:
    :return: deg
    """
    deg = rad * (180 / 3.14)
    return deg


print(deg_to_gms(36.97, 1))
dms = deg_to_gms(36.97, 1)
print(gms_to_deg(dms[0], dms[1], dms[2]))
print(deg_to_rad(10))
print(rad_to_deg(deg_to_rad(10)))