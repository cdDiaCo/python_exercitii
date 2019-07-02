from src.beginner_p2 import merge_two_objects

def test_simple():
    a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
    b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

    new_obj = merge_two_objects(a, b)
    assert new_obj == {'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3,
                        2]}, 'm': ([1], "wer")}








# intrebari: 1. Obiectele au mereu aceeasi lungime(numar de elemente)?
#            2. Cheile obiectelor se potrivesc mereu?
#            3. key-urile sunt in aceeasi ordine?
#            3. sau trebuie test case-uri pt cazurile de mai sus?


