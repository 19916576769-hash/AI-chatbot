from pipeline import run_pipeline

def test_pipeline_returns_string():
    result = run_pipeline("Hello")

    assert isinstance(result, str)


def test_pipeline_not_empty():
    result = run_pipeline("Hello")

    assert len(result) > 0


def test_pipeline_contains_role():
    result = run_pipeline("Hello")

    assert "你是KK" in result