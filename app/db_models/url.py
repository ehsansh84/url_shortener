from typing import List
from app.core.base_db import DB

module_name = 'url'
module_text = 'Url'


class Url(DB):
    f"""
    Use this model to manage a {module_text}
    """

    def __init__(self, _id=None, module_name=module_name, module_text=module_text, db=None, user_id='', name=''):
        self._id: str = _id
        self.original_url: str = user_id
        self.url: str = name
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


