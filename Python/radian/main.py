


def deg_to_gms(deg: int) -> str:
    """
    deg to gms
    :param deg: decimal degrees
    :return: degrees, minutes, seconds
    """

    grad: int = int(deg)
    minutes_ost: int = (deg - grad) * 60
    minutes: int = int(minutes_ost)
    seconds: int = round((minutes_ost - minutes) * 60, 5)

    return f'{grad}° {minutes}` {seconds}"'


def deg_to_rad(deg: int) -> float:
    """
    deg to rad
    :param deg: decimal degrees
    :return: radians
    """
    return (3.14 / 180) * deg


def gms_to_deg(degrees: int, minutes: int, seconds: int) -> float:
    """
    gms to deg
    :param degrees: str degrees with special symbol
    :param minutes: str minutes with special symbol
    :param seconds: str seconds with special symbol
    :return: decimal
    """
    res = int(degrees[:2]) + (int(minutes[:2]) / 60) + (int(seconds[:2]) / 3600)

    return res


def rad_to_deg(rad: int) -> float:
    """
    rad to deg
    :param rad: radians
    :return: decimal decrees
    """
    return (180 / 3.14) * rad



