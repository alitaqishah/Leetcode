from pathlib import Path
import re


README_FILE = Path("README.md")

rows = []


for folder in Path(".").iterdir():

    # Sirf folders ko check karo
    if not folder.is_dir():
        continue

    # GitHub ka hidden folder ignore karo
    if folder.name.startswith("."):
        continue

    # Folder name se problem number aur name nikalo
    match = re.match(r"^(\d+)-(.*)$", folder.name)

    if not match:
        continue

    problem_number = int(match.group(1))
    problem_name = match.group(2)

    # Problem name ko readable form mein convert karo
    problem_name = problem_name.replace("-", " ").title()

    # Python file find karo
    python_files = list(folder.glob("*.py"))

    if not python_files:
        continue

    python_file = python_files[0]

    # GitHub link
    solution_link = (
        f"https://github.com/alitaqishah/Leetcode/"
        f"blob/main/{folder.name}/{python_file.name}"
    )

    rows.append(
        (
            problem_number,
            problem_name,
            f"[Python]({solution_link})"
        )
    )


# Problem number ke according sort karo
rows.sort(key=lambda x: x[0])


# README create karo
content = "# Leetcode\n\n"

content += "| **#** | **Problem** | **Solution** |\n"
content += "| ----- | ----------- | ------------ |\n"


for number, problem, solution in rows:

    content += f"| {number} | {problem} | {solution} |\n"


README_FILE.write_text(content, encoding="utf-8")

print("README updated successfully!")