from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Optional


class Sequence:
    def __init__(self, text: str) -> None:
        self._text = text
        self._alphabet = {}
        self._words = {}

        
def get_alphabet(text: str) -> Counter:
    alphabet = Counter()
    for t in text:
        alphabet[t] += 1
    return alphabet

        
class ActionContext:
    pass

def classname(instance):
    return instance.__class__.__name__

class Action:
    def __init__(self):
        print(classname(self))
    
    def execute(self, 
                source: str, 
                context: ActionContext) -> None:
        print(f"{classname(self):s}.execute")

    
class Parser:
    def __init__(self, alphabet: str) -> None:
        self._actions_per_character = defaultdict(list)
        self._actions = {}
        self._alphabet = alphabet
        self._characters = []
        
    @property
    def actions_per_character(self):
        return self._actions_per_character
    
    @property
    def actions(self):
        return self._actions

    @property
    def alphabet(self):
        return self._alphabet
    
    @property
    def characters(self):
        return self._characters

    def update_action(self, 
                      key: int, 
                      action: Action) -> None:
        self.actions[key] = action
        
    def update_actions_per_character(self, 
               characters: str, 
               action_key: int
               ) -> None:
        for c in characters:
            self.actions_per_character[c].append(action_key)

    def check(self) -> bool:
        number_of_actions = len(self.actions)
        for character, actions in self.actions_per_character.items():
            test = all((0 <= a < len(actions)))
            if test:
                continue
            else:
                return False
        return True

            
class TreeNode:
    def __init__(self, 
                 key: Tuple[int, int],
                 parent: Optional['TreeNode'] = None
                 ) -> None:
        self._key = key
        self._parent = parent
        self._count = 1
        self._children = {}
        
    @property
    def key(self):
        return self._key
    
    @property
    def parent(self) -> Optional['TreeNode']:
        return self._parent
    
    @property
    def count(self) -> int:
        return self._count
    
    @count.setter
    def count(self, value: int) -> None:
        self._count = value


    
