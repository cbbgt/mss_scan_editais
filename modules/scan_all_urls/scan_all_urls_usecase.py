
from domain.repositories.foment_instrument_interface import IFomentInstrumentRepository
from typing import Any


class ScanAllUrlsUsecase:
    def __init__(self, repo: IFomentInstrumentRepository) -> None:
        self.repository = repo

    async def __call__(self, *args: Any, **kwds: Any) -> bool:
        await self.repository.scan_all_urls()
        return True
