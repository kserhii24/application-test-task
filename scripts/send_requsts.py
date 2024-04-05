import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100):
            task = asyncio.create_task(fetch(session, "http://127.0.0.1/payload"))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

if __name__ == "__main__":
    asyncio.run(main())
