def tally():
    score = 0
    while True:
        inc = yield score
        score += inc
