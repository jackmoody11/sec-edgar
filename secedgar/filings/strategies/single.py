from secedgar.filings.strategies import FilingStrategy


class SingleCIKFilingStrategy(FilingStrategy):
    def __init__(self, start_date, end_date, filing_types, cik_lookups):
        super().__init__(start_date, end_date, filing_types=filing_types, cik_lookups=cik_lookups)
