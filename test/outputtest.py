from subprocess import check_output

def test(command):
    return str(check_output(command,shell=True)).split("\\r\\n")


def test2(arr):
    for a in arr:
        print(a)

test2(test("type *"))
