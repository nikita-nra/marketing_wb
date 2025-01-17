from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Keyword:
    keyword: str
    count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Keyword':
        _keyword = str(obj.get("keyword"))
        _count = int(obj.get("count"))
        return Keyword(_keyword, _count)

@dataclass
class Words:
    excluded: List[str]
    pluse: List[str]
    keywords: List[Keyword]
    fixed: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Words':
        #А если пустое или один ключевик?
        _excluded = str(obj.get("excluded")).replace("['", '').replace("']", '').split("', '")
        _pluse = str(obj.get("pluse")).replace("['", '').replace("']", '').split("', '")
        _keywords = [Keyword.from_dict(y) for y in obj.get("keywords")]
        _fixed = bool(obj.get("fixed"))
        return Words(_excluded, _pluse, _keywords, _fixed)
    
@dataclass
class SW:
    words: Words

    @staticmethod
    def from_dict(obj: Any) -> 'SW':
        _words = Words.from_dict(obj.get("words"))
        return SW(_words)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
