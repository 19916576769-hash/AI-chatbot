# test/test_memory.py
from memory import extract_memory  # 注意这里不要用 security.memory，如果 memory.py 在根目录的话

def test_memory_name():
    result = extract_memory("我叫KJ")
    assert result is not None
    # 如果你知道它会返回什么，可以写更精确的断言，比如 assert "KJ" in result

def test_memory_job():
    result = extract_memory("我是信息安全专业")
    assert result is not None

def test_memory_hobby():
    result = extract_memory("我喜欢篮球")
    assert result is not None
