from job import Job
from HeapManager import HeapManager
from HashTable import HashTable

class JobScheduler:
    """Job Scheduler using Hashing (for lookup) and Min-Heap (for priority queue)."""

    def __init__(self):
        self.heap_manager = HeapManager()
        self.hash_table = HashTable()

    def add_job(self):
        """Prompt user to add a job."""
        try:
            job_id = int(input("Enter Job ID: "))
            description = input("Enter Job Description: ")
            priority = int(input("Enter Job Priority (lower number = higher priority): "))

            job = Job(job_id, description, priority)
            if self.hash_table.add_job(job):
                self.heap_manager.add_job(job)
                print(f"✅ Job {job_id} added successfully!\n")
        except ValueError:
            print("❌ Invalid input! Job ID and priority must be numbers.\n")

    def process_job(self):
        """Process the highest-priority job."""
        job = self.heap_manager.process_job()
        if job:
            self.hash_table.delete_job(job.job_id)
            print(f"🚀 Processing {job}\n")
        else:
            print("⚠️ No jobs to process.\n")

    def delete_job(self):
        """Prompt user to delete a job."""
        try:
            job_id = int(input("Enter Job ID to delete: "))
            job = self.hash_table.delete_job(job_id)
            if job:
                self.heap_manager.delete_job(job)
                print(f"🗑️ Job {job_id} deleted successfully!\n")
            else:
                print(f"❌ Job {job_id} not found.\n")
        except ValueError:
            print("❌ Invalid input! Job ID must be a number.\n")

    def find_job(self):
        """Prompt user to find a job by ID."""
        try:
            job_id = int(input("Enter Job ID to search: "))
            job = self.hash_table.find_job(job_id)
            if job:
                print(f"🔍 Found: {job}\n")
            else:
                print("❌ Job not found.\n")
        except ValueError:
            print("❌ Invalid input! Job ID must be a number.\n")

    def display_jobs(self):
        """Display all jobs sorted by priority."""
        jobs = self.heap_manager.get_jobs()
        if jobs:
            print("\n📌 Jobs in Priority Queue (Sorted by Priority):")
            for job in jobs:
                print(job)
            print()
        else:
            print("⚠️ No jobs available.\n")

    def run(self):
        """Run the interactive menu for the job scheduler."""
        while True:
            print("\n🔷 Job Scheduler Menu 🔷")
            print("1️⃣ Add Job")
            print("2️⃣ Process Highest Priority Job")
            print("3️⃣ Delete Job")
            print("4️⃣ Find Job")
            print("5️⃣ Display Jobs")
            print("6️⃣ Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_job()
            elif choice == "2":
                self.process_job()
            elif choice == "3":
                self.delete_job()
            elif choice == "4":
                self.find_job()
            elif choice == "5":
                self.display_jobs()
            elif choice == "6":
                print("👋 Exiting Job Scheduler. Have a great day!")
                break
            else:
                print("❌ Invalid choice! Please enter a number between 1 and 6.\n")


# Run the interactive Job Scheduler
if __name__ == "__main__":
    scheduler = JobScheduler()
    scheduler.run()
