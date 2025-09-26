import csv

with open("courses_core.csv", encoding="utf-8", newline="") as f1:
    r1 = csv.DictReader(f1)
    core_columns = []
    for c in r1.fieldnames:
        if c != "student_id":
            core_columns.append(c)

    core = {}
    for row in r1:
        sid = row["student_id"]
        core[sid] = row

with open("courses_extra.csv", encoding="utf-8", newline="") as f2:
    r2 = csv.DictReader(f2)
    extra_columns = []
    for c in r2.fieldnames:
        if c != "student_id":
            extra_columns.append(c)

    extra = {}
    for row in r2:
        sid = row["student_id"]
        extra[sid] = row

common_ids = []
for sid in core:
    if sid in extra:
        common_ids.append(sid)

common_ids.sort(key=int)

with open("merged.csv", "w", encoding="utf-8", newline="") as out:
    header = ["student_id"] + core_columns + extra_columns
    writer = csv.DictWriter(out, fieldnames=header)
    writer.writeheader()

    for sid in common_ids:
        row = {"student_id": sid}
        for c in core_columns:
            row[c] = core[sid][c]
        for c in extra_columns:
            row[c] = extra[sid][c]
        writer.writerow(row)
