
from domain.repositories.foment_instrument_interface import IFomentInstrumentRepository
from typing import Any


class ScanAllUrlsUsecase:
    def __init__(self, repo: IFomentInstrumentRepository) -> None:
        self.repository = repo

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.repository.scan_all_urls()
