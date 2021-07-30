from bs4 import BeautifulSoup
import json
import re
import requests
from RequestMask import RequestMask
from BibTexConverter import BibTexConverter
from tqdm import tqdm


class AuthorInstParser:

    def __init__(self, entries, parse_type, upper_bound, lower_bound, output_path):
        self.entries = entries
        self.parse_type = parse_type
        self.parse_parse_type()
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.prefix = "http://dx.doi.org"
        self.suffix = "#pill-authors__contentcon"
        self.masked_header = RequestMask.make_mask_header()
        self.output_path = output_path

    def parse_parse_type(self):
        entry = self.entries[0]
        pub = entry["publisher"]
        if str(pub).__contains__("ACM"):
            self.parse_type = 0
        if str(pub).__contains__("IEEE"):
            self.parse_type = 1

    def process(self):
        with open(self.output_path, "w") as f:
            for entry in self.entries:
                if entry.get("doi") is not None and entry.get("author") is not None:
                    doi = entry["doi"]
                    # author_list = []
                    # inst_list = []
                    if self.parse_type == 1:
                        url = self.prefix + "/" + doi
                        doc = requests.get(url, headers=self.masked_header).text
                        author_list, inst_list = AuthorInstParser.find_author_info(doc)
                    else:
                        url = self.prefix + "/" + doi + self.suffix
                        doc = requests.get(url, headers=self.masked_header).text
                        author_list, inst_list = AuthorInstParser.find_author_info2(doc)

                    if AuthorInstParser.judge(author_list, inst_list):
                        bib_converter = BibTexConverter(entry)
                        txt = bib_converter.convert_to_apa()
                        print(txt)
                        f.write(txt)
                        f.write("\n")

    @staticmethod
    def judge(author_list, inst_list):
        first_author = author_list[0]
        first_author_inst = inst_list[0]
        first_author_inst = str(first_author_inst)
        if first_author_inst.lower().__contains__("china") or first_author_inst.lower().endswith("china"):
            return True
        return False

    """return author_list, inst_list"""
    @staticmethod
    def find_author_info(doc):
        author_list = []
        inst_list = []
        soup = BeautifulSoup(doc, "html.parser")
        tgt_div = None
        for tag in soup.find_all("script"):
            if str(tag).__contains__("xplGlobal.document.metadata"):
                tgt_div = tag
        assert tgt_div is not None
        s = tgt_div.contents[0]
        p = re.compile("xplGlobal.document.metadata=(.*)};")
        m = re.search(p, str(s))
        author_info = m.group(1) + "}"
        json_boj = json.loads(author_info)
        authors = json_boj["authors"]
        for author in authors:
            author_list.append(author["name"])
            inst_list.append(author["affiliation"])
        assert len(author_list) == len(inst_list)
        return author_list, inst_list

    """return author list, inst list"""
    @staticmethod
    def find_author_info2(doc):
        author_list = []
        inst_list = []
        soup = BeautifulSoup(doc, "html.parser")
        ul = soup.find("ul", attrs={"ariaa-label": "authors"})
        li_list = ul.find_all("li", class_="loa__item")
        for li in li_list:
            author_name = li.a["title"]
            span = li.find("span", class_="loa_author_inst")
            if span.find("p") is not None:
                author_inst = span.find("p").contents[0]
            else:
                author_inst = ""
            # print(author_name)
            # print(author_inst)
            author_list.append(author_name)
            inst_list.append(author_inst)
        assert len(author_list) == len(inst_list)
        return author_list, inst_list


# if __name__ == "__main__":
#     doi = "10.1145/1368088.1368180"
#     parser = AuthorInstParser([doi], 1, None, None)
#     parser.process()
