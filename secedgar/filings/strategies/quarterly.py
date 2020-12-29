from secedgar.filings.strategies import IndexFilingStrategy


class QuarterlyFilingStrategy(IndexFilingStrategy):
    def __init__(self, start_date, end_date, filing_types, cik_lookups):
        super().__init__(start_date, end_date, filing_types, cik_lookups)
