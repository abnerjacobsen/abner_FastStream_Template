from typing import Annotated

from dishka.integrations.base import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends as FromFastAPI
from fastapi.security import APIKeyHeader

from app import models
from app.usecases import Services


@inject
async def get_current_user(
        token: Annotated[str, FromFastAPI(APIKeyHeader(name='access-token'))],
        services: FromDishka[Services],
) -> models.User | None:
    return await services.user.retrieve_by_token(token)


CurrentUser = Annotated[models.User, FromFastAPI(get_current_user)]
