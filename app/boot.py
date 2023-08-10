import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, status, HTTPException
import uvicorn
from app.api.url import router as url_router
from app.db_models.url import Url
app = FastAPI()
app.include_router(router=url_router)


@app.get("/{_id}", response_description=f"Redirect to original url")
async def get_one(_id, request: Request):
    from app.core.base62 import Base62
    if _id != 'favicon.ico':
        order = Base62.decode_base_62(_id)
        obj = Url()
        result = obj.list({'order': order})
        if len(result) > 0:
            original_url = result[0].url
            params = request.scope.get("query_string", b"").decode("utf-8")
            final_url = f'{original_url}&{params}'
            result[0].visit()
            return RedirectResponse(url=final_url)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_CONFLICT,
                detail=f'{_id} is not correct',
            )


if __name__ == "__main__":
    uvicorn.run("boot:app", host="0.0.0.0", port=8000, reload=True)
