import sys

def error_message_details(error,sys_object:sys)->str:
    _,_,exc_tb = sys_object.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"""
        Error occured in python script name : {file_name},
        line number : {exc_tb.tb_lineno} and 
        error : {str(error)}
    """
    return error_message

class CustomException(Exception):
    def __init__(self,error, sys_object:sys):
        super.__init__(error)
        self.error_message = error_message_details(error,sys_object)

    def __str__(self):
        return self.error_message