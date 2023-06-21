from infra.repositories.foment_instrument_repository_gsheet import FomentInstrumentRepositoryGSheet
from .scan_all_urls_usecase import ScanAllUrlsUsecase
from .scan_all_urls_controller import ScanAllUrlsController

repo_instrument_foment = FomentInstrumentRepositoryGSheet()
usecase = ScanAllUrlsUsecase(repo=repo_instrument_foment)
controller = ScanAllUrlsController(usecase=usecase)


def scan_all_urls_presenter(request):

    controller(request=request)

    return ("Ok", 200, headers)
