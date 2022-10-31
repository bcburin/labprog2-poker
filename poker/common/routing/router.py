from __future__ import annotations
from typing import Callable, Any, Awaitable

HandlerType = Callable[..., Awaitable[Any]]


class Router:

    def __init__(self, *, prefix: str):
        self._prefix = prefix
        self._handlers = {}

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def handlers(self) -> dict[str, HandlerType]:
        return self._handlers

    @property
    def routes(self) -> list[str]:
        return list(self._handlers.keys())

    def add(self, route: str):
        def decorator(handler: HandlerType):
            self._handlers[f'{self.prefix}.{route}'] = handler
            return handler
        return decorator

    def add_router(self, router: Router):
        for route, handler in router.handlers.items():
            nested_route = f'{self.prefix}.{route}'
            self._handlers[nested_route] = handler

    async def do_task(self, route: str, *args, **kwargs):
        if route not in self.routes:
            raise ValueError('No such route.')
        handler = self.handlers[route]
        return handler(*args, **kwargs)


