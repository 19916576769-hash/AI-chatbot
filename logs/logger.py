import logging
from prompt import detect_task

logging.basicConfig(
    level=logging.INFO,
    filename="logs/app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def log_prompt(prompt,task,version):
    task = detect_task()
    print("=" * 60)

    print("Prompt logger")

    print(f"Prompt Version : {version}")

    print(f"Task : {task}")

    print()

    print(prompt)

    print("=" * 60)

    logging.info(
        f"[{version}] [{task}] {prompt}"
        )  ##终端可以看到logger


    