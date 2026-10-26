"""Q4(a): the ORIGINAL buggy code (connection leaks on error)."""


class Connection:
    open_count = 0

    def __init__(self):
        Connection.open_count += 1
        print("connection opened, open =", Connection.open_count)

    def close(self):
        Connection.open_count -= 1
        print("connection closed, open =", Connection.open_count)


def lookup(student_id):
    conn = Connection()
    if student_id < 0:
        raise ValueError("bad id")
    print("found student", student_id)
    conn.close()


lookup(1)
try:
    lookup(-1)
except ValueError as e:
    print("error:", e)
lookup(2)
print("open connections now:", Connection.open_count)
