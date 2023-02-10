#!/usr/bin/env python3

from fastapi import FastAPI
from modelz import expose_models, _render
from uvicorn import run

# must be imported in order to be registered
import models.message
import models.ticket

app = FastAPI()

def main():
    expose_models(app)
    run(app)

if __name__ == "__main__":
    main()