from mahjong_engine import generate_combinations, write_workbook

hands = []

def add(hand_id, groups, suit_constraints=None, value_vars=None):
    hands.append({
        'hand_id': hand_id,
        'groups': groups,
        'suit_constraints': suit_constraints or {},
        'value_vars': value_vars or {},
    })

def same(size, tile_type, suit=None, value=None, wind=None, allow_joker=None):
    g = {'kind': 'same', 'size': size, 'tile_type': tile_type}
    if suit is not None: g['suit'] = suit
    if value is not None: g['value'] = value
    if wind is not None: g['wind'] = wind
    if allow_joker is not None: g['allow_joker'] = allow_joker
    return g

def complement(domain, value_var, tile_type, suit=None):
    g = {'kind': 'complement_singles', 'domain': domain, 'value_var': value_var, 'tile_type': tile_type}
    if suit is not None: g['suit'] = suit
    return g

def digits_2026(suit):
    """The 4 loose singles making up '2026': 2,2(pair no-joker),0(dragon),6."""
    return [
        same(2, 'number', suit=suit, value=2),
        same(1, 'number', suit=suit, value=6),
        same(1, 'dragon', suit=suit),
    ]

# =====================================================================
# 2026 HANDS
# =====================================================================

# 1. 222 (suit1) 000 2222 (suit2) 6666 (suit2) -- any 2 suits
add('2026-1: 222 000 2222 6666',
    [
        same(3, 'number', suit='A', value=2),
        same(3, 'dragon', suit='Dot'),
        same(4, 'number', suit='B', value=2),
        same(4, 'number', suit='B', value=6),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 2. 2026 (suit1) DDD (suit1) 2222 (suit2) DDD (suit2) -- 2 suits, matching dragons, kong 2 or 6
add('2026-2: 2026 DDD 2222 DDD',
    digits_2026('A') + [
        same(3, 'dragon', suit='A'),
        same(4, 'number', suit='B', value=[2, 6]),
        same(3, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 3. FFF 2026 (suit1) 222 (suit2) 6666 (suit3) -- any 3 suits
add('2026-3: FFF 2026 222 6666',
    [same(3, 'flower')] +
    digits_2026('A') + [
        same(3, 'number', suit='B', value=2),
        same(4, 'number', suit='C', value=6),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 4. 22 (s1) 00 222 666 (s2) NEWS -- any 2 suits (00 is always white dragon, fixed suit)
add('2026-4: 22 00 222 666 NEWS',
    [
        same(2, 'number', suit='A', value=2),
        same(2, 'dragon', suit='Dot'),
        same(3, 'number', suit='B', value=2),
        same(3, 'number', suit='B', value=6),
        same(1, 'wind', wind='North'),
        same(1, 'wind', wind='East'),
        same(1, 'wind', wind='West'),
        same(1, 'wind', wind='South'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# =====================================================================
# EVENS
# =====================================================================

# 1. 222 444 6666 8888 -- any 1 suit
add('Evens-1: 222 444 6666 8888 (1 suit)',
    [
        same(3, 'number', suit='A', value=2),
        same(3, 'number', suit='A', value=4),
        same(4, 'number', suit='A', value=6),
        same(4, 'number', suit='A', value=8),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 2. 222 444 (s1) 6666 8888 (s2) -- any 2 suits
add('Evens-2: 222 444 6666 8888 (2 suits)',
    [
        same(3, 'number', suit='A', value=2),
        same(3, 'number', suit='A', value=4),
        same(4, 'number', suit='B', value=6),
        same(4, 'number', suit='B', value=8),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 3. FF 2222 (s1) 44 66 (s2) 8888 (s1) -- any 2 suits
add('Evens-3: FF 2222 44 66 8888',
    [
        same(2, 'flower'),
        same(4, 'number', suit='A', value=2),
        same(2, 'number', suit='B', value=4),
        same(2, 'number', suit='B', value=6),
        same(4, 'number', suit='A', value=8),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 4. EE 22 444 666 88 WW -- any 1 suit, east and west only
add('Evens-4: EE 22 444 666 88 WW',
    [
        same(2, 'wind', wind='East'),
        same(2, 'number', suit='A', value=2),
        same(3, 'number', suit='A', value=4),
        same(3, 'number', suit='A', value=6),
        same(2, 'number', suit='A', value=8),
        same(2, 'wind', wind='West'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 5. 2222 (s1) DDD (s1) 8888 (s2) DDD (s2) -- 2 suits, matching dragons, these numbers only
add('Evens-5: 2222 DDD 8888 DDD',
    [
        same(4, 'number', suit='A', value=2),
        same(3, 'dragon', suit='A'),
        same(4, 'number', suit='B', value=8),
        same(3, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 6. FFF 22 44 666 8888 -- any 1 suit
add('Evens-6: FFF 22 44 666 8888',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=2),
        same(2, 'number', suit='A', value=4),
        same(3, 'number', suit='A', value=6),
        same(4, 'number', suit='A', value=8),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 7. 2468 (s1) 2222 (s2) D (s2) 2222 (s3) D (s3) -- 3 suits, both kongs MATCH (same value, from 2/4/6/8), matching dragons
add('Evens-7: 2468 2222 D 2222 D',
    [
        same(1, 'number', suit='A', value=2),
        same(1, 'number', suit='A', value=4),
        same(1, 'number', suit='A', value=6),
        same(1, 'number', suit='A', value=8),
        same(4, 'number', suit='B', value='K'),
        same(1, 'dragon', suit='B'),
        same(4, 'number', suit='C', value='K'),
        same(1, 'dragon', suit='C'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'K': [2, 4, 6, 8]})

# 8. FFF 2468 (s1) FFF 2222 (s2) -- any 2 suits, kong 2,4,6, or 8
add('Evens-8: FFF 2468 FFF 2222',
    [
        same(3, 'flower'),
        same(1, 'number', suit='A', value=2),
        same(1, 'number', suit='A', value=4),
        same(1, 'number', suit='A', value=6),
        same(1, 'number', suit='A', value=8),
        same(3, 'flower'),
        same(4, 'number', suit='B', value=[2, 4, 6, 8]),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 9. FF 246 (s1) 888 (s1) 246 (s2) 888 (s2) -- any 2 suits
add('Evens-9: FF 246 888 246 888',
    [
        same(2, 'flower'),
        same(1, 'number', suit='A', value=2),
        same(1, 'number', suit='A', value=4),
        same(1, 'number', suit='A', value=6),
        same(3, 'number', suit='A', value=8),
        same(1, 'number', suit='B', value=2),
        same(1, 'number', suit='B', value=4),
        same(1, 'number', suit='B', value=6),
        same(3, 'number', suit='B', value=8),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# =====================================================================
# ANY LIKE NUMBERS
# =====================================================================

# 1. 1111 (s1) FFFFFF 1111 (s2) -- any 2 suits, any like number
add('AnyLike-1: 1111 FFFFFF 1111',
    [
        same(4, 'number', suit='A', value='V'),
        same(6, 'flower'),
        same(4, 'number', suit='B', value='V'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'V': list(range(1, 10))})

# 2. 1111 (s1) D (s1) 111 (s2) D (s2) 1111 (s3) D (s3) -- 3 suits, matching dragons, any like number
add('AnyLike-2: 1111 D 111 D 1111 D',
    [
        same(4, 'number', suit='A', value='V'),
        same(1, 'dragon', suit='A'),
        same(3, 'number', suit='B', value='V'),
        same(1, 'dragon', suit='B'),
        same(4, 'number', suit='C', value='V'),
        same(1, 'dragon', suit='C'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'V': list(range(1, 10))})

# 3. FF 1111 (s1) 11 (s2) 1111 (s3) DD (any of s1/s2/s3) -- 3 suits, any dragon, any like number
add('AnyLike-3: FF 1111 11 1111 DD',
    [
        same(2, 'flower'),
        same(4, 'number', suit='A', value='V'),
        same(2, 'number', suit='B', value='V'),
        same(4, 'number', suit='C', value='V'),
        same(2, 'dragon', suit=['A', 'B', 'C']),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'V': list(range(1, 10))})

# =====================================================================
# QUINTS
# =====================================================================

# 1. 11111 (s1) 1111 (s2) 11111 (s3) -- any 3 suits, any like number
add('Quints-1: 11111 1111 11111',
    [
        same(5, 'number', suit='A', value='V'),
        same(4, 'number', suit='B', value='V'),
        same(5, 'number', suit='C', value='V'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'V': list(range(1, 10))})

# 2. FF 11111 (s1) 22 (s1) 33333 (s1) -- any 1 suit, any 3 consecutive numbers
add('Quints-2: FF 11111 22 33333',
    [
        same(2, 'flower'),
        same(5, 'number', suit='A', value=('offset', 'S', 0)),
        same(2, 'number', suit='A', value=('offset', 'S', 1)),
        same(5, 'number', suit='A', value=('offset', 'S', 2)),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 8))})  # start 1..7 so start+2 <= 9

# 3. 11111 (s1) 44444 (s1) DDDD (s2) -- any 2 (distinct) numbers in 1 suit, opposite dragon
add('Quints-3: 11111 44444 DDDD',
    [
        same(5, 'number', suit='A', value='V1'),
        same(5, 'number', suit='A', value='V2'),
        same(4, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'V1': list(range(1, 10)), 'V2': list(range(1, 10))})

# =====================================================================
# CONSECUTIVE RUNS
# =====================================================================

# 1. 11 222 33 444 5555 -- any 1 suit, these numbers only (fixed 1-5)
add('Runs-1: 11 222 33 444 5555',
    [
        same(2, 'number', suit='A', value=1),
        same(3, 'number', suit='A', value=2),
        same(2, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=4),
        same(4, 'number', suit='A', value=5),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 2. 55 666 77 888 9999 -- any 1 suit, these numbers only (fixed 5-9)
add('Runs-2: 55 666 77 888 9999',
    [
        same(2, 'number', suit='A', value=5),
        same(3, 'number', suit='A', value=6),
        same(2, 'number', suit='A', value=7),
        same(3, 'number', suit='A', value=8),
        same(4, 'number', suit='A', value=9),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 3. FFF 1111 234 5555 -- any 1 suit, any 5 consecutive numbers
add('Runs-3: FFF 1111 234 5555',
    [
        same(3, 'flower'),
        same(4, 'number', suit='A', value=('offset', 'S', 0)),
        same(1, 'number', suit='A', value=('offset', 'S', 1)),
        same(1, 'number', suit='A', value=('offset', 'S', 2)),
        same(1, 'number', suit='A', value=('offset', 'S', 3)),
        same(4, 'number', suit='A', value=('offset', 'S', 4)),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 6))})  # start+4<=9 -> start<=5

# 4. FFF 1111 (s1) 234 (s2) 5555 (s1) -- any 2 suits, any 5 consecutive numbers
add('Runs-4: FFF 1111 234 5555 (2 suits)',
    [
        same(3, 'flower'),
        same(4, 'number', suit='A', value=('offset', 'S', 0)),
        same(1, 'number', suit='B', value=('offset', 'S', 1)),
        same(1, 'number', suit='B', value=('offset', 'S', 2)),
        same(1, 'number', suit='B', value=('offset', 'S', 3)),
        same(4, 'number', suit='A', value=('offset', 'S', 4)),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'S': list(range(1, 6))})

# 5. 11 22 (s1) 111 222 (s2) 3333 (s3) -- any 3 suits, any 3 consecutive
add('Runs-5: 11 22 111 222 3333',
    [
        same(2, 'number', suit='A', value=('offset', 'S', 0)),
        same(2, 'number', suit='A', value=('offset', 'S', 1)),
        same(3, 'number', suit='B', value=('offset', 'S', 0)),
        same(3, 'number', suit='B', value=('offset', 'S', 1)),
        same(4, 'number', suit='C', value=('offset', 'S', 2)),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'S': list(range(1, 8))})

# 6. 111 222 3333 4444 -- any 1 suit, any 4 consecutive
add('Runs-6: 111 222 3333 4444',
    [
        same(3, 'number', suit='A', value=('offset', 'S', 0)),
        same(3, 'number', suit='A', value=('offset', 'S', 1)),
        same(4, 'number', suit='A', value=('offset', 'S', 2)),
        same(4, 'number', suit='A', value=('offset', 'S', 3)),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 7))})

# 7. 111 222 (s1) 3333 4444 (s2) -- any 2 suits, any 4 consecutive
add('Runs-7: 111 222 3333 4444 (2 suits)',
    [
        same(3, 'number', suit='A', value=('offset', 'S', 0)),
        same(3, 'number', suit='A', value=('offset', 'S', 1)),
        same(4, 'number', suit='B', value=('offset', 'S', 2)),
        same(4, 'number', suit='B', value=('offset', 'S', 3)),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'S': list(range(1, 7))})

# 8. FFF 11 22 333 DDDD -- any 1 suit, any consecutive run (length 3)
add('Runs-8: FFF 11 22 333 DDDD',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=('offset', 'S', 0)),
        same(2, 'number', suit='A', value=('offset', 'S', 1)),
        same(3, 'number', suit='A', value=('offset', 'S', 2)),
        same(4, 'dragon', suit='A'),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 8))})

# 9. FFF 11 (s1) 22 (s2) 333 (s1) DDDD (s2) -- any 2 suits, any consecutive run
add('Runs-9: FFF 11 22 333 DDDD (2 suits)',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=('offset', 'S', 0)),
        same(2, 'number', suit='B', value=('offset', 'S', 1)),
        same(3, 'number', suit='A', value=('offset', 'S', 2)),
        same(4, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'S': list(range(1, 8))})

# 10. 1111 FFFFFF 2222 -- any 1 suit, any 2 consecutive
add('Runs-10: 1111 FFFFFF 2222',
    [
        same(4, 'number', suit='A', value=('offset', 'S', 0)),
        same(6, 'flower'),
        same(4, 'number', suit='A', value=('offset', 'S', 1)),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 9))})

# 11. FF 1111 2222 3333 -- any 1 suit, any 3 consecutive
add('Runs-11: FF 1111 2222 3333',
    [
        same(2, 'flower'),
        same(4, 'number', suit='A', value=('offset', 'S', 0)),
        same(4, 'number', suit='A', value=('offset', 'S', 1)),
        same(4, 'number', suit='A', value=('offset', 'S', 2)),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 8))})

# 12. FF 1111 (s1) 2222 (s2) 3333 (s3) -- any 3 suits, any 3 consecutive
add('Runs-12: FF 1111 2222 3333 (3 suits)',
    [
        same(2, 'flower'),
        same(4, 'number', suit='A', value=('offset', 'S', 0)),
        same(4, 'number', suit='B', value=('offset', 'S', 1)),
        same(4, 'number', suit='C', value=('offset', 'S', 2)),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'S': list(range(1, 8))})

# 13. 1 22 333 (s1) 1 22 333 (s2) 44 (s3) -- any 3 suits, any 4 consecutive
add('Runs-13: 1 22 333 / 1 22 333 / 44',
    [
        same(1, 'number', suit='A', value=('offset', 'S', 0)),
        same(2, 'number', suit='A', value=('offset', 'S', 1)),
        same(3, 'number', suit='A', value=('offset', 'S', 2)),
        same(1, 'number', suit='B', value=('offset', 'S', 0)),
        same(2, 'number', suit='B', value=('offset', 'S', 1)),
        same(3, 'number', suit='B', value=('offset', 'S', 2)),
        same(2, 'number', suit='C', value=('offset', 'S', 3)),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'S': list(range(1, 7))})

# =====================================================================
# ODDS
# =====================================================================

# 1. 11 333 55 777 9999 -- any 1 suit
add('Odds-1: 11 333 55 777 9999',
    [
        same(2, 'number', suit='A', value=1),
        same(3, 'number', suit='A', value=3),
        same(2, 'number', suit='A', value=5),
        same(3, 'number', suit='A', value=7),
        same(4, 'number', suit='A', value=9),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 2. 11 333 (s1) 55 777 (s2) 9999 (s3) -- any 3 suits
add('Odds-2: 11 333 55 777 9999 (3 suits)',
    [
        same(2, 'number', suit='A', value=1),
        same(3, 'number', suit='A', value=3),
        same(2, 'number', suit='B', value=5),
        same(3, 'number', suit='B', value=7),
        same(4, 'number', suit='C', value=9),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 3. 111 333 (s1) 3333 5555 (s2) -- any 2 suits
add('Odds-3: 111 333 3333 5555',
    [
        same(3, 'number', suit='A', value=1),
        same(3, 'number', suit='A', value=3),
        same(4, 'number', suit='B', value=3),
        same(4, 'number', suit='B', value=5),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 4. 555 777 (s1) 7777 9999 (s2) -- any 2 suits
add('Odds-4: 555 777 7777 9999',
    [
        same(3, 'number', suit='A', value=5),
        same(3, 'number', suit='A', value=7),
        same(4, 'number', suit='B', value=7),
        same(4, 'number', suit='B', value=9),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 5. NN 1111 33 5555 SS -- any 1 suit, north/south only
add('Odds-5: NN 1111 33 5555 SS',
    [
        same(2, 'wind', wind='North'),
        same(4, 'number', suit='A', value=1),
        same(2, 'number', suit='A', value=3),
        same(4, 'number', suit='A', value=5),
        same(2, 'wind', wind='South'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 6. NN 5555 77 9999 SS -- any 1 suit, north/south only
add('Odds-6: NN 5555 77 9999 SS',
    [
        same(2, 'wind', wind='North'),
        same(4, 'number', suit='A', value=5),
        same(2, 'number', suit='A', value=7),
        same(4, 'number', suit='A', value=9),
        same(2, 'wind', wind='South'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 7. 113579 (s1, pair any odd + complement singles) 1111 (s2, =pair) 1111 (s3, =pair) -- 3 suits
add('Odds-7: 113579 1111 1111',
    [
        same(2, 'number', suit='A', value='V'),
        complement([1, 3, 5, 7, 9], 'V', 'number', suit='A'),
        same(4, 'number', suit='B', value='V'),
        same(4, 'number', suit='C', value='V'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'V': [1, 3, 5, 7, 9]})

# 8. FFF 11 33 555 DDDD -- any 1 suit with matching dragon
add('Odds-8: FFF 11 33 555 DDDD',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=1),
        same(2, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=5),
        same(4, 'dragon', suit='A'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 9. FFF 55 77 999 DDDD -- any 1 suit with matching dragon
add('Odds-9: FFF 55 77 999 DDDD',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=5),
        same(2, 'number', suit='A', value=7),
        same(3, 'number', suit='A', value=9),
        same(4, 'dragon', suit='A'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 10. 11 33 (s1) 111 333 (s2) 5555 (s3) -- any 3 suits
add('Odds-10: 11 33 111 333 5555',
    [
        same(2, 'number', suit='A', value=1),
        same(2, 'number', suit='A', value=3),
        same(3, 'number', suit='B', value=1),
        same(3, 'number', suit='B', value=3),
        same(4, 'number', suit='C', value=5),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 11. 55 77 (s1) 555 777 (s2) 9999 (s3) -- any 3 suits
add('Odds-11: 55 77 555 777 9999',
    [
        same(2, 'number', suit='A', value=5),
        same(2, 'number', suit='A', value=7),
        same(3, 'number', suit='B', value=5),
        same(3, 'number', suit='B', value=7),
        same(4, 'number', suit='C', value=9),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 12. 1111 33 55 77 9999 -- any 1 suit
add('Odds-12: 1111 33 55 77 9999',
    [
        same(4, 'number', suit='A', value=1),
        same(2, 'number', suit='A', value=3),
        same(2, 'number', suit='A', value=5),
        same(2, 'number', suit='A', value=7),
        same(4, 'number', suit='A', value=9),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 13. 1111 (s1) 33 55 77 (s2) 9999 (s1) -- any 2 suits
add('Odds-13: 1111 33 55 77 9999 (2 suits)',
    [
        same(4, 'number', suit='A', value=1),
        same(2, 'number', suit='B', value=3),
        same(2, 'number', suit='B', value=5),
        same(2, 'number', suit='B', value=7),
        same(4, 'number', suit='A', value=9),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 14. FF 11 33 55 (s1) 111 (s2) 111 (s3) -- any 3 suits, these numbers only
add('Odds-14: FF 11 33 55 111 111',
    [
        same(2, 'flower'),
        same(2, 'number', suit='A', value=1),
        same(2, 'number', suit='A', value=3),
        same(2, 'number', suit='A', value=5),
        same(3, 'number', suit='B', value=1),
        same(3, 'number', suit='C', value=1),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 15. FF 55 77 99 (s1) 555 (s2) 555 (s3) -- any 3 suits, these numbers only
add('Odds-15: FF 55 77 99 555 555',
    [
        same(2, 'flower'),
        same(2, 'number', suit='A', value=5),
        same(2, 'number', suit='A', value=7),
        same(2, 'number', suit='A', value=9),
        same(3, 'number', suit='B', value=5),
        same(3, 'number', suit='C', value=5),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 16. FF 135 777 999 (s1) DDD (s2) -- any 1 suit with opposite dragon
add('Odds-16: FF 135 777 999 DDD',
    [
        same(2, 'flower'),
        same(1, 'number', suit='A', value=1),
        same(1, 'number', suit='A', value=3),
        same(1, 'number', suit='A', value=5),
        same(3, 'number', suit='A', value=7),
        same(3, 'number', suit='A', value=9),
        same(3, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# =====================================================================
# WINDS AND DRAGONS
# =====================================================================

# 1. NNNN EEE WWW SSSS
add('WD-1: NNNN EEE WWW SSSS',
    [
        same(4, 'wind', wind='North'),
        same(3, 'wind', wind='East'),
        same(3, 'wind', wind='West'),
        same(4, 'wind', wind='South'),
    ])

# 2. NNN EEEE WWWW SSS
add('WD-2: NNN EEEE WWWW SSS',
    [
        same(3, 'wind', wind='North'),
        same(4, 'wind', wind='East'),
        same(4, 'wind', wind='West'),
        same(3, 'wind', wind='South'),
    ])

# 3. 1234 (s1) DDD (s2) DDD (s3) DDDD (s1) -- 4 consecutive in 1 suit, 3 suits total
add('WD-3: 1234 DDD DDD DDDD',
    [
        same(1, 'number', suit='A', value=('offset', 'S', 0)),
        same(1, 'number', suit='A', value=('offset', 'S', 1)),
        same(1, 'number', suit='A', value=('offset', 'S', 2)),
        same(1, 'number', suit='A', value=('offset', 'S', 3)),
        same(3, 'dragon', suit='B'),
        same(3, 'dragon', suit='C'),
        same(4, 'dragon', suit='A'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'S': list(range(1, 7))})

# 4. NNN 1111 (s1) 1111 (s2) SSS -- any like odd numbers in any 2 suits
add('WD-4: NNN 1111 1111 SSS',
    [
        same(3, 'wind', wind='North'),
        same(4, 'number', suit='A', value='V'),
        same(4, 'number', suit='B', value='V'),
        same(3, 'wind', wind='South'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'V': [1, 3, 5, 7, 9]})

# 5. EEE 2222 (s1) 2222 (s2) WWW -- any like even numbers in any 2 suits
add('WD-5: EEE 2222 2222 WWW',
    [
        same(3, 'wind', wind='East'),
        same(4, 'number', suit='A', value='V'),
        same(4, 'number', suit='B', value='V'),
        same(3, 'wind', wind='West'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2},
    {'V': [2, 4, 6, 8]})

# 6. FFF NNNN FFF DDDD -- any wind, any dragon
add('WD-6: FFF NNNN FFF DDDD',
    [
        same(3, 'flower'),
        same(4, 'wind', wind=['North', 'East', 'South', 'West']),
        same(3, 'flower'),
        same(4, 'dragon', suit='D'),
    ],
    {'vars': ['D'], 'distinct_count': None})

# 7. 1 N 2 EE 3 WWW 4 SSSS -- any 1 suit, these numbers only
add('WD-7: 1 N 2 EE 3 WWW 4 SSSS',
    [
        same(1, 'number', suit='A', value=1),
        same(1, 'wind', wind='North'),
        same(1, 'number', suit='A', value=2),
        same(2, 'wind', wind='East'),
        same(1, 'number', suit='A', value=3),
        same(3, 'wind', wind='West'),
        same(1, 'number', suit='A', value=4),
        same(4, 'wind', wind='South'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 8. FF NNNN SSSS DD (s1) DD (s2) -- any 2 dragons
add('WD-8: FF NNNN SSSS DD DD',
    [
        same(2, 'flower'),
        same(4, 'wind', wind='North'),
        same(4, 'wind', wind='South'),
        same(2, 'dragon', suit='A'),
        same(2, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 9. FF EEEE WWWW DD (s1) DD (s2) -- any 2 dragons
add('WD-9: FF EEEE WWWW DD DD',
    [
        same(2, 'flower'),
        same(4, 'wind', wind='East'),
        same(4, 'wind', wind='West'),
        same(2, 'dragon', suit='A'),
        same(2, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 10. NN EEE 2026 (s1) WWW SS -- any 1 suit for 2026
add('WD-10: NN EEE 2026 WWW SS',
    [
        same(2, 'wind', wind='North'),
        same(3, 'wind', wind='East'),
    ] + digits_2026('A') + [
        same(3, 'wind', wind='West'),
        same(2, 'wind', wind='South'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# =====================================================================
# 369's
# =====================================================================

# 1. 333 666 (s1) 6666 9999 (s2) -- any 2 suits
add('369-1: 333 666 6666 9999',
    [
        same(3, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=6),
        same(4, 'number', suit='B', value=6),
        same(4, 'number', suit='B', value=9),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 2. 333 666 (s1) 6666 (s2) 9999 (s3) -- any 3 suits
add('369-2: 333 666 6666 9999 (3 suits)',
    [
        same(3, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=6),
        same(4, 'number', suit='B', value=6),
        same(4, 'number', suit='C', value=9),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 3. 33 66 (s1) 333 666 (s2) 9999 (s3) -- any 3 suits
add('369-3: 33 66 333 666 9999',
    [
        same(2, 'number', suit='A', value=3),
        same(2, 'number', suit='A', value=6),
        same(3, 'number', suit='B', value=3),
        same(3, 'number', suit='B', value=6),
        same(4, 'number', suit='C', value=9),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 4. FFF 33 666 99 DDDD -- any 1 suit with matching dragon
add('369-4: FFF 33 666 99 DDDD',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=6),
        same(2, 'number', suit='A', value=9),
        same(4, 'dragon', suit='A'),
    ],
    {'vars': ['A'], 'distinct_count': 1})

# 5. FFF 33 666 99 (s1) DDDD (s2) -- any 1 suit with opposite dragon
add('369-5: FFF 33 666 99 DDDD (opp)',
    [
        same(3, 'flower'),
        same(2, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=6),
        same(2, 'number', suit='A', value=9),
        same(4, 'dragon', suit='B'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 6. 33 66 (s1) 666 999 (s2) NEWS -- any 2 suits
add('369-6: 33 66 666 999 NEWS',
    [
        same(2, 'number', suit='A', value=3),
        same(2, 'number', suit='A', value=6),
        same(3, 'number', suit='B', value=6),
        same(3, 'number', suit='B', value=9),
        same(1, 'wind', wind='North'),
        same(1, 'wind', wind='East'),
        same(1, 'wind', wind='West'),
        same(1, 'wind', wind='South'),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 7. FF 3369 (s1, pair 3/6/9 + complement) 3333 (s2,=pair) 3333 (s3,=pair) -- 3 suits
add('369-7: FF 3369 3333 3333',
    [
        same(2, 'flower'),
        same(2, 'number', suit='A', value='P'),
        complement([3, 6, 9], 'P', 'number', suit='A'),
        same(4, 'number', suit='B', value='P'),
        same(4, 'number', suit='C', value='P'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'P': [3, 6, 9]})

# 8. FF 333 666 999 (s1) 369 (s2) -- any 2 suits
add('369-8: FF 333 666 999 369',
    [
        same(2, 'flower'),
        same(3, 'number', suit='A', value=3),
        same(3, 'number', suit='A', value=6),
        same(3, 'number', suit='A', value=9),
        same(1, 'number', suit='B', value=3),
        same(1, 'number', suit='B', value=6),
        same(1, 'number', suit='B', value=9),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# =====================================================================
# SINGLES AND PAIRS
# =====================================================================

# 1. NN EE WW SS 1 D (s1) 1 D (s2) 1 D (s3) -- 3 suits, any like number, matching dragon
add('SP-1: NN EE WW SS 1D 1D 1D',
    [
        same(2, 'wind', wind='North'),
        same(2, 'wind', wind='East'),
        same(2, 'wind', wind='West'),
        same(2, 'wind', wind='South'),
        same(1, 'number', suit='A', value='V'),
        same(1, 'dragon', suit='A'),
        same(1, 'number', suit='B', value='V'),
        same(1, 'dragon', suit='B'),
        same(1, 'number', suit='C', value='V'),
        same(1, 'dragon', suit='C'),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3},
    {'V': list(range(1, 10))})

# 2. 2 4 66 88 (s1) 2 4 66 88 (s2) 88 (s3) -- 3 suits, these numbers only
add('SP-2: 2 4 66 88 x2 + 88',
    [
        same(1, 'number', suit='A', value=2),
        same(1, 'number', suit='A', value=4),
        same(2, 'number', suit='A', value=6),
        same(2, 'number', suit='A', value=8),
        same(1, 'number', suit='B', value=2),
        same(1, 'number', suit='B', value=4),
        same(2, 'number', suit='B', value=6),
        same(2, 'number', suit='B', value=8),
        same(2, 'number', suit='C', value=8),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 3. FF 3369 (s1) 3669 (s2) 3699 (s3) -- any 3 suits (fixed templates per position)
add('SP-3: FF 3369 3669 3699',
    [
        same(2, 'flower'),
        same(2, 'number', suit='A', value=3),
        same(1, 'number', suit='A', value=6),
        same(1, 'number', suit='A', value=9),
        same(2, 'number', suit='B', value=6),
        same(1, 'number', suit='B', value=3),
        same(1, 'number', suit='B', value=9),
        same(2, 'number', suit='C', value=9),
        same(1, 'number', suit='C', value=3),
        same(1, 'number', suit='C', value=6),
    ],
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

# 4. 11 22 33 44 55 66 77 -- any 1 suit, any 7 consecutive
add('SP-4: 11 22 33 44 55 66 77',
    [
        same(2, 'number', suit='A', value=('offset', 'S', 0)),
        same(2, 'number', suit='A', value=('offset', 'S', 1)),
        same(2, 'number', suit='A', value=('offset', 'S', 2)),
        same(2, 'number', suit='A', value=('offset', 'S', 3)),
        same(2, 'number', suit='A', value=('offset', 'S', 4)),
        same(2, 'number', suit='A', value=('offset', 'S', 5)),
        same(2, 'number', suit='A', value=('offset', 'S', 6)),
    ],
    {'vars': ['A'], 'distinct_count': 1},
    {'S': list(range(1, 4))})  # start+6<=9 -> start<=3

# 5. 11 357 99 (s1) 11 357 99 (s2) -- any 2 suits
add('SP-5: 11 357 99 x2',
    [
        same(2, 'number', suit='A', value=1),
        same(1, 'number', suit='A', value=3),
        same(1, 'number', suit='A', value=5),
        same(1, 'number', suit='A', value=7),
        same(2, 'number', suit='A', value=9),
        same(2, 'number', suit='B', value=1),
        same(1, 'number', suit='B', value=3),
        same(1, 'number', suit='B', value=5),
        same(1, 'number', suit='B', value=7),
        same(2, 'number', suit='B', value=9),
    ],
    {'vars': ['A', 'B'], 'distinct_count': 2})

# 6. FF 2026 (s1) 2026 (s2) 2026 (s3) -- any 3 suits
add('SP-6: FF 2026 2026 2026',
    [same(2, 'flower')] + digits_2026('A') + digits_2026('B') + digits_2026('C'),
    {'vars': ['A', 'B', 'C'], 'distinct_count': 3})

if __name__ == '__main__':
    print(f"Total hands defined: {len(hands)}")
    results = []
    for h in hands:
        rows = generate_combinations(h)
        results.append((h, rows))
    write_workbook(results, '/mnt/user-data/outputs/Mahjong_All_Hand_Combinations.xlsx')
