import functools
import io
import sys
from contextlib import redirect_stdout
# We should really saves this as some kind of class Im practicing my nvim coding in pythin to try adn get faster at typing in nvim I use the lazy vim git hub its very cool.
from typing import Callable, Any, List, Dict
from enum import Enum, auto 

# my dict wasnt working and out of time #TODO FIX it
def capture_and_print(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f = io.StringIO()
        with redirect_stdout(f):
            result = func(*args, **kwargs)
        
        captured = f.getvalue()
        wrapper.captured_output = captured
        
        # --- Still print it ---
        print(captured, end="") 
        
        return result
    return wrapper



#
#
type printFn = Callable[[str], None]
class NameCalls(Enum):
    nice = auto()
    mean = auto()
    normal = auto()
    wierd = auto()

def name_call(name:str): 
         print(f" LOL {f'{name}':%^9} xP", end="")
class NameCalling():
    def __init__(self,name : str, call : NameCalls, method : Callable[[str],None]):
        self.name = name
        self.call : NameCalls =call
        self.func : Callable[[str], None] = method
        self.extra_words : str = "I get added to the comment"
        match self.call:
            case NameCalls.nice:
                self.extra_words = "Your damm handsome hun"
            case NameCalls.mean:
                self.extra_words = "Your like a sink plug"
            case NameCalls.normal:
                self.extra_words = "Your being caled out"
            case NameCalls.wierd:
                self.extra_words = "WAGHAHAHAH YOU DA BEST ! ROOOOR!"
        self.full_package = f"WE ARE CALLING FOR {self.name} YOU That your , {self.extra_words}"
        # I thought it would be cool if we stored out calls in a list to then look at after doing some calls to really show why classes were so cool
        self.calls : List  = []
        self.calls_dict : Dict = {}
        self.call_id : int = 0
    @capture_and_print
    def Naming(self,Number_Of_calls:int) -> bool:
        '''Functions are meant to have some text under them that explain what they do so when you hover over them you can see this
        of course doing 3 \'\'\' can allow you to tpye over multiple lines and you should be careful on not writing acutionable code 
        as it happens strings can be converted into code.
        This function takes : A number of calls it calls that many times and then returns true if it was finished.
        '''
        local_calls : list = []
        for _ in range(Number_Of_calls):
            self.func(self.full_package)
            local_calls.append(self.full_package)
        self.calls.append(local_calls)
        self.calls_dict[f"{self.name}_{self.call_id}"] = local_calls
        return True
    def reset_user(self, name=None,call=None,method=None):
        check_none = lambda var : not(var is None)
        if check_none(name):
            self.name : str= name
        if check_none(method):
            self.func : printFn = method
        if check_none(call):
            self.call :NameCalls = call
        self.__init__(name=self.name,call=self.call,method=self.func)
    def print_keys(self):
        for (j) in (self.calls_dict.keys()):
            print(f"Key :{""} Value {j}\n{'':_^60}\n")
            print(len(self.calls))
def crazzy_print(text : str, num1 =13,num2=69,num3=3):
    text_list : List = [ord(texty) for texty in text ]
    adjusted_texty : List = [(((text * num1)+ num2)*num3) for text in text_list]
    char_list : List = [chr(int(str(adjusted_texty[i]) + str(adjusted_texty[i+1])) if int(str(adjusted_texty[i]) + str(adjusted_texty[i+1])) < 110000 else int(str(adjusted_texty[i]) + str(adjusted_texty[i+1])) % 110000 ) for i in range(0, len(adjusted_texty), 2)]
    listy_string = "".join(char_list)
    print(listy_string)
Rushil = NameCalling(name="Cheese",call=NameCalls.nice,method=name_call)
Rushil.Naming(Number_Of_calls =400)
Rushil.reset_user(method =crazzy_print)
Rushil.Naming(Number_Of_calls =300)
Rushil.reset_user(method =lambda x: print(f"Eheh this works right {x}") )
Rushil.Naming(Number_Of_calls =200)
Rushil.reset_user(name="Soggy Cheese",call=NameCalls.nice,method=name_call)
Rushil.reset_user(method =lambda x: print(f"We have bad news {x} No dont tell me I am ... "),call=NameCalls.wierd )
Rushil.Naming(Number_Of_calls =300)
Rushil.reset_user(name="Cheese",call=NameCalls.nice,method=name_call)
Rushil.Naming(Number_Of_calls =300)
# Rushil.print_keys() #TODO FIX ME 
all_prints = Rushil.Naming.captured_output
print(f'\n\n\n\n\n\nIn toatal we printed the following length : {len(all_prints)}')
