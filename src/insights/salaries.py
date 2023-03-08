from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salaries = read(path)
    salaries_list = []
    for salary in salaries:
        if salary["max_salary"].isnumeric():
            salaries_list.append(int(salary["max_salary"]))
    return max(salaries_list)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    salaries = read(path)
    salaries_list = []
    for salary in salaries:
        if salary["min_salary"].isnumeric():
            salaries_list.append(int(salary["min_salary"]))
    return min(salaries_list)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("Error")
    salary_type = type(salary)
    if (
        (
            type(job["min_salary"]) is not int
            and not str(job["min_salary"]).isdigit()
        )
        or (
            type(job["max_salary"]) is not int
            and not str(job["max_salary"]).isdigit()
        )
        or (salary_type is not int and salary_type is not str)
        or (salary_type is str and not salary.isdigit())
    ):
        raise ValueError("Error")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Error")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_in_salary_range = []
    for job in jobs:
        try:
            filter = matches_salary_range(job, salary)
            if filter:
                jobs_in_salary_range.append(job)
        except ValueError:
            pass
    return jobs_in_salary_range
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
