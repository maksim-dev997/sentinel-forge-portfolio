#!/usr/bin/env python3

from datetime import datetime


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def main():
    try:
        with open(INPUT_FILE, "r") as file:
            lines = file.readlines()

        line_count = len(lines)

        report = []
        report.append("AUTOMATION REPORT")
        report.append("")
        report.append(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report.append(f"Input lines: {line_count}")
        report.append("")
        report.append("INPUT DATA:")
        report.append("")

        for line in lines:
            report.append(line.strip())

        with open(OUTPUT_FILE, "w") as file:
            file.write("\n".join(report))

        print("REPORT CREATED")

    except FileNotFoundError:
        print("INPUT FILE NOT FOUND")


if __name__ == "__main__":
    main()
