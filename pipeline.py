from prompt import build_prompt,PROMPT_VERSION,detect_task
from logs.logger import log_prompt
def run_pipeline(question):
    task = detect_task(question)
    prompt = build_prompt(question)
    log_prompt(
    prompt=prompt,
    task=task,
    version=PROMPT_VERSION,
)
    return {
        "prompt" : prompt
    }

