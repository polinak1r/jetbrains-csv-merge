import unittest
import csv


class TestCase(unittest.TestCase):
    def test_header(self):
        with open("courses_core.csv", encoding="utf-8", newline="") as f:
            r1 = csv.DictReader(f)
            core_cols = [c for c in r1.fieldnames if c != "student_id"]
        with open("courses_extra.csv", encoding="utf-8", newline="") as f:
            r2 = csv.DictReader(f)
            extra_cols = [c for c in r2.fieldnames if c != "student_id"]
        with open("merged.csv", encoding="utf-8", newline="") as f:
            header = next(csv.reader(f))

        self.assertEqual(
            header, ["student_id"] + core_cols + extra_cols,
            msg="Header is wrong. Expected: student_id + CORE cols + EXTRA cols."
        )
        self.assertEqual(
            header.count("student_id"), 1,
            msg="Duplicate 'student_id' in header. Keep it only once."
        )

    def test_ids(self):
        with open("courses_core.csv", encoding="utf-8", newline="") as f:
            r1 = csv.DictReader(f)
            core_ids = {row["student_id"] for row in r1}
        with open("courses_extra.csv", encoding="utf-8", newline="") as f:
            r2 = csv.DictReader(f)
            extra_ids = {row["student_id"] for row in r2}
        with open("merged.csv", encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))[1:]

        expected_ids = sorted(core_ids & extra_ids, key=int)
        actual_ids = [r[0] for r in rows]

        self.assertEqual(
            actual_ids, expected_ids,
            msg="Wrong ID set/order. Use intersection only and sort numerically."
        )

    def test_rows(self):
        with open("courses_core.csv", encoding="utf-8", newline="") as f:
            r1 = csv.DictReader(f)
            core_cols = [c for c in r1.fieldnames if c != "student_id"]
            core = {row["student_id"]: row for row in r1}
        with open("courses_extra.csv", encoding="utf-8", newline="") as f:
            r2 = csv.DictReader(f)
            extra_cols = [c for c in r2.fieldnames if c != "student_id"]
            extra = {row["student_id"]: row for row in r2}
        with open("merged.csv", encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))[1:]

        expected_ids = sorted(set(core) & set(extra), key=int)
        for i, sid in enumerate(expected_ids):
            expected = [sid] + [core[sid][c] for c in core_cols] + [extra[sid][c] for c in extra_cols]
            self.assertEqual(
                rows[i], expected,
                msg=f"Row for student_id={sid} is wrong. Copy values exactly from CORE and EXTRA."
            )


if __name__ == "__main__":
    unittest.main()
