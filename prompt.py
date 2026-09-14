from config import ENABLE_MEMORY,ENABLE_ROLES,ENABLE_RULES,ENABLE_STYLE
from database import load_memory


"""
Prompt Engine

Version: 1.0.0

Modules:
- Role
- Memory
- Rules
- Style
"""



def build_role():
    return """
    你是KK,
    你是一个AI万能助手,
    你的目标是帮助用户学习、编程、分析问题，并提供准确、清晰的回答。
    """

def build_style():
    return """
    你回答问题的风格是：
    1. 回答尽量简洁
    2. 必要时举例
    3. 不要有任何多余的解释
    4. 用户的问题多向用户提问，帮助用户更好地理解问题式和知识点
    6. 使用markdown格式,必要时使用代码块,必要时使用表格
    """
def build_rules():
    return """
    你回答问题的规则是：
    1. 回答要准确
    2. 必须注重用户安全
    3. 诚实回答,需要用户提供的信息就主动向用户提问
    4. 回答准确,不知道就是不知道,不要乱编
    """

def build_memory():
    memory = load_memory()  # 加载记忆数据到内存中
    prompt = ""
    if memory:
        prompt += "\n\n"
        prompt += "【用户长期记忆】\n"
        for key, value in memory.items():
            prompt += f"{key}: {value}\n"
    return prompt


def build_translation_prompt():
    return """
    翻译：
    保持原意。
    自然表达。
    必要时解释文化差异。
    """



def build_programming_prompt():
    return """
    如果回答代码：
    必须：
    使用Markdown。
    添加代码注释。
    解释思路。
    注意性能。
    """



def detect_task(question):
    """根据用户的问题,找到提示词的名称"""
    question = question.lower()
    if "python" in question:
        return "programming"

    if "翻译" in question:
        return "翻译"
    else :
        return ""




def build_prompt(question):
    """构建发送给大模型的完整提示词prompt,并且根据用户的问题完成各种组合"""

    task = detect_task(question)

    
    sections = []

    if ENABLE_ROLES:
        sections.append(build_role())

    if ENABLE_MEMORY:
        sections.append(build_memory())

    if ENABLE_RULES:
        sections.append(build_rules())

    if ENABLE_STYLE:
        sections.append(build_style())

    if task == "翻译":
        sections.append(build_translation_prompt())

    elif task == "programming":
        sections.append(build_programming_prompt())
   
    

    return "\n\n".join(sections)   ##自动加了两个换行符,让各个部分之间有间隔,更清晰









