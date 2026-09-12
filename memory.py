from openai import OpenAI
from config import (API_KEY, MODEL_NAME, MEMORY_PROMPT)
import json,logging

client = OpenAI(
    api_key=API_KEY,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)







def extract_memory(question):
    #准备,组织messages
    messages = [
        {"role": "system", "content": MEMORY_PROMPT},
        {"role": "user", "content": question}
    ]


    #调用聊天模型
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            stream = False   #这个记忆提取不需要流式输出,直接返回完整结果,返回会速度加快一些
        )


    except Exception as e:
        logging.error(
            f"调用聊天模型失败：{type(e).__name__} - {e}"
        )
        return None


    #获得结果
    result = response.choices[0].message.content.strip()
    print(">>> 模型原始返回:", repr(result))  

    #strip()去掉首尾空格,如果是NONE,就返回None,否则将JSON字符串转换为Python对象



    #将JSON字符串转换为Python对象
    result = result.strip().strip("'").strip('"')

    if result.lower() == "none":
        return None



    # 异常处理 真正解析JSON字符串,如果解析失败,返回None
    try:
        return json.loads(result)

    except json.JSONDecodeError:
        logging.error(
            f"解析JSON字符串失败：{result}"
        )
        return None

    