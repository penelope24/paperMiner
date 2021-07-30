from BibtexParser import BibtexParser
from AuthorInstParser import AuthorInstParser


if __name__ == "__main__":
    for i in range(2006, 2007):
        year = i
        if year != 2010 and year != 2015:
            print("now at year: ", year)
            BASE_PATH = "C:\\Users\\fy\\Desktop\\icses"
            output_path = BASE_PATH + "\\results\\" + str(year) + ".txt"
            bib_file = BASE_PATH + "\\icse" + str(year) + ".bib"
            parse_type = -1
            if year % 2 == 0:
                parse_type = 0
            else:
                parse_type = 1
            bib_parser = BibtexParser(bib_file)
            entries = []
            for entry in bib_parser:
                entries.append(entry)
            auth_parser = AuthorInstParser(entries, parse_type, None, None, output_path)
            auth_parser.process()
