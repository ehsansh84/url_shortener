import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from fastapi import FastAPI
import uvicorn
from app.api.url import router as url_router
from app.db_models.url import Url
app = FastAPI()
app.include_router(router=url_router)


@app.get("/{_id}", response_description=f"Redirect to original url")
async def get_one(_id):
    from app.core.base62 import Base62
    if _id != 'favicon.ico':
        order = Base62.decode_base_62(_id)
        obj = Url()
        result = obj.list({'order': order})
        print(result[0])
        print(len(result))
    #
    # if obj.is_loaded():
    #     return obj.to_json()
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f'{module_text} with id {_id} not found!',
    #     )


if __name__ == "__main__":
    uvicorn.run("boot:app", host="0.0.0.0", port=8000, reload=True)
