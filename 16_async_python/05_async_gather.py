import asyncio

async def download_file(file_name):
    print(f"Downloading {file_name}")

    await asyncio.sleep(2)

    print(f"{file_name} downloaded")

async def main():

    await asyncio.gather(
        download_file("file1.pdf"),
        download_file("file2.pdf"),
        download_file("file3.pdf")
    )

asyncio.run(main())