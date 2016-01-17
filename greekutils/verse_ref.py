from .booknames import SBL_SHORT


def bcv_to_verse_ref(bcv, scheme=SBL_SHORT, start=1, separator=":"):
    b = int(bcv[0:2]) - start
    c = int(bcv[2:4])
    v = int(bcv[4:6])
    return "{} {}{}{}".format(scheme[b], c, separator, v)
