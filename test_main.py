import pytest


input1 = """
入力例1
""".strip()

output1 = """
出力例1
""".strip()

input2 = """
入力例2
""".strip()

output2 = """
出力例1
""".strip()


def main():
    解答


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
