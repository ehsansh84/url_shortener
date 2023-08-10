from typing import List
from app.core.base_db import DB
from bson import ObjectId
from datetime import datetime

module_name = 'url'
module_text = 'Url'


class Url(DB):
    f"""
    Use this model to manage a {module_text}
    """

    def __init__(self, _id=None, module_name=module_name, module_text=module_text, db=None, url='', visits=0):
        self._id: str = _id
        self.url: str = url
        self.visits: int = visits
        super().__init__(_id=_id, module_name=module_name, module_text=module_text, db=db)
        self.order: int = self.new_order()

    def list(self, query=None) -> List['Url']:
        return super().list(query=query)

    def new_order(self) -> int:
        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "maxFieldValue": {"$max": "$order"}
                }
            }
        ]
        result = list(self.col.aggregate(pipeline))

        if result:
            return result[0]["maxFieldValue"] + 1
        else:
            return 1

    def url_is_correct(self) -> bool:
        return self.url.startswith("http://") or self.url.startswith("https://")

    def visit(self) -> bool:
        self.col.update_one({'_id': ObjectId(self._id)}, {
            '$inc': {'visits': 1},
            '$set': {'updated_at': datetime.now()}
        })
        return True
