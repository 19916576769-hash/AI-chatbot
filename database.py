import sqlite3
from config import DATABASE_PATH
def init_database():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()

    conn.close()




# 保存一条聊天记录
def save_message(role, content):

    # 连接数据库
    conn = sqlite3.connect(DATABASE_PATH)

    # 创建游标
    cursor = conn.cursor()

    # 执行SQL语句
    cursor.execute(
        """
        INSERT INTO chat_history(role, content)
        VALUES (?, ?)
        """,
        (role, content)
    )

    # 保存
    conn.commit()

    # 关闭
    conn.close()



    # 读取所有聊天记录
def load_history(limit=20):

    # 连接数据库
    conn = sqlite3.connect(DATABASE_PATH)

    # 创建游标
    cursor = conn.cursor()

    # 查询所有聊天记录
    cursor.execute("""
    SELECT role, content
    FROM chat_history
    ORDER BY id DESC
    LIMIT ?
    """,(limit,))


    # 获取所有数据
    rows = cursor.fetchall()

    # 反转列表，使最新的记录在前
    rows.reverse() 

    # 关闭数据库
    conn.close()

    history = []

    for role, content in rows:

        history.append(
            {
                "role": role,
                "content": content
            }
        )

    return history

init_database()

if __name__ == "__main__":

    save_message("user", "你好")
    save_message("assistant", "你好呀")

    history = load_history()

    print(history)