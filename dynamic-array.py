def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    result = []

    for query in queries:
        q_type, x, y = query
        idx = (x ^ last_answer) % n

        if q_type == 1:
            seq_list[idx].append(y)
        elif q_type == 2:
            value = seq_list[idx][y % len(seq_list[idx])]
            last_answer = value
            result.append(last_answer)

    return result
