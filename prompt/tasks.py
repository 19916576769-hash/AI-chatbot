def build_translation_prompt(question):
    return """
    翻译：
    保持原意。
    自然表达。
    必要时解释文化差异。
    """



def build_programming_prompt(question):
    return """
    如果回答代码：
    必须：
    使用Markdown。
    添加代码注释。
    解释思路。
    注意性能。
    """
##***********************Mapping***********************##

TASK_PROMPTS = {

    "translation": build_translation_prompt,

    "programming": build_programming_prompt,

}

TASK_KEYWORDS = {

    "programming": [
        "python",
        "java",
        "代码",
        "bug",
        "编程",
    ],

    "translation": [
        "翻译",
        "translate",
        "英文",
    ]
}

##**************************Mapping************************************##

def detect_task(question):
    """根据用户的问题,找到提示词的名称"""
    question = question.lower()
    for task,keywords in TASK_KEYWORDS.items():

        if any(keyword in question for keyword in keywords):
            return task

    return "general"


