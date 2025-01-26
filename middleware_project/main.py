import logging

from fastapi import FastAPI, Body, Request
from starlette.middleware import Middleware

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import (
  TrustedHostMiddleware,
)

from middleware.asgi_middleware import ASGIMiddleware
#from middleware.asgi_middleware import asgi_middleware

from middleware.request_middleware import HashBodyContentMiddleWare
from middleware.response_middleware import ExtraHeadersResponseMiddleware

from contextlib import asynccontextmanager
from middleware.webhook import WebhookSenderMiddleWare, Event

logger = logging.getLogger("uvicorn")

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield {"webhook_urls": set()}


app = FastAPI(
  title="Middleware App",
  lifespan=lifespan,
  middleware=[
    Middleware(ASGIMiddleware, parameter="ex_param") # as class
   # Middleware(asgi_middleware, parameter="ex_param") # as function decorator
  ]
)

app.add_middleware(
    HashBodyContentMiddleWare,
    allowed_paths=["/send"],
)

app.add_middleware(
    ExtraHeadersResponseMiddleware,
    headers=(
        ("new-header", "fastapi-cookbook"),
        (
            "another-header",
            "fastapi-cookbook",
        ),
    ),
)


@app.get("/")
async def read_root():
    return {"Hello": "Middleware World"}

@app.post("/send")
async def send(message: str = Body()):
    logger.info(f"Message: {message}")
    return message

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost"],
)


@app.post("/register-webhook-url")
async def add_webhook_url(
    request: Request, url: str = Body()
):
    if not url.startswith("http"):
        url = f"http://{url}"
    request.state.webhook_urls.add(url)
    return {"url added": url}


app.add_middleware(
    WebhookSenderMiddleWare,
)


@app.webhooks.post("/fastapi-webhook")
def fastapi_webhook(event: Event):
    """_summary_

    Args:
        event (Event): Received event from webhook
        It contains information about the
        host, path, timestamp and body of the request
    """