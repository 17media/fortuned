import asyncio


class Fortune(object):
    def __await__(self):
        return self.get().__await__()

    async def get(self):
        proc = await asyncio.create_subprocess_exec('fortune', '-s', stdout=asyncio.subprocess.PIPE)
        data, stderr = await proc.communicate()
        text = data.decode('utf-8').rstrip()
        return text
