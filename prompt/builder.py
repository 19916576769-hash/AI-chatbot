
from .tasks import detect_task, TASK_PROMPTS
from .stages import PROMPT_STAGES


def build_prompt(question):
    """构建发送给大模型的完整提示词prompt,并且根据用户的问题完成各种组合"""

    task = detect_task(question)

    
    sections = []

    for name,stage_func in PROMPT_STAGES:

        result = stage_func()

        if result:
            sections.append(result)


    builder = TASK_PROMPTS.get(task)

    if builder:
        sections.append(builder(question))

   
    

    return "\n\n".join(sections)   ##自动加了两个换行符,让各个部分之间有间隔,更清晰
