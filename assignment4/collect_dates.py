"""
Task 2 (IN4110 only)

parsing dates from wikipedia
"""

from __future__ import annotations

import re

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_date_patterns() -> tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """
    months_block = [
        r"\b[jJ]an(?:uary)?\b",
        r"\b[fF]eb(?:ruary)?\b",
        r"\b[mM]ar(?:ch)?\b",
        r"\b[aA]pr(?:il)?\b",
        r"\b[mM]ay\b",
        r"\b[jJ]un(?:e)?\b",
        r"\b[jJ]ul(?:y)?\b",
        r"\b[aA]ug(?:ust)?\b",
        r"\b[sS]ep(?:tember)?\b",
        r"\b[oO]ct(?:ober)?\b",
        r"\b[nN]ov(?:ember)?\b",
        r"\b[dD]ec(?:ember)?\b",
    ]
    months = r"(?:" + "|".join(months_block) + ")"

    day = r"\d{1,2}"
    year = r"\d{4}"

    return year, months, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """

    if s.isdigit():
        if len(s) == 2:
            return s
        return s.zfill(2)

    s = s.capitalize()

    return str(month_names.index(s) + 1).zfill(2)


def zero_pad(n: str):
    """zero-pad a number string

    arguments:
        n (str) : number
    returns:
        n (str) : zero-padded number string
    """
    return n.zfill(2)


def find_dates(text: str, output: str | None = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
        output (str, Optional) : The file to write the output to if wanted
    return:
        results (List): A list with all the dates found
    """
    year, month, day = get_date_patterns()

    DMY = rf"({day})\s({month})\s({year})"
    MDY = rf"({month})\s({day}),?\s({year})"
    YMD = rf"({year})\s({month})\s({day})"
    ISO = rf"({year})-(\d{{2}})-({day})"

    dates = []

    for match in re.findall(DMY, text):
        d, m, y = match
        dates.append(f"{y}/{convert_month(m)}/{zero_pad(d)}")

    for match in re.findall(MDY, text):
        m, d, y = match
        dates.append(f"{y}/{convert_month(m)}/{zero_pad(d)}")

    for match in re.findall(YMD, text):
        y, m, d = match
        dates.append(f"{y}/{convert_month(m)}/{zero_pad(d)}")

    for match in re.findall(ISO, text):
        y, m, d = match
        dates.append(f"{y}/{m}/{zero_pad(d)}")

    if output:
        with open(output, "w") as f:
            for date in dates:
                f.write(date + "\n")

    return dates
