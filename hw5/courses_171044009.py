class Course:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def is_overlapped(self, other):
        return self.start < other.finish


def max_attend(courses):
    result = 0
    while courses:
        earliest = min(courses, key=lambda c: c.finish)
        result += 1
        courses = [c for c in courses if not c.is_overlapped(earliest)]
    return result


courses = [
    Course(1, 2),
    Course(3, 4),
    Course(0, 6),
    Course(5, 7),
    Course(8, 9),
    Course(5, 9),
]

print(max_attend(courses))
