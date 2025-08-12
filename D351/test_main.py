import pytest


input1 = """
3423
12003
9580
""".strip()

output1 = """
12003
""".strip()

input2 = """
99999
1
50000
""".strip()

output2 = """
99999
""".strip()


def main():
    input_line = [int(input()) for _ in range(3)]
    result = max(input_line)
    print(result)


# 以下は固定
def test_main(monkeypatch) -> None:
    check(monkeypatch, main, input1, output1)
    check(monkeypatch, main, input2, output2)


def check(monkeypatch, func: None, input: str, output: str) -> None:
    import io

    stdin = io.StringIO(input)
    stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr("sys.stdin", stdin)
        m.setattr("sys.stdout", stdout)
        func()

    assert stdout.getvalue() == output + "\n"


if __name__ == "__main__":
    pytest.main([__file__])
