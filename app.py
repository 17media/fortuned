import os
import asyncio
import aiohttp.web
import aioredis


async def handle(request):
    # print(request.app)
    proc = await asyncio.create_subprocess_exec('fortune', '-s', stdout=asyncio.subprocess.PIPE)
    data, stderr = await proc.communicate()
    # exit = proc.wait()
    text = data.decode('utf-8').rstrip()

    # with (await pool) as redis:
    #     await redis.set('en', text)
    #     # print((yield from redis.get('my-key')))

    # await exit
    return aiohttp.web.Response(text=text)

# async def wshandler(request):
#     ws = web.WebSocketResponse()
#     await ws.prepare(request)
#
#     async for msg in ws:
#         if msg.type == web.MsgType.text:
#             ws.send_str("Hello, {}".format(msg.data))
#         elif msg.type == web.MsgType.binary:
#             ws.send_bytes(msg.data)
#         elif msg.type == web.MsgType.close:
#             break
#
#     return ws




async def main():
    app = aiohttp.web.Application()
    # app.router.add_get('/echo', wshandler)
    app.router.add_get('/', handle)
    # app.router.add_get('/{name}', handle)

    pool = await aioredis.create_pool(
        ('localhost', 6379),
        minsize=5, maxsize=10,
    )
    aiohttp.web.run_app(app)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    # async with pool.get() as conn:
    #     value = await conn.get('my-key')
    #     print('raw value:', value)
