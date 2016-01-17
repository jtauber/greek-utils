def trigrams(it):

    prev_2 = None
    prev_1 = None

    for current in it:
        if prev_1 is not None:
            yield prev_2, prev_1, current

        prev_2 = prev_1
        prev_1 = current

    yield prev_2, prev_1, None
