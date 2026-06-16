import os

QUEUE_FILE = "task_queue.txt"
RUNNING_FILE = "queue_running.txt"
COMPLETED_FILE = "completed_tasks.txt"
FAILED_FILE = "failed_tasks.txt"

print("TASK QUEUE DEMO")

if not os.path.exists(QUEUE_FILE):
    print("QUEUE FILE NOT FOUND")
    exit()

with open(QUEUE_FILE, "r", encoding="utf-8") as queue:
    tasks = queue.readlines()

tasks = [task.strip() for task in tasks if task.strip()]

if len(tasks) == 0:
    print("QUEUE EMPTY")
    exit()

current_task = tasks[0]

with open(RUNNING_FILE, "w", encoding="utf-8") as running:
    running.write(current_task)

print("RUNNING TASK:")
print(current_task)

try:

    if current_task.startswith("mkdir "):

        folder_name = current_task.replace(
            "mkdir ",
            ""
        )

        os.makedirs(
            folder_name,
            exist_ok=True
        )

    elif current_task.startswith("touch "):

        file_name = current_task.replace(
            "touch ",
            ""
        )

        open(
            file_name,
            "a",
            encoding="utf-8"
        ).close()

    else:

        raise Exception(
            "UNKNOWN COMMAND"
        )

    with open(
        COMPLETED_FILE,
        "a",
        encoding="utf-8"
    ) as completed:

        completed.write(
            current_task + "\n"
        )

    print("TASK COMPLETED")

except Exception as error:

    with open(
        FAILED_FILE,
        "a",
        encoding="utf-8"
    ) as failed:

        failed.write(
            current_task + "\n"
        )

    print("TASK FAILED")
    print(error)

remaining_tasks = tasks[1:]

with open(
    QUEUE_FILE,
    "w",
    encoding="utf-8"
) as queue:

    for task in remaining_tasks:

        queue.write(
            task + "\n"
        )

with open(
    RUNNING_FILE,
    "w",
    encoding="utf-8"
) as running:

    running.write("")

print("QUEUE UPDATED")
