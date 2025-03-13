import heapq

class HeapManager:
    def __init__(self):
        self.heap = []

    def add_job(self, job):
        heapq.heappush(self.heap, job)

    def process_job(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def delete_job(self, job):
        self.heap.remove(job)
        heapq.heapify(self.heap)

    def get_jobs(self):
        return sorted(self.heap)