# CSV Merge Task 
### Theory  part
> **CSV (Comma-Separated Values)** is a plain-text table format where each line is a record and columns are separated by a delimiter (commonly a comma). 


For example:
| student_id | math | informatics |
|------------|------|-------------|
| 1          | 90   | 65          |
| 2          | 77   | 100         |
| 3          | 100  | 90          |

And how it looks in plain text:
```
student_id,math,informatics
1,90,65
2,77,100
3,100,90
```


Let's explore the **basics of the `csv` module**:
  - `csv.DictReader(file)` - reads rows as dictionaries; column names come from the header (`.fieldnames`).
  It looks like this: `{'student_id': '1', 'math': '90', 'informatics': '65'}`
  - `csv.DictWriter(file, fieldnames=[...])` - performs the reverse operation: it takes dictionaries and writes them back into a CSV file, following the fixed column order defined by fieldnames. Before writing the rows, you usually call `writeheader()` to output the header line. For example:
```python
import csv
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["student_id", "math", "informatics"])
    writer.writeheader()  # writes: student_id,math,informatics
    writer.writerow({"student_id": 1, "math": 90, "informatics": 65})
```
  
 Extra useful  **attributes/parameters:**
   - `DictReader.fieldnames` - stores the list of column names read from the header; useful to inspect available fields.  
   - `DictWriter(fieldnames=...)` - defines the exact order of columns when writing rows back into a CSV file. 
   - `delimiter` — specifies the character that separates values (comma by default, but can be ';', tab, etc.).  

You can find the `csv` module documentation here: - https://docs.python.org/3/library/csv.html

And quick reminder on **how to open the file:** `open(path, mode, encoding="utf-8", newline="")` where `newline=""` prevents extra blank lines on some OSes; set `encoding` explicitly.


### Assignment part

You are given **two CSV files** with course results:

`courses_core.csv` - core subjects  
| student_id | math | informatics |
|------------|------|-------------|
| 1          | 90   | 65          |
| 2          | 77   | 100         |
| 3          | 100  | 90          |

 `courses_extra.csv` - extra subjects  
 | student_id | history     | chemistry |
|------------|-------------|-----------|
| 1          | passed      | 70        |
| 2          | not passed  | 100       |
| 4          | passed      | 85        |
| 5          | not passed  | 92        |

Each file has a `student_id` column plus several grade columns. Your task is to create `merged.csv` which contains **only students present in both files**. Requirements:

- Rows: only `student_id` found in **both** inputs.  
- Sort rows by `student_id` in ascending numeric order.  
- Columns: first `student_id`, then **all** columns from `courses_core.csv` (excluding `student_id`), then **all** columns from `courses_extra.csv` (excluding `student_id`).  
- Values are copied exactly from the corresponding rows in each source.

Some notes:
- The `student_id` column must appear **only once** in the output (we keep a single `student_id` and do not duplicate it from both inputs).
- `student_id` values are **integers**; rows must be sorted in ascending numeric order (`key=int`).
