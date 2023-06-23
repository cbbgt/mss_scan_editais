
from typing import Any
from modules.scan_all_urls.scan_all_urls_usecase import ScanAllUrlsUsecase
from helpers.external_interfaces.external_interface import IRequest, IResponse


class ScanAllUrlsController:
    def __init__(self, usecase: ScanAllUrlsUsecase) -> None:
        self.ScanAllUrlsUsecase = usecase

    async def __call__(self, request: IRequest) -> IResponse:
        try:
            print("cheguei antes do usecase")
            await self.ScanAllUrlsUsecase()
        except Exception as err:
            print(f"Erro no arquivo scan_all_urls_controller.py): {err}")
