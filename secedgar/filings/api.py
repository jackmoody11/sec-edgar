from secedgar.filings import CIKLookup, FilingType
from secedgar.filings.strategies import (DailyFilingStrategy,
                                         QuarterlyFilingStrategy,
                                         SingleCIKFilingStrategy)
from secedgar.utils import sanitize_date
from secedgar.utils.exceptions import FilingTypeError


class Filings:
    def __init__(self, start_date, end_date, filing_types=None, cik_lookups=None):
        self._start_date = start_date
        self._end_date = end_date
        self._filing_types = filing_types
        self._cik_lookups = cik_lookups

        # Choose which strategy will be used here
        if filing_types is None and cik_lookups is None:
            self._strategy = SingleCIKFilingStrategy()

    @property
    def start_date(self):
        """Union([datetime.datetime, str]): Date before which no filings are fetched."""
        return self._start_date

    @start_date.setter
    def start_date(self, val):
        if val is not None:
            self._start_date = val
            self._params['datea'] = sanitize_date(val)
        else:
            self._start_date = None

    @property
    def end_date(self):
        """Union([datetime.datetime, str]): Date after which no filings are fetched."""
        return self._end_date

    @end_date.setter
    def end_date(self, val):
        self._end_date = val
        self._params['dateb'] = sanitize_date(val)

    @property
    def filing_type(self):
        """``secedgar.filings.FilingType``: FilingType enum of filing."""
        return self._filing_type

    @filing_type.setter
    def filing_type(self, filing_type):
        if not isinstance(filing_type, FilingType):
            raise FilingTypeError
        self._filing_type = filing_type
        self._params['type'] = filing_type.value

    @property
    def cik_lookup(self):
        """``secedgar.filings.cik_lookup.CIKLookup``: CIKLookupobject."""
        return self._cik_lookup

    @cik_lookup.setter
    def cik_lookup(self, val):
        if not isinstance(val, CIKLookup):
            val = CIKLookup(val)
        self._cik_lookup = val

    def get_filings_dict(self):
        pass

    def save(self, directory, dir_pattern=None, file_pattern=None):
        """Save files in specified directory.

        Args:
            directory (str): Path to directory where files should be saved.
            dir_pattern (str): Format string for subdirectories. Default is "{cik}/{type}".
                Valid options are {cik} and/or {type}.
            file_pattern (str): Format string for files. Default is "{accession_number}".
                Valid options are {accession_number}.

        Returns:
            None

        Raises:
            ValueError: If no text urls are available for given filing object.
        """
        pass
