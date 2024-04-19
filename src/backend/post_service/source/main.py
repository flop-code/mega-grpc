from pydantic import ValidationError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from grpc import RpcError, StatusCode as GRPCStatusCode

from exceptions import UnauthorizedError
from config import settings
from router import router


app = FastAPI(
    title="Mega-gRPC Post Service",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    root_path="/api/post",
)


@app.exception_handler(ValidationError)
async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"details": str(exc)}
    )


@app.exception_handler(RpcError)
async def rpc_error_handler(request: Request, exc: RpcError):
    if exc.code() == GRPCStatusCode.UNAUTHENTICATED:
        raise UnauthorizedError()
    else:
        raise exc


app.include_router(router)

origins = [settings.FRONTEND_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],
    allow_headers=[
        "Content-Type", "Set-Cookie",
        "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
    ],
)
