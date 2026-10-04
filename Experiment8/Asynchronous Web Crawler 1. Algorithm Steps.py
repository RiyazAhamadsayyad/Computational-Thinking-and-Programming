import asyncio
import aiohttp
import time

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

async def fetch(session, url):
    for _ in range(3):
        try:
            async with session.get(url, timeout=5) as r:
                return r.status
        except:
            await asyncio.sleep(1)
    return "Failed"

async def async_crawler():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )

start = time.time()
result = asyncio.run(async_crawler())
print("Async:", result)
print("Time:", round(time.time() - start, 2), "seconds")
