"""
Constructs NOC fact and dimension tables.
-----------------------------------------
Name           Created On     Modified On
-----------    ----------     -----------
Schuyler K.    2026-06-24     2026-06-24
"""
import os

class Noc:
    """
    Represents NOC in a snowflake schema. Transforms the csv into the
    dimension and its outrigger tables before loading.
    """
    def __init__(self, file: str):
        self.level_ot: set[int] = set()

        self.__parse_file(file)

    def __parse_file(self, file: str) -> None:
        """
        Parses a file containing NOC classification information and parses
        it into dimensions. Class as a whole represents a fact.
        """
        if not os.path.exists(file):
            raise Exception(f"File '{file}' does not exist.")

        # Encoding is necessary as the data source has a BOM
        with open(file, encoding="utf-8-sig") as f:
            header: list[str] = []

            for i, line in enumerate(f.readlines()):
                row: list[str] = line.split(",")
                header = self.__parse_head(header, row, i)

                # Skip header now
                if i == 0: continue

                self.level_ot.add(self.__parse_level(header, row))
        return

    def __parse_head(self, header: list[str], row: list[str], i: int) -> list[str]:
        """
        Takes a header, a row and a line number and parses and cleans 
        the header from the row if it has not already been done.
        """
        header = row if i == 0 else header
        header = [cell.lower().strip() for cell in header]

        return header


    def __parse_level(self, header: list[str], row: list[str]) -> int:
        """
        Parses a header to find the "Level" column, then parses a row
        to find the level cell.

        Returns the transformed level value.
        """
        level: str = row[header.index("level")].strip()
        if not level.isnumeric():
            raise Exception(f"Column 'level' value <{level}> is not numeric.")

        return int(level)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    noc = Noc(args.file)
    print("NOC Levels\n----------")
    for level in noc.level_ot:
        print(level, end=" ")
    print()

