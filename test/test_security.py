from security.pipeline import run_security

def test_normal():
    assert run_security("Hello") is not None

def test_empty():
    assert run_security("") is not None

def test_long():
    assert run_security("A" * 600) is not None