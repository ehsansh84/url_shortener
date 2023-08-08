from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder

from app.api_models.url import Write
from app.db_models.url import Url as DataModel

module_name = 'url'
module_text = 'Url'
router = APIRouter(
    prefix=f"/{module_name}",
    tags=[module_name]
)


# @router.post("/", response_description=f"Create a {module_text}", status_code=status.HTTP_201_CREATED, response_model=OutputCreate)
@router.post("/", response_description=f"Create a {module_text}", status_code=status.HTTP_201_CREATED)
async def create(item: Write):
        obj = DataModel()
        obj.set_payload(jsonable_encoder(item))
        if obj.exists('url', obj.url):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'{obj.url} already exists!',
            )
        _id = obj.insert()
        return {
            'detail': f'{module_text} created.',
            'data': {
                'id': str(_id),
            }
        }


