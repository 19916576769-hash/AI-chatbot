from .input_filter import check_input,SecurityResult


def run_security(text:str)  -> SecurityResult   :


    """
    Run all the security checks

    Args:
        text (str):
            User input.
        
            
    Returns:
        SecurityResult:
        {
            "allowed"  : bool,
            "text"  : str,
            "risk"  : int,
            "reason"  : list[str] 
        
        }  

        ## 字典补充解释说明

        allowed:
            Whether the input is allowed.

        text:
            Sanitized user input.

        risk:
            Risk score (0-100).

        reason:
            List of detected risks.
    
    """
    result = check_input(text)


    if result.safe:
        return result

    if not result.safe:
        return result
    

    



