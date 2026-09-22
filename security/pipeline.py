from .input_filter import check_input,SecurityResult
from .injection import detect_prompt_injection

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

    ## 输入的安全检查
    result = check_input(text)


    if not result.safe:
        return result
    

    ## 输入内容的安全检查
    result = detect_prompt_injection(result.text)

    
    if not result.safe:
        return result




    
    return result



