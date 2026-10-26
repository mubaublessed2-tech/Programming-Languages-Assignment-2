"""Q4(b): fixed with a context manager ('with')."""


class Connection:
    open_count = 0

    def __init__(self):
        Connection.open_count += 1
        print("connection opened, open =", Connection.open_count)

    def close(self):
        Connection.open_count -= 1
        print("connection closed, open =", Connection.open_count)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False  # do not swallow the exception


def lookup(student_id):
    with Connection():
        if student_id < 0:
            raise ValueError("bad id")
        print("found student", student_id)


lookup(1)
try:
    lookup(-1)
except ValueError as e:
    print("error:", e)
lookup(2)
print("open connections now:", Connection.open_count)
