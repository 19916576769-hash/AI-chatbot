from prompt import PromptEngine
from logs.logger import log_prompt






def run_pipeline(question):

    engine = PromptEngine()
    result = engine.build(question)

    log_prompt(
        prompt=result.prompt,
        task=result.task,
        version=result.version,
)
    return result.prompt
