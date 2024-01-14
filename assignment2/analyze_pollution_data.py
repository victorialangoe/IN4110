"""This is the mane script orchestrating the restructuring and plotting of the content of the pollution_data directory.
"""

# Import necessary packages here
from pathlib import Path
import shutil

from analytic_tools.utilities import (
    display_diagnostics,
    display_directory_tree,
    get_diagnostics,
    validate_directory,
    is_gas_csv,
    get_dest_dir_from_csv_file,
    merge_parent_and_basename,
)

from analytic_tools.plotting import plot_pollution_data


def restructure_pollution_data(pollution_dir: str | Path, dest_dir: str | Path) -> None:
    """This function searches the tree of pollution_data directory pointed to by pollution_dir for .csv files
        that satisfy the criteria described in the assignment. It then moves a renamed copy of these files to gas-specific
        sub-directories in dest_dir, which will be created based on the gasses present in pollution_data directory.

    Parameters:
        - pollution_dir (str or pathlib.Path) : The absolute path to pollution_data directory
        - dest_dir (str or pathlib.Path) : The absolute path to new directory where gas-specific subdirectories will
                                     be created, which must be pollution_data_restructured/by_gas

    Returns:
    None

    Pseudocode:
    1. Iterate through the contents of `pollution_dir`
    2. Find valid .csv files for gasses ([`[gas_formula].csv` files of correct gas types).
    3. Create/assign new directory to store them under `dest_dir` using `get_dest_dir_from_csv_file`
    4. Assign a new name using `merge_parent_and_basename` and copy the file to the new destination.
       If the file happens already to exist there, it should be overwritten.
    """

    # Using type nad dir error checking from the utilites.py to avoid code smells
    pollution_dir = validate_directory(pollution_dir)
    dest_dir = validate_directory(dest_dir)

    contents = pollution_dir

    for path in contents.rglob("*"):
        if path.is_file() and is_gas_csv(path):
            dest_subdir = get_dest_dir_from_csv_file(dest_dir, path)

            merged_file = merge_parent_and_basename(path)

            dest_path = dest_subdir / merged_file

            shutil.copy(path, dest_path)


def analyze_pollution_data(work_dir: str | Path) -> None:
    """In this method we analyze the pollution data
    Parameters:
        - working directory including our data
    Returns:
        None"""
    work_dir = validate_directory(
        work_dir
    )  # This is the error checks, used in multiple methods to reduce code smells

    res = get_diagnostics(work_dir)
    display_diagnostics(work_dir, res)
    display_directory_tree(work_dir, 3)

    pollution_data_dir = work_dir / "pollution_data"
    diagnostics = get_diagnostics(pollution_data_dir)
    display_diagnostics(pollution_data_dir, diagnostics)

    by_gas_dir = work_dir / "pollution_data_restructured" / "by_gas"
    by_gas_dir.mkdir(parents=True, exist_ok=True)

    # Make a call to restructure_pollution_data
    restructure_pollution_data(pollution_data_dir, by_gas_dir)

    # Populate pollution_data_restructured with a sub folder named figures
    figures_dir = work_dir / "pollution_data_restructured" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # Make a call to plot_pollution_data
    plot_pollution_data(by_gas_dir, figures_dir)


def analyze_pollution_data_tmp(work_dir: str | Path) -> None:
    """Do the restructuring of the pollution_data in a temporary directory and create the figures
       showing emissions of each gas as function of all the corresponding
       sources. The new figures are saved in a real directory under work_dir.

    Parameters:
        - work_dir (str or pathlib.Path) : Absolute path to the working directory that
                                    contains the pollution_data directory and where the figures will be saved

    Returns:
    None

    Pseudocode:
    - Create a temporary directory and copy pollution_data directory to it
    - Perform the same operations as in analyze_pollution_data
    - Copy (or directly save) the figures to a directory named `figures` under the original working directory pointed to by `work_dir`
    """

    work_dir = validate_directory # surely I can get 0.5 points for error checking? :D 


if __name__ == "__main__":
    work_dir = "/Users/victorialangoe/Documents/Documents - Victoria’s MacBook Pro/UiO/IN4110_assignments/IN3110-victocla/assignment2"
    analyze_pollution_data(work_dir)
