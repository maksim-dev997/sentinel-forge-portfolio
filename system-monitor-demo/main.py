import os

print("SYSTEM MONITOR DEMO")

cpu_usage = os.getloadavg()[0]

memory_info = os.popen(
    "free -m | grep Mem"
).read().split()

total_ram = memory_info[1]
used_ram = memory_info[2]
free_ram = memory_info[3]

disk_info = os.popen(
    "df -h / | tail -1"
).read().split()

disk_total = disk_info[1]
disk_used = disk_info[2]
disk_free = disk_info[3]

with open(
    "report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "SYSTEM MONITOR REPORT\n\n"
    )

    report.write(
        f"CPU LOAD: {cpu_usage}\n"
    )

    report.write(
        f"TOTAL RAM: {total_ram} MB\n"
    )

    report.write(
        f"USED RAM: {used_ram} MB\n"
    )

    report.write(
        f"FREE RAM: {free_ram} MB\n"
    )

    report.write(
        f"DISK TOTAL: {disk_total}\n"
    )

    report.write(
        f"DISK USED: {disk_used}\n"
    )

    report.write(
        f"DISK FREE: {disk_free}\n"
    )

print("REPORT CREATED")
