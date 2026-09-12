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
    #再增加一张表，用于存储记忆数据memory
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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



def save_memory(key, value):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memory(key, value)
        VALUES(?, ?)

        ON CONFLICT(key) #如果key已经存在，则更新value和updated_at字段
        DO UPDATE SET
            value = excluded.value,
            updated_at = CURRENT_TIMESTAMP
    """, (key, value))

    conn.commit()

    conn.close()


def load_memory():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT key, value
        FROM memory
    """)

    rows = cursor.fetchall()

    conn.close()

    memory = {}

    for key, value in rows:
        memory[key] = value

    return memory


def delete_memory(key):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM memory
        WHERE key=?
    """, (key,))

    conn.commit()

    conn.close()



init_database()

if __name__ == "__main__":

    save_message("user", "你好")
    save_message("assistant", "你好呀")

    history = load_history()

    print(history)