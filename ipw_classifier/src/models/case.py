from bs4 import BeautifulSoup
from dataclasses import dataclass
from uuid import UUID
from typing import Set
import math
import numpy as np
#import spacy
import nl_core_news_lg

#Variables
nlp = nl_core_news_lg.load()

#Constants
NOUN: str = 'NOUN'

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
        future: str 
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
        returnvalue = ''
        
        if string is not None and not (isinstance(string, float) and math.isnan(string)): 
            # parse html
            soup = BeautifulSoup(string, 'html.parser')
            returnvalue = soup.getText()

            # remove '\\n'
            returnvalue = returnvalue.replace('\\n', '')

        return returnvalue
 
    def vector(self):
        string = self.description.lower()
        tokens = nlp(string)
        n = 0
        for token in tokens:
            if token.pos_ == NOUN:
                n += 1
                if n == 1:
                    vector_sum = token.vector
                else:
                    vector_sum += token.vector
        if n > 0:
            returnvalue = vector_sum / n
        else:
            returnvalue = nlp('').vector
        return returnvalue

    def norm(self) -> float:
        return np.linalg.norm(self.vector())
    
    def distance(self, case) -> float:
        vector1 = self.vector()
        vector2 = case.vector()

        if self.norm() == 0:
            raise ValueError(f'Vector length is 0 for sample {self.id}. This sample should not be part of the clustering algorithm')
        if case.norm() == 0:
            raise ValueError(f'Vector length is 0 for sample {case.id}. This sample should not be part of the clustering algorithm')

        similarity = np.dot(vector1, vector2) / (self.norm() * case.norm())
        similarity = max(-1.0, min(1.0, similarity)) # to remove corner cases from rounding
        returnvalue = 1 - similarity # to create a distance that is 0 for equal cases (similarity = 1) and 2 for cases that are very far apart
        return returnvalue



