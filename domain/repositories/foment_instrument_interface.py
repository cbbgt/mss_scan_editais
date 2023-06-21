
from abc import ABC, abstractmethod
from typing import List, Tuple
from domain.entities.foment_instrument import FomentInstrument


class IFomentInstrumentRepository(ABC):  # todo implementar os metodos

    @abstractmethod
    def scan_all_urls(self):
        pass

    @abstractmethod
    def get_all_foment_instruments(self) -> List[FomentInstrument]:
        pass

    @abstractmethod
    def get_foment_instrument_by_code(self, fomentInstrumentCode: str) -> FomentInstrument:
        pass

    @abstractmethod
    def update_foment_instrument(self, fomentInstrumentCode: str, newState: FomentInstrument) -> FomentInstrument:
        pass

    # To Do
    # @abstractmethod
    # def create_foment_instrument(self, fomentInstrument: FomentInstrument) -> FomentInstrument:
    #     pass

    # @abstractmethod
    # def delete_foment_instrument(self, fomentInstrumentCode: str) -> bool:
    #     pass
