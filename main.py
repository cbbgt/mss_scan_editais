from modules.scan_all_urls.scan_all_urls_presenter import scan_all_urls_presenter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from helpers.get_html_async import get_html_async
from helpers.send_email import send_email

from pyppeteer import launch

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/scan")
async def scan_all_urls():
    response = await scan_all_urls_presenter()
    return (response)


@app.post("/scanUrl")
async def scan_url(data: dict = None):
    print(f"A url que iremos analisar: {data.get('url')}")
    browser = await launch({
        'executablePath': '/usr/bin/chromium',
        'args': ['--no-sandbox'],
        "ignoreHTTPSErrors": True,
        'headless': True
    })

    A = await get_html_async(data.get('url'), browser)

    return [A]


@app.get('/')
def home():
    return ['RADAR DA INOVAÇÃO', 200]
