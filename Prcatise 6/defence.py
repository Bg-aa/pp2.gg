import os
from functools import reduce
import shutil

if not os.path.exists("scores"):
    os.makedirs("scores")
    with open(os.path.join("scores", "class1.txt"), "w") as f:
        f.write("Alice,85\nBob,90\nCharlie,78\n")
    with open(os.path.join("scores", "class2.txt"), "w") as f:
        f.write("David,92\nEve,88\nFrank,81\n")
    with open(os.path.join("scores", "class3.txt"), "w") as f:
        f.write("Grace,95\nHank,70\nIvy,87\n")

students = []

files = os.listdir("scores")

for file in files:
    if file.endswith(".txt"):
        path = os.path.join("scores", file)
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if line and "," in line:
                    name, score = line.split(",")
                    students.append((name.strip(), int(score.strip())))

if not students:
    print("Error: student list is empty!")
    exit()

names = [s[0] for s in students]
scores = [s[1] for s in students]

total_students = len(students)
total_score = sum(scores)
max_score = max(scores)
min_score = min(scores)
average_score = total_score / total_students

new_scores = list(map(lambda x: x + 5, scores))

top_students = list(filter(lambda x: x[1] > 85, students))

product_scores = reduce(lambda x, y: x * y, scores)

print("Students with index:")
for i, (name, score) in enumerate(students, start=1):
    print(i, name, score)

combined = list(zip(names, scores))
#print("Combined:", combined)

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("\nSorted students:")
for name, score in sorted_students:
    print(name, score)

with open("report.txt", "w") as f:
    f.write(f"Total students: {total_students}\n")
    f.write(f"Average score: {average_score:.2f}\n")
    f.write(f"Highest score: {max_score}\n")
    f.write(f"Lowest score: {min_score}\n\n")
    f.write("Top students (>85):\n")
    for name, score in top_students:
        f.write(f"{name} {score}\n")

shutil.copy("report.txt", "report_backup.txt")

print("\nReport saved to report.txt and backup created as report_backup.txt")