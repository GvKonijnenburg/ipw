from bs4 import BeautifulSoup
from dataclasses import dataclass
from uuid import UUID
from typing import Dict
import math

@dataclass()  
class Case:
    id: UUID
    perspective: str
    milestones: str
    scenarios: str
    breakthrough: str
    exception: str
    do_self: str
    support: str
    treatment: str
    description: str
    solution: str
    future: str

    def __init__(  
        self,  
        id: UUID,  
        perspective: str,  
        milestones: str,  
        scenarios: str,  
        breakthrough: str,  
        exception: str,  
        do_self: str,  
        support: str,  
        treatment: str,  
        description: str,  
        solution: str,  
        future: str,  
    ):  
        self.id = id  
        self.perspective = self._clean_input(perspective)  
        self.milestones = self._clean_input(milestones)  
        self.scenarios = self._clean_input(scenarios)  
        self.breakthrough = self._clean_input(breakthrough)  
        self.exception = self._clean_input(exception)  
        self.do_self = self._clean_input(do_self)  
        self.support = self._clean_input(support)  
        self.treatment = self._clean_input(treatment)  
        self.description = self._clean_input(description)  
        self.solution = self._clean_input(solution)  
        self.future = self._clean_input(future)  
  
    def _clean_input(self, string: str) -> str:  
        if string is None or (isinstance(string, float) and math.isnan(string)): 
            return ''  
        else:  
            soup = BeautifulSoup(string, 'html.parser')
            return soup.getText()

    def word_count(string:str, returnvalue:Dict[str, int] = None) -> Dict[str, int]:
        if returnvalue = None:

        words = string.split()
        for word in words:
            if word in returnvalue:
                returnvalue[word] += 1
            else:
                returnvalue[word] = 1
        return returnvalue()



