from modules.scan_all_urls.scan_all_urls_presenter import scan_all_urls_presenter
from fastapi import FastAPI

from helpers.get_html_async import get_html_async
from helpers.send_email import send_email

app = FastAPI()


@app.post("/scan")
async def scan_all_urls():
    response = await scan_all_urls_presenter()
    return (response)


@app.post("/scanUrl")
async def scan_url(data: dict = None):
    print(f"A url que iremos analisar: {data.get('url')}")

    A = await get_html_async(data.get('url'))

    return [A]


@app.post('/sendEmail')
def send_email_via_fastapi(data: dict = None):
    send_email('Teste', '<p>enviando pela fastapi</p>')
    return 200
