from pyppeteer import launch
from .reduce_html import reduce_html
from .send_email import send_email


async def get_html(url):
    browser = await launch(headless=True)
    page = await browser.newPage()

    try:
        await page.goto(url, timeout=30000)
        html = await page.evaluate(
            "() => document.body.innerText"
        )
        # html = await page.content()
        await browser.close()
        return html
    except Exception as err:
        send_email(
            'Ocorreu um erro no Radar da Inovação',
            body=f"""
            <h1>Erro no MSS SCAN EDITAIS</h1>
            <p>Tentativa de acesso na URL: {url}</p>
            <p>Erro do console: {err}</p>
            """
        )

    return 'PÁGINA COM ERRO'


async def get_html_async(url):
    html = await get_html(url)
    html = reduce_html(html)
    print(f'TAMANHO DO TEXTO: {len(html)}')
    return html
