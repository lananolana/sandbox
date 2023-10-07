import math


def make(numer, denom):
    """
    Takes a numerator and a denominator as input and returns a fraction
    """
    gcd = math.gcd(numer, denom)
    return {
        "numer": int(numer / gcd),
        "denom": int(denom / gcd),
    }


def get_numer(rat):
    """
    Selector returns numerator
    """
    return rat["numer"]


def get_denom(rat):
    """
    Selector returns denominator
    """
    return rat["denom"]


def add(rat1, rat2):
    """
    Summation adds the given fractions
    """
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def sub(rat1, rat2):
    """
    Subtraction finds the difference between two fractions
    """
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )


def to_str(rat):
    """
    Returns a string representation of a number (for debugging)
    """
    return f"{get_numer(rat)}/{get_denom(rat)}"
