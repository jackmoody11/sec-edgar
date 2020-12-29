from abc import ABC, abstractmethod


class FilingStrategy(ABC):
    def __init__(self, start_date, end_date, filing_types=None, cik_lookups=None):
        self._start_date = start_date
        self._end_date = end_date
        self._filing_types = filing_types
        self._cik_lookups = cik_lookups

    @abstractmethod
    def get_filings_dict(self):
        pass

    @abstractmethod
    def save(self, directory, dir_pattern=None, file_pattern=None):
        pass
