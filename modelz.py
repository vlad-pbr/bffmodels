from typing import List
from dataclasses import is_dataclass, fields
from fastapi import FastAPI
from fastapi.responses import Response

"""
Very cool BFF shared model thing.
"""

_models_list: List[type] = []

py_to_ts = {
    str: "string",
    int: "number",
    bool: "boolean"
}
nl = chr(10)
ht = chr(9)

def modelz(cls: type) -> type:

    if is_dataclass(cls):
        _models_list.append(cls)

    return cls

def expose_models(app: FastAPI) -> None:

    @app.get("/models")
    def _route():
        return Response(
            content=_render(),
            headers={
                "Content-Type": "text/javascript"
            }
        )
    
def _render() -> str:

    def _render_model(_m: type) -> str:
        return f"interface {_m.__name__} {{{nl}{nl.join([ f'{ht}{field.name}: {py_to_ts.get(field.type)};' for field in fields(_m) ])}{nl}}}{nl}export default {_m.__name__};"
    
    return f"{nl}{nl}".join([ _render_model(m) for m in _models_list ])