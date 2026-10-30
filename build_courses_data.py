import json
from courses_law import law_courses
from courses_politics import politics_courses
from courses_ir import ir_courses
from courses_econ import econ_courses

all_courses = law_courses + politics_courses + ir_courses + econ_courses

print(f"Total courses combined: {len(all_courses)}")

# Verify all course IDs are unique
ids = [c["id"] for c in all_courses]
assert len(ids) == len(set(ids)), f"Duplicate IDs detected: {[x for x in ids if ids.count(x) > 1]}"

# Verify all required fields
for i, c in enumerate(all_courses, 1):
    assert "id" in c, f"Missing id in course {i}"
    assert "title" in c, f"Missing title in course {i}"
    assert "category" in c, f"Missing category in course {i}"
    assert "instructor" in c, f"Missing instructor in course {i}"
    assert "modules" in c and len(c["modules"]) > 0, f"Missing modules in course {i}"
    for m in c["modules"]:
        assert "lessons" in m and len(m["lessons"]) > 0, f"Missing lessons in module of course {c['id']}"
        for l in m["lessons"]:
            assert "id" in l and "title" in l and "body" in l, f"Invalid lesson in course {c['id']}"

js_content = f"/* The Paper Crane Academy - 40 Comprehensive Academic Courses */\nwindow.COURSES_SEED = {json.dumps(all_courses, indent=2)};\n"

with open("/Users/shreyangondaliya/Paper-crane-academy/courses-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated /Users/shreyangondaliya/Paper-crane-academy/courses-data.js with {len(all_courses)} courses.")
