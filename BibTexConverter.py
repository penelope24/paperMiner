import re


class BibTexConverter:

    def __init__(self, bib_entry):
        self.entry = bib_entry

    def convert_to_apa(self):
        author = self.entry["author"].replace("\n", " ")
        author = re.sub(r"[{}]", "", author)
        year = self.entry["year"].replace("\n", " ")
        title = self.entry["title"].replace("\n", " ")
        title = re.sub(r"[{}]", "", title)
        journal = self.entry["booktitle"].replace("\n", " ")
        journal = re.sub(r"[{}]", "", journal)
        pages = self.entry["pages"].replace("\n", " ")
        publisher = self.entry["publisher"].replace("\n", " ")
        publisher = re.sub(r"[{}]", "", publisher)

        return author + "(" + year + ")." + title + "." + "In " + journal + "(pp." + pages + ")." + publisher + "."
