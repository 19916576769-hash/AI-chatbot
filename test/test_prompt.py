from prompt import build_prompt

def test_build_prompt():
    prompt = build_prompt("Hello")

    assert isinstance(prompt, str)
    assert len(prompt) > 0