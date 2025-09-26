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
        
# union instead of intersection
all_ids = []
for sid in core:
    all_ids.append(sid)
for sid in extra:
    if sid not in all_ids:
        all_ids.append(sid)

all_ids.sort(key=int)

with open("merged.csv", "w", encoding="utf-8", newline="") as out:
    header = ["student_id"] + core_columns + extra_columns
    writer = csv.DictWriter(out, fieldnames=header)
    writer.writeheader()

    for sid in all_ids:
        row = {"student_id": sid}
        for c in core_columns:
            if sid in core:
                row[c] = core[sid][c]
            else:
                row[c] = ""
        for c in extra_columns:
            if sid in extra:
                row[c] = extra[sid][c]
            else:
                row[c] = ""
        writer.writerow(row)
