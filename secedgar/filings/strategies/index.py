from secedgar.filings.strategies import FilingStrategy


class IndexFilingStrategy(FilingStrategy):
    def __init__(self, start_date, end_date, filing_types, cik_lookups):
        super().__init__(start_date, end_date, filing_types=filing_types, cik_lookups=cik_lookups)

    def get_master_idx_file(self):
        pass  # TODO: Implement this
