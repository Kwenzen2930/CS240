Job Scheduler Using Hashing and Heaps
=====================================

This Python script implements a job scheduler using a hash table for fast job lookup and a min-heap for 
managing job priorities. The script provides an interactive menu for users to add, process, delete, find, 
and display jobs.

Files and Classes
-----------------
1. `scheduler.py`: The main script that runs the job scheduler.
2. `job.py`: Defines the `Job` class.
3. `heap_manager.py`: Defines the `HeapManager` class.
4. `hash_table.py`: Defines the `HashTable` class.

### JobScheduler Class (scheduler.py)
The `JobScheduler` class provides methods to add, process, delete, find, and display jobs.
It uses the `HeapManager` and `HashTable` classes to manage jobs.

- `add_job()`: Prompts the user to add a job.
- `process_job()`: Processes the highest-priority job.
- `delete_job()`: Prompts the user to delete a job.
- `find_job()`: Prompts the user to find a job by ID.
- `display_jobs()`: Displays all jobs sorted by priority.
- `run()`: Runs the interactive menu for the job scheduler.

Usage
-----
1. Run the `scheduler.py` script.
2. Follow the interactive menu to add, process, delete, find, and display jobs.

