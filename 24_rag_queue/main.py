from dotenv import load_dotenv

import uvicorn


def main():
    load_dotenv()
    from .server import app

    uvicorn.run(app, port=8000, host="0.0.0.0")


main()