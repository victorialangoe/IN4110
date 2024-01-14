"""
Task 3

Collecting anniversaries from Wikipedia
"""
from __future__ import annotations

from pathlib import Path
import re
from bs4 import BeautifulSoup

import pandas as pd

from requesting_urls import get_html

# Month names to submit for, from Wikipedia:Selected anniversaries namespace
months_in_namespace = [
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


def extract_anniversaries(html: str, month: str) -> list[str]:
    """Extract all the passages from the html which contain an anniversary, and save their plain text in a list.
        For the pages in the given namespace, all the relevant passages start with a month href
         <p>
            <b>
                <a href="/wiki/April_1" title="April 1">April 1</a>
            </b>
            :
            ...
        </p>

    Parameters:
        - html (str): The html to parse
        - month (str): The month in interest, the page name of the Wikipedia:Selected anniversaries namespace

    Returns:
        - ann_list (list[str]): A list of the highlighted anniversaries for a given month
                                The format of each element in the list is:
                                '{Month} {day}: Event 1 (maybe some parentheses); Event 2; Event 3, something, something\n'
                                {Month} can be any month in the namespace and {day} is a number 1-31
    """
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find_all("p")

    ann_list = []

    for paragraph in paragraphs:
        link = paragraph.find("a", href=re.compile(rf"/wiki/{month}_(\d+)"))
        text = paragraph.get_text().strip()

        if link:
            ann_list.append(text)

    return ann_list


def anniversary_list_to_df(ann_list: list[str]) -> pd.DataFrame:
    """Transform the list of anniversaries into a pandas dataframe.

    Parameters:
        ann_list (list[str]): A list of the highlighted anniversaries for a given month
                                The format of each element in the list is:
                                '{Month} {day}: Event 1 (maybe some parenthesis); Event 2; Event 3, something, something\n'
                                {Month} can be any month in months list and {day} is a number 1-31
    Returns:
        df (pd.Dataframe): A (dense) dataframe with columns ["Date"] and ["Event"] where each row represents a single event
    """

    ann_table = []

    for ann in ann_list:
        parts = ann.split(":", 1)

        if len(parts) > 1:
            date, event = parts
            events = event.split(";")
            for event in events:
                if event.strip():
                    ann_table.append([date, event.strip()])

    headers = ["Date", "Event"]
    df = pd.DataFrame(ann_table, columns=headers)

    return df


def anniversary_table(
    namespace_url: str, month_list: list[str], work_dir: str | Path
) -> None:
    """Given the namespace_url and a month_list, create a markdown table of highlighted anniversaries for all of the months in list,
        from Wikipedia:Selected anniversaries namespace

    Parameters:
        - namespace_url (str):  Full url to the "Wikipedia:Selected_anniversaries/" namespace
        - month_list (list[str]) - List of months of interest, referring to the page names of the namespace
        - work_dir (str | Path) - (Absolute) path to your working directory

    Returns:
        None
    """

    # Loop through all months in month_list
    # Extract the html from the url (use one of the already defined functions from earlier)
    # Gather all highlighted anniversaries as a list of strings
    # Split into date and event
    # Render to a df dataframe with columns "Date" and "Event"
    # Save as markdown table

    work_dir = Path(work_dir)
    output_dir = work_dir / "tables_of_anniversaries"
    output_dir.mkdir(exist_ok=True, parents=True)

    for month in month_list:
        page_url = f"{namespace_url}{month}"
        html = get_html(page_url)

        ann_list = extract_anniversaries(html, month)

        df = anniversary_list_to_df(ann_list)

        table = df.to_markdown(tablefmt="grid")

        output_filepath = output_dir / f"anniversaries_{month}.md"
        with output_filepath.open("w") as f:
            f.write(table)


if __name__ == "__main__":
    # make tables for all the months
    work_dir = "/Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment4"
    namespace_url = "https://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/"
    anniversary_table(namespace_url, months_in_namespace, work_dir)

