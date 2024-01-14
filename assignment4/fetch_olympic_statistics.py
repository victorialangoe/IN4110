"""
Task 4

collecting olympic statistics from wikipedia
"""

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup

from requesting_urls import get_html

import re

import matplotlib.pyplot as plt

import numpy as np

# Countries to submit statistics for
scandinavian_countries = ["Norway", "Sweden", "Denmark"]

# Summer sports to submit statistics for
summer_sports = ["Sailing", "Athletics", "Handball", "Football", "Cycling", "Archery"]


def report_scandi_stats(url: str, sports_list: list[str], work_dir: str | Path) -> None:
    """
    Given the url, extract and display following statistics for the Scandinavian countries:

      -  Total number of gold medals for for summer and winter Olympics
      -  Total number of gold, silver and bronze medals in the selected summer sports from sport_list
      -  The best country in number of gold medals in each of the selected summer sports from sport_list

    Display the first two as bar charts, and the last as an md. table and save in a separate directory.

    Parameters:
        url (str) : url to the 'All-time Olympic Games medal table' wiki page
        sports_list (list[str]) : list of summer Olympic games sports to display statistics for
        work_dir (str | Path) : (absolute) path to your current working directory

    Returns:
        None
    """

    # Make a call to get_scandi_stats
    # Plot the summer/winter gold medal stats
    # Iterate through each sport and make a call to get_sport_stats
    # Plot the sport specific stats
    # Make a call to find_best_country_in_sport for each sport
    # Create and save the md table of best in each sport stats

    work_dir = Path(work_dir)
    stats_dir = work_dir / "olympic_games_results"
    stats_dir.mkdir(exist_ok=True, parents=True)

    country_dict = get_scandi_stats(url)
    plot_total_medals(country_dict, stats_dir)

    # Find the best country by gold for each sport and create markdown table
    best_sports = {}

    for sport in sports_list:
        sport_results = {}

        for country, data in country_dict.items():
            medals_for_sport = get_sport_stats(data["url"], sport)
            sport_results[country] = medals_for_sport

        plot_grouped_bar_chart(sport_results, stats_dir, sport)
        best_sports[sport] = find_best_country_in_sport(sport_results)

    with open(stats_dir / "best_of_sport_by_Gold.md", "w") as f:
        f.write("| Sport | Best Country |\n")
        f.write("|-------|--------------|\n")
        for sport, best_country in best_sports.items():
            f.write(f"| {sport} | {best_country} |\n")


def get_scandi_stats(
    url: str,
) -> dict[str, dict[str, str | dict[str, int]]]:
    """Given the url, extract the urls for the Scandinavian countries,
       as well as number of gold medals acquired in summer and winter Olympic games
       from 'List of NOCs with medals' table.

    Parameters:
      url (str): url to the 'All-time Olympic Games medal table' wiki page

    Returns:
      country_dict: dictionary of the form:
        {
            "country": {
                "url": "https://...",
                "medals": {
                    "Summer": 0,
                    "Winter": 0,
                },
            },
        }

        with the tree keys "Norway", "Denmark", "Sweden".
    """

    base_url = "https://en.wikipedia.org"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    table = tables[0]

    if table:
        columns = table.find_all("tr")[2:]
    else:
        print("Couldn't find the table!")
        return {}

    country_dict: dict[str, dict[str, str | dict[str, int]]] = {}

    for column in columns:
        rows = column.find_all("td")
        if not rows:  # if its not < td >,
            continue
        country_link = rows[0].find("a")

        if country_link:
            country_name = country_link.text
        else:
            continue

        country_url = base_url + rows[0].find("a")["href"]

        summer_golds = int(rows[2].text.replace(",", "").strip())
        winter_golds = int(rows[7].text.replace(",", "").strip())

        if country_name in scandinavian_countries:
            country_dict[country_name] = {
                "url": country_url,
                "medals": {
                    "Summer": summer_golds,
                    "Winter": winter_golds,
                },
            }

    print("country dict: ", country_dict)
    return country_dict


def get_sport_stats(country_url: str, sport: str) -> dict[str, int]:
    """Given the url to country specific performance page, get the number of gold, silver, and bronze medals
      the given country has acquired in the requested sport in summer Olympic games.

    Parameters:
        - country_url (str) : url to the country specific Olympic performance wiki page
        - sport (str) : name of the summer Olympic sport in interest. Should be used to filter rows in the table.

    Returns:
        - medals (dict[str, int]) : dictionary of number of medal acquired in the given sport by the country
                          Format:
                          {"Gold" : x, "Silver" : y, "Bronze" : z}
    """
    html = get_html(country_url)
    soup = BeautifulSoup(html, "html.parser")

    span_tag = soup.find("span", id=re.compile("^Medals_by_[Ss]ummer_[Ss]port$", re.I))

    table = span_tag.find_parent().find_parent().find("table", class_="wikitable")

    if not table:
        print("Couldn't find the table!")

    columns = table.find_all("tr")[1:]

    medals = dict()

    for column in columns:
        rows = column.find_all("td")

        if not rows:
            continue

        sport_link = column.find("a")

        if sport_link:
            sport_name = sport_link.text
        else:
            continue

        print("sport name: ", sport_name)

        if sport_name == sport:
            gold = int(rows[0].text.replace(",", "").strip())
            medals["Gold"] = gold
            silver = int(rows[1].text.replace(",", "").strip())
            medals["Silver"] = silver
            bronze = int(rows[2].text.replace(",", "").strip())
            medals["Bronze"] = bronze
            break

    print("medals: ", medals)

    return medals


