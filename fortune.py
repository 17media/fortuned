import asyncio
import shlex


class Fortune(object):
    def __await__(self):
        return self.get().__await__()

    async def get(self, lang=None):
        proc = await asyncio.create_subprocess_exec(
            *shlex.split('fortune -s data/{lang}'.format(lang=lang or 'en')),
            stdout=asyncio.subprocess.PIPE,
        )
        data, stderr = await proc.communicate()
        text = data.decode('utf-8').rstrip()
        return text
