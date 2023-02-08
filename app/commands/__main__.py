import typer
import requests

from app.config import settings

app = typer.Typer()


@app.command()
def alert():
    response = requests.post(settings.WEBHOOK_URL, json={"text": "Hello, World!"})


if __name__ == "__main__":
    app()
