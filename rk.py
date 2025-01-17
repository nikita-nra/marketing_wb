from typing import Any
from dataclasses import dataclass
import json
@dataclass
class RK:
    advertId: int
    name: str
    type: int
    status: int
    dailyBudget: int
    createTime: str
    changeTime: str
    startTime: str
    endTime: str

    @staticmethod
    def from_dict(obj: Any) -> 'RK':
        _advertId = int(obj.get("advertId"))
        _name = str(obj.get("name"))
        _type = int(obj.get("type"))
        _status = int(obj.get("status"))
        _dailyBudget = int(obj.get("dailyBudget"))
        _createTime = str(obj.get("createTime"))
        _changeTime = str(obj.get("changeTime"))
        _startTime = str(obj.get("startTime"))
        _endTime = str(obj.get("endTime"))
        return RK(_advertId, _name, _type, _status, _dailyBudget, _createTime, _changeTime, _startTime, _endTime)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
