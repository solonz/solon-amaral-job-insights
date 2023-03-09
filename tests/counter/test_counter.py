from src.pre_built.counter import count_ocurrences

path = "data/jobs.csv"


def test_counter():
    assert count_ocurrences(path, "complex") == 2068
    assert count_ocurrences(path, "release") == 178
