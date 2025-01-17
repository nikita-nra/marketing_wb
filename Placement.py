from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class Budget:
    dailyMax: int
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'Budget':
        _dailyMax = int(obj.get("dailyMax"))
        _total = int(obj.get("total"))
        return Budget(_dailyMax, _total)
    
    def get_json(self):
        d = {
            "total": self.total,
            "dailyMax": self.dailyMax
        }
        return d
    
@dataclass
class Intervals:
    begin: int
    end: int

    @staticmethod
    def from_dict(obj: Any) -> 'Intervals':
        _begin = int(obj.get("begin"))
        _end = int(obj.get("end"))
        return Intervals(_begin, _end)
    
    def get_json(self):
        d = {
            "begin": self.begin,
            "end": self.end
        }
        return d
    
@dataclass
class Info:
    count: int
    place: int
    price: int

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        _count = int(obj.get("count"))
        _place = int(obj.get("place"))
        _price = int(obj.get("price"))
        return Info(_count, _place, _price)
    
    def get_json(self):
        d = {
            "place": self.place,
            "price": self.price,
            "count": self.count
        }
        return d

@dataclass
class PlacesInfo:
    entryPrices: List[int]
    estimatedPlace: List[Any]
    info: List[Info]

    @staticmethod
    def from_dict(obj: Any) -> 'PlacesInfo':
        _entryPrices = [y for y in obj.get("entryPrices")]
        #if str(obj.get("estimatedPlace")) == 'None':
        _estimatedPlace = str(obj.get("estimatedPlace"))
        _info = [Info.from_dict(y) for y in obj.get("info")]
        return PlacesInfo(_entryPrices, _estimatedPlace, _info)
    
    def get_json(self):
        d = {
            #исправить
            #"estimatedPlace": self.estimatedPlace,
            "estimatedPlace": [],
            "entryPrices": self.entryPrices,
            "info": [Info.get_json(y) for y in self.info]
        }
        return d
    
@dataclass
class SearchElements:
    active: bool
    brand: str
    name: str
    nm: int
    stock: bool

    @staticmethod
    def from_dict(obj: Any) -> 'SearchElements':
        _active = bool(obj.get("active"))
        _brand = str(obj.get("brand"))
        _name = str(obj.get("name"))
        _nm = int(obj.get("nm"))
        _stock = bool(obj.get("stock"))
        return SearchElements(_active, _brand, _name, _nm, _stock)
    
    def get_json(self):
        d = {
            "nm": self.nm,
            "name": self.name,
            "brand": self.brand,
            "active": self.active,
            "stock": self.stock
        }
        return d

@dataclass
class Places:
    dailyBudget: int
    #excludedWords: str
    excludedWords: json
    intervals: List[Any]
    keyWord: str
    placesInfo: PlacesInfo
    price: int
    searchElements: List[SearchElements]
    subjectId: int

    @staticmethod
    def from_dict(obj: Any) -> 'Places':
        _dailyBudget = int(obj.get("dailyBudget"))
        _excludedWords = json.dumps(obj.get("excludedWords"))
        #if str(obj.get("intervals")) == 'None':
        #    _excludedWords = str("null")
        #else:
        #    _excludedWords = str(obj.get("excludedWords"))

        if str(obj.get("intervals")) == 'None':
            _intervals = json.dumps(obj.get("intervals"))
        else:
            _intervals = [Intervals.from_dict(y) for y in obj.get("intervals")]

        _keyWord = str(obj.get("keyWord"))
        _placesInfo = PlacesInfo.from_dict(obj.get("placesInfo"))
        _price = int(obj.get("price"))
        _searchElements = [SearchElements.from_dict(y) for y in obj.get("searchElements")]
        _subjectId = int(obj.get("subjectId"))
        return Places(_dailyBudget, _excludedWords, _intervals, _keyWord, _placesInfo, _price, _searchElements, _subjectId)
    
    def get_json(self):
        if self.intervals == 'null':
            intervals = None
        else:
            intervals = [Intervals.get_json(y) for y in self.intervals]
        
        if self.excludedWords == 'null':
            excludedWords = None
        else:
            excludedWords = self.excludedWords
        d = {
            "keyWord": self.keyWord,
            "subjectId": self.subjectId,
            "price": self.price,
            "placesInfo": PlacesInfo.get_json(self.placesInfo),
            "searchElements": [SearchElements.get_json(y) for y in self.searchElements],
            "dailyBudget": self.dailyBudget,
            "intervals": intervals,
            "excludedWords": excludedWords,
            "is_active": True
        }
        return d

@dataclass
class Place:
    budget: Budget
    fixed: bool
    limited: bool
    locale: List[int]
    minCPM: int
    name: str
    nmsCount: int
    place: List[Places]
    status: int
    stepCPM: int

    @staticmethod
    def from_dict(obj: Any) -> 'Place':
        _budget = Budget.from_dict(obj.get("budget"))
        _fixed = bool(obj.get("fixed"))
        _limited = bool(obj.get("limited"))
        _locale = [y for y in obj.get("locale")]
        _minCPM = int(obj.get("minCPM"))
        _name = str(obj.get("name"))
        _nmsCount = int(obj.get("nmsCount"))
        _place = [Places.from_dict(y) for y in obj.get("place")]
        _status = int(obj.get("status"))
        _stepCPM = int(obj.get("stepCPM"))
        return Place(_budget, _fixed, _limited, _locale, _minCPM, _name, _nmsCount, _place, _status, _stepCPM)
    
    def get_json(self):  
        d = {
            "budget": Budget.get_json(self.budget),
            "minCPM": self.minCPM,
            "stepCPM": self.stepCPM,
            "locale": self.locale,
            "place": [Places.get_json(y) for y in self.place],
            "limited": self.limited,
            "nmsCount": self.nmsCount,
            "name": self.name,
            "status": self.status,
            "fixed": self.fixed,
            "excludedBrands": []
        }
        return d