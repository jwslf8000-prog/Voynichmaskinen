WEIGHTS = (5, 7, 9, 13, 21)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def t_row(N: int, weight: int):
    if (N + 1) % weight:
        return None
    k = (N + 1) // weight
    values = tuple(a * k - 1 for a in WEIGHTS)
    prime_flags = tuple(is_prime(x) for x in values)
    return {
        "weight": weight,
        "k": k,
        "values": values,
        "prime_flags": prime_flags,
        "score": sum(prime_flags),
    }

def pkt_profile(N: int):
    rows = tuple(t_row(N, w) for w in WEIGHTS)
    profile = tuple(0 if r is None else r["score"] for r in rows)
    return profile, sum(profile), rows

if __name__ == "__main__":
    profile, strength, rows = pkt_profile(49139)
    assert profile == (2, 4, 5, 5, 3), profile
    assert strength == 19, strength
    assert rows[2]["values"] == (27299,38219,49139,70979,114659)
    assert rows[3]["values"] == (18899,26459,34019,49139,79379)
    print("PKT control OK:", profile, strength)
