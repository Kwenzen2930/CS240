class Job:
    def __init__(self, job_id, description, priority):
        self.job_id = job_id
        self.description = description
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"(Job {self.job_id}: {self.description}, Priority {self.priority})"