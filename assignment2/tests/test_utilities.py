""" Test script executing all the necessary unit tests for the functions in analytic_tools/utilities.py module
    which is a part of the analytic_tools package
"""

# Include the necessary packages here
from pathlib import Path

import pytest

# This should work if analytic_tools has been installed properly in your environment
from analytic_tools.utilities import (
    get_dest_dir_from_csv_file,
    get_diagnostics,
    is_gas_csv,
    merge_parent_and_basename,
)


@pytest.mark.task12
def test_get_diagnostics(example_config):
    """Test functionality of get_diagnostics in utilities module

    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing the example configuration
                                     from Figure 1 in assignment2.md

    Returns:
    None
    """

    testDict = get_diagnostics(example_config)
    assert testDict["files"] == 10
    assert testDict["subdirectories"] == 5
    assert testDict[".csv files"] == 8
    assert testDict[".npy files"] == 2
    assert testDict[".md files"] == 0
    assert testDict["other files"] == 0


@pytest.mark.task12
@pytest.mark.parametrize(
    "exception, dir",
    [
        (NotADirectoryError, "Not_a_real_directory"),
        (NotADirectoryError, "Not_a_real_file.txt"),
        (TypeError, 12345),
        (TypeError, True),
    ],
)
def test_get_diagnostics_exceptions(
    exception, dir
):  # look on this a bit later when it comes to edge cases....
    """Test the error handling of get_diagnostics function

    Parameters:
        exception (concrete exception): The exception to raise
        dir (str or pathlib.Path): The parameter to pass as 'dir' to the function

    Returns:
        None
    """
    with pytest.raises(exception):
        get_diagnostics(dir)


@pytest.mark.task22
def test_is_gas_csv():
    """Test functionality of is_gas_csv from utilities module

    Parameters:
        None

    Returns:
        None
    """

    CO2 = "assignment2/pollution_data/by_src/src_oil_and_gass/CO2.csv"
    CH4 = "assignment2/pollution_data/by_src/src_oil_and_gass/CH4_mYQ.csv"
    assert is_gas_csv(CO2) == True
    assert is_gas_csv(CH4) == False


@pytest.mark.task22
@pytest.mark.parametrize(
    "exception, path",
    [
        (ValueError, Path(__file__).parent.absolute()),
        (TypeError, 12345),
        (TypeError, True),
        (
            ValueError,
            "assignment2/pollution_data/by_src/src_oil_and_gass/CO2.txt",
        ),
    ],
)
def test_is_gas_csv_exceptions(exception, path):
    """Test the error handling of is_gas_csv function

    Parameters:
        exception (concrete exception): The exception to raise
        path (str or pathlib.Path): The parameter to pass as 'path' to function

    Returns:
        None
    """

    with pytest.raises(exception):
        is_gas_csv(path)


@pytest.mark.task24
def test_get_dest_dir_from_csv_file(example_config):
    """Test functionality of get_dest_dir_from_csv_file in utilities module.

    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing the example configuration
            from Figure 1 in assignment2.md

    Returns:
        None
    """

    gasses = ["CH4", "CO2", "H2"]

    for gas in gasses:
        test_path = example_config / f"{gas}.csv"
        test_path.touch()

        result_path = get_dest_dir_from_csv_file(example_config, test_path)
        print(result_path)  # test by adding flag -s to check the dirs

        assert result_path == example_config / f"gas_{gas}"


@pytest.mark.task24
@pytest.mark.parametrize(
    "exception, dest_parent, file_path",
    [
        (ValueError, Path(__file__).parent.absolute(), "foo.txt"),
        (TypeError, 666, "CO2.csv"),
        (TypeError, Path(__file__).parent.absolute(), 123),
        (
            ValueError,
            Path(__file__).parent.absolute(),
            "foo.jpeg",
        ),
        (
            ValueError,
            Path(__file__).parent.absolute(),
            "NE10.csv",  # Neon
        ),
    ],
)
def test_get_dest_dir_from_csv_file_exceptions(exception, dest_parent, file_path):
    """Test the error handling of get_dest_dir_from_csv_file function

    Parameters:
        exception (concrete exception): The exception to raise
        dest_parent (str or pathlib.Path): The parameter to pass as 'dest_parent' to the function
        file_path (str or pathlib.Path): The parameter to pass as 'file_path' to the function

    Returns:
        None
    """
    with pytest.raises(exception):
        get_dest_dir_from_csv_file(dest_parent, file_path)


@pytest.mark.task26
def test_merge_parent_and_basename():
    """Test functionality of merge_parent_and_basename from utilities module

    Parameters:
        None

    Returns:
        None
    """
    CO2 = "assignment2/pollution_data/by_src/src_oil_and_gass/CO2.csv"  # Testing the same as the previous real locations
    CH4 = "assignment2/pollution_data/by_src/src_oil_and_gass/CH4.csv"
    new_C02 = merge_parent_and_basename(CO2)
    new_CH4 = merge_parent_and_basename(CH4)
    assert new_C02 == "src_oil_and_gass_CO2.csv"
    assert new_CH4 == "src_oil_and_gass_CH4.csv"


@pytest.mark.task26
@pytest.mark.parametrize(
    "exception, path",
    [(TypeError, 33), (ValueError, "/no_file/"), (ValueError, "only_file.csv")],
)
def test_merge_parent_and_basename_exceptions(exception, path):
    """Test the error handling of merge_parent_and_basename function

    Parameters:
        exception (concrete exception): The exception to raise
        path (str or pathlib.Path): The parameter to pass as 'pass' to the function

    Returns:
        None
    """
    with pytest.raises(exception):
        merge_parent_and_basename(path)
