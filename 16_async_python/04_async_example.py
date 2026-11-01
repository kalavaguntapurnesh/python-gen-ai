import asyncio
import aiohttp

async def fetch_data(session, url):
    
    async with session.get(url) as response:
        return await response.json()
    
async def main():
    
    urls = [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments"
    ]
    
    async with aiohttp.ClientSession() as session:
        
        results = await asyncio.gather(*(fetch_data(session, url) for url in urls))
        
        for result in results:
            print(result)
            
asyncio.run(main())