class Job:
    def __init__(self, id, deadline, profit) -> None:
        self.id = id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self) -> str:
        return f"job({self.id})"


def job_sequencing(jobs: list[Job]) -> list[int]:
    """
    Function to solve the Job Sequencing Problem with deadlines using a greedy algorithm.

    The Job Sequencing Problem is aimed at scheduling jobs in such a way that the maximum profit is obtained,
    given a set of jobs with associated deadlines and profits. Each job can take only one unit of time,
    and a job can only be scheduled before or on its deadline.

    Args:
    jobs (list[Job]): A list of jobs, where each job is represented as a tuple (job_id, deadline, profit).
        - job_id (int): Unique identifier of the job.
        - deadline (int): The latest time unit by which the job can be completed.
        - profit (int): The profit earned from completing the job.

    Returns:
    list[int]: A list of job_ids representing the sequence of jobs that maximizes the total profit.

    Time Complexity:
    - Sorting the jobs takes O(n log n), and scheduling takes O(n^2) in the worst case.

    Space Complexity:
    - O(n) for storing the time slots and the result sequence.

    Example:
    >>> jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]
    >>> job_sequencing_with_deadlines(jobs)
    [1, 3, 5]  # Job sequence yielding maximum profit
    """

    jobs.sort(key=lambda item: item.profit, reverse=True)
    result = [None] * len(jobs)

    for job in jobs:
        for pos in range(job.deadline - 1, -1, -1):
            if result[pos] is None:
                result[pos] = job
                break

    return [job for job in result if job is not None]


jobs = [
    Job(id=1, deadline=2, profit=100),
    Job(id=2, deadline=1, profit=19),
    Job(id=3, deadline=2, profit=27),
    Job(id=4, deadline=1, profit=25),
    Job(id=5, deadline=3, profit=15),
]

print(job_sequencing(jobs))