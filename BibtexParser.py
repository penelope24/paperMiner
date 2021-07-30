import bibtexparser
from BibTexConverter import BibTexConverter


class BibtexParser:

    def __init__(self, bib_path):
        self.path = bib_path
        self.bib_database = None
        with open(self.path, "r") as f:
            self.bib_database = bibtexparser.load(f)
        assert self.bib_database is not None

    def __iter__(self):
        for entry in self.bib_database.entries:
            # if entry.get("doi") is not None and entry.get("author") is not None:
            #     doi = entry["doi"]
            #     yield doi
            yield entry

    def __len__(self):
        return len(self.bib_database)


if __name__ == "__main__":
    path = "C:\\Users\\fy\\Desktop\\icses\\icse2015.bib"
    with open(path, "r") as f:
        bib_database = bibtexparser.load(f)
        for entry in bib_database.entries:
            bib_converter = BibTexConverter(entry)
            print(bib_converter.convert_to_apa())