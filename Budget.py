from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Budget:
    cash: int
    netting: int
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'Budget':
        _cash = int(obj.get("cash"))
        _netting = int(obj.get("netting"))
        _total = int(obj.get("total"))
        return Budget(_cash, _netting, _total)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
