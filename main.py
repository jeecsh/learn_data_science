def fbonatch(N):
    sequence = []
    a, b = 0, 1
    for i in range(N):
        c = a + b
        sequence.append(c)
        a = b
        b = c
    return sequence
