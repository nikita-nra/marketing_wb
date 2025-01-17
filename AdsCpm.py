from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Advert:
    code: str
    advertId: int
    id: int
    cpm: int
    subject: int

    @staticmethod
    def from_dict(obj: Any) -> 'Advert':
        _code = str(obj.get("code"))
        _advertId = int(obj.get("advertId"))
        _id = int(obj.get("id"))
        _cpm = int(obj.get("cpm"))
        _subject = int(obj.get("subject"))
        return Advert(_code, _advertId, _id, _cpm, _subject)

@dataclass
class Bids:
    adverts: List[Advert]

    @staticmethod
    def from_dict(obj: Any) -> 'Bids':
        try:
            _adverts = [Advert.from_dict(y) for y in obj.get("adverts")]
            return Bids(_adverts)
        except:
            return None
    


@dataclass
class Item:
    id: int
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        return Item(_id, _name)

@dataclass
class Filter:
    items: List[Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Filter':
        _items = [Item.from_dict(y) for y in obj.get("items")]
        return Filter(_items)
    
@dataclass
class Data:
    filters: List[Filter]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        _filters = [Filter.from_dict(y) for y in obj.get("filters")]
        return Data(_filters)

@dataclass
class Category:
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        try:
            _data = Data.from_dict(obj.get("data"))
            return Category(_data)
        except:
            return None
    

@dataclass
class Cpm:
    id: List[str]
    name: List[str]
    cpm: List[str]

    @staticmethod
    def create(bids: Bids, category: Category) -> 'Cpm':
        if bids == None or category == None:
            return None
        _id = []
        _name = []
        _cpm = []
        for i in range(0, max(10, min(len(bids.adverts), 50))):
            try:
                _id.append(bids.adverts[i].id)
            except:
                _id.append('None')
            try:
                _b = True
                for filter in category.data.filters:
                    for item in filter.items:
                        if item.id == bids.adverts[i].subject:
                            _name.append(item.name)
                            _b = False
                            break
                if _b == True:
                    _name.append('None')
            except:
                _name.append('None')
            try:
                _cpm.append(bids.adverts[i].cpm)
            except:
                _cpm.append('None')
        return Cpm(_id, _name, _cpm)
    
    def to_string(self):
        try:
            strs = []
            for i in range(0, 10):
                strs.append(str(self.cpm[i]) + ' ' + str(self.name[i]) + ' ' + str(self.id[i]))
            return strs
        except:
            return None
