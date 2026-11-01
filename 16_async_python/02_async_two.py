import asyncio

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    print(f"Brewing Completed {name}...")
    

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai")
    )

asyncio.run(main())