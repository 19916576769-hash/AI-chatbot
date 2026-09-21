from .config import MAX_INPUT_LENGTH,ENABLE_INPUT_FILTER



class SecurityResult :
    def __init__(
        self,
        safe:bool,
        score:int,
        reason:list[str],
        text:str,
        logs:list | None = None,
    ):
        self.safe = safe
        self.score = score
        self.reason = reason
        self.text = text
        self.logs = logs or []




def check_input(text : str) ->SecurityResult  :
    """
    Validate user input.


    Returns:

        SecurityResult
    
    
    """


    text = text.strip()


    if text == "" :
        safe=False
        score=100
        reason=["Empty Input"]
        text=""
        return SecurityResult(
            safe=safe,
            score=score,
            reason=reason,
            text=text,
        )
                        
    
    if len(text) > MAX_INPUT_LENGTH :
        safe=False
        score=80
        reason=["Input TooLong"]
        text=text
        return SecurityResult (
            safe=safe,
            score=score,
            reason=reason,
            text=text,
        )
                        

    else :
        return  SecurityResult(
            safe=True,
            score=0,
            reason=[],
            text=text,
        )


    
                        






        
