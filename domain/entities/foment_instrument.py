from typing import List
# Entidade
import abc


class FomentInstrument(abc.ABC):
    code: str
    acronym: str
    name: str
    foment_type: List[str]
    edital_url: str
    edital_html: str
    news_url: str
    news_html: str

    def __init__(self, code, acronym, name, foment_type, edital_url, edital_html, news_url, news_html):
        self.code = code
        self.acronym = acronym
        self.name = name
        self.foment_type = foment_type
        self.edital_url = edital_url
        self.edital_html = edital_html
        self.news_url = news_url
        self.news_html = news_html

    @staticmethod
    def from_excel(self):
        pass
        # return FomentInstrument(

        # )

    @staticmethod
    def to_excel(self):
        pass
