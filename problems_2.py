def get_names(users):
    names = []
    for user in users:
        names.append(user.get("name"))
    return names

def total_marks(student):
    total = 0
    marks = student.get("marks") or []
    for m in marks:
        total += m
    return total