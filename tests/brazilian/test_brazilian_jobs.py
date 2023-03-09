from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    jobs = read_brazilian_file(path)
    for job in jobs:
        assert job.keys() == {"title", "salary", "type"}

        # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_dictionary_keys
