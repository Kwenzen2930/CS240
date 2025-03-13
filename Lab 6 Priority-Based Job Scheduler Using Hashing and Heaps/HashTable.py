class HashTable:
    def __init__(self):
        self.table = {}

    def add_job(self, job):
        if job.job_id in self.table:
            return False
        self.table[job.job_id] = job
        return True

    def delete_job(self, job_id):
        return self.table.pop(job_id, None)

    def find_job(self, job_id):
        return self.table.get(job_id)