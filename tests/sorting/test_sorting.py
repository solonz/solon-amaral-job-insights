from src.pre_built.sorting import sort_by


mock = [
    {
        "min_salary": 8000,
        "max_salary": 15000,
        "date_posted": "07-03-2023",
    },
    {
        "min_salary": 5000,
        "max_salary": 12000,
        "date_posted": "08-03-2023",
    },
    {
        "min_salary": 6000,
        "max_salary": 13000,
        "date_posted": "09-03-2023",
    },
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock[0]["min_salary"] == 5000
