import os
import asyncio
import aiohttp.web
import fortune


async def handle(request):
    message = await request.app['fortune']
    return aiohttp.web.Response(text=message)


async def init_fortune(app):
    app['fortune'] = fortune.Fortune()


def make_app():
    app = aiohttp.web.Application()
    app.on_startup.append(init_fortune)
    app.router.add_get('/', handle)
    return app


if __name__ == '__main__':
    aiohttp.web.run_app(make_app())
