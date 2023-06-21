
from typing import Any
from modules.scan_all_urls.scan_all_urls_usecase import ScanAllUrlsUsecase
from helpers.external_interfaces.external_interface import IRequest, IResponse


class ScanAllUrlsController:
    ScanAllUrlsUsecase: ScanAllUrlsUsecase

    def __init__(self, usecase: ScanAllUrlsUsecase) -> None:
        self.ScanAllUrlsUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            ScanAllUrlsUsecase()
        except Exception as err:
            print(err)
