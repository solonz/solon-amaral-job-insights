from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf-8") as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')

        return list(content)


def get_unique_job_types(path: str):
    jobs = read(path)
    job_types = []
    for job in jobs:
        job_types_record = job["job_type"]
        if job_types_record not in job_types:
            job_types.append(job_types_record)
    return job_types

    """Checks all different job types and returns a list of them


    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