def find_best_country_in_sport(
    results: dict[str, dict[str, int]], medal: str = "Gold"
) -> str:
    """Given a dictionary with medal stats in a given sport for the Scandinavian countries, return the country
        that has received the most of the given `medal`.

    Parameters:
        - results (dict) : a dictionary of country specific medal results in a given sport. The format is:
                        {"Norway" : {"Gold" : 1, "Silver" : 2, "Bronze" : 3},
                         "Sweden" : {"Gold" : 1, ....},
                         "Denmark" : ...
                        }
        - medal (str) : medal type to compare for. Valid parameters: ["Gold" | "Silver" |"Bronze"]. Should be used as a key
                          to the medal dictionary.
    Returns:
        - best (str) : name of the country(ies) leading in number of gold medals in the given sport
                       If one country leads only, return its name, like for instance 'Norway'
                       If two countries lead return their names separated with '/' like 'Norway/Sweden'
                       If all or none of the countries lead, return string 'None'
    """
    valid_medals = {"Gold", "Silver", "Bronze"}
    if medal not in valid_medals:
        raise ValueError(
            f"{medal} is invalid parameter for ranking, must be in {valid_medals}"
        )

    new_results_dict = {k: v.get(medal, 0) for k, v in results.items()}
    max_value = max(new_results_dict.values())
    keys_with_max_value = [k for k, v in new_results_dict.items() if v == max_value]

    if len(keys_with_max_value) == 1:
        best = keys_with_max_value[0]
    elif len(keys_with_max_value) == 2:
        best = "/".join(sorted(keys_with_max_value))
    else:
        best = "None"

    return best


# Define your own plotting functions and optional helper functions


def plot_scandi_stats(
    country_dict: dict[str, dict[str, str | dict[str, int]]],
    output_parent: str | Path | None = None,
) -> None:
    """Plot the number of gold medals in summer and winter games for each of the scandi countries as bars.

    Parameters:
      country_dict (dict[str, dict[str, int]]) : a nested dictionary of country names and the corresponding number of summer and winter
                            gold medals from 'List of NOCs with medals' table.
                            Format:
                            {"country_name": {"Summer" : x, "Winter" : y}}
      output_parent (Union[str, Path]) : parent file path to save the plot in
    Returns:
      None
    """
    raise NotImplementedError


def plot_total_medals(country_dict, stats_dir):
    """
    Plots the total number of medals for each Scandinavian country in a bar chart.

    Parameters:
        country_dict: Dictionary with data about each country and their medals.
        stats_dir: Path to directory where the plot should be saved.

    Returns:
        None
    """

    n_countries = len(country_dict)
    bar_width = 0.25

    r1 = np.arange(n_countries)
    r2 = [x + bar_width for x in r1]

    countries = list(country_dict.keys())
    summer_medals = [country_dict[country]["medals"]["Summer"] for country in countries]
    winter_medals = [country_dict[country]["medals"]["Winter"] for country in countries]

 
    plt.bar(r1, summer_medals, width=bar_width, color="red", label="Summer")
    plt.bar(r2, winter_medals, width=bar_width, color="blue", label="Winter")

    plt.xlabel("Countries")
    plt.xticks([r + bar_width for r in range(n_countries)], countries)
    plt.ylabel("Total medals")
    plt.title("Total medals per Scandinavian country")
    plt.legend()

    plt.savefig(stats_dir / "total_medal_ranking.png")
    plt.close()


def plot_grouped_bar_chart(sport_results, stats_dir, sport):
    """
    Plots the total number of each medal (gold, silver, bronze) for each Scandinavian country in a bar chart.

    Parameters:
        sport_results: Dictionary with data about each country and their medals.
        stats_dir: Path to directory where the plot should be saved.
        sport: Name of the sport.

    Returns:
        None
    """
    n_countries = len(sport_results)
    bar_width = 0.25

    r1 = np.arange(n_countries)
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    gold = [sport_results[country].get("Gold", 0) for country in sport_results]
    silver = [sport_results[country].get("Silver", 0) for country in sport_results]
    bronze = [sport_results[country].get("Bronze", 0) for country in sport_results]


    plt.bar(r1, gold, width=bar_width, label="Gold")
    plt.bar(r2, silver, width=bar_width, label="Silver")
    plt.bar(r3, bronze, width=bar_width, label="Bronze")

    plt.xlabel("Country")
    plt.xticks([r + bar_width for r in range(n_countries)], sport_results.keys())
    plt.ylabel("Medals")
    plt.title(f"{sport} Medal Ranking")
    plt.legend()

    plt.savefig(stats_dir / f"{sport}_medal_ranking.png")
    plt.close()


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
    work_dir = "/Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment4"
    report_scandi_stats(url, summer_sports, work_dir)
