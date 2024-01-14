"""Module containing functions used to achieve the desired restructuring of the pollution_data directory
"""
import os
from pathlib import Path
from typing import Dict, List


def validate_directory(dir: str | Path) -> Path:
    """This is a helper-method that I created so that I dont have to duplicate alot of code, some methods require different fail checks
    so I have not implemented all of the error handling needed for the whole assigment, but the ones that are usually used
    """
    if isinstance(dir, str):
        dir = Path(dir)
    elif not isinstance(dir, Path):
        raise TypeError(f"Expected path object, but received {type(dir).__name__}")

    if not dir.exists():
        raise NotADirectoryError(f"This path {dir} does not exist")

    if not dir.is_dir():
        raise NotADirectoryError(
            f"Did not get a directory, but received {type(dir).__name__}"
        )

    return dir


def get_diagnostics(dir: str | Path) -> Dict[str, int]:
    """Get diagnostics for the directory tree, with root directory pointed to by dir.
       Counts up all the files, subdirectories, and specifically .csv, .txt, .npy, .md and other files in the whole directory tree.

    Parameters:
        dir (str or pathlib.Path) : Absolute path to the directory of interest

    Returns:
        res (Dict[str, int]) : a dictionary of the findings with following keys: files, subdirectories, .csv files, .txt files, .npy files, .md files, other files.

    """

    dir = validate_directory(dir)

    res = {
        "files": 0,
        "subdirectories": 0,
        ".csv files": 0,
        ".txt files": 0,
        ".npy files": 0,
        ".md files": 0,
        "other files": 0,
    }

    for path in dir.rglob("*"):
        if path.is_file():
            res["files"] += 1
            if path.suffix == ".csv":
                res[".csv files"] += 1
            elif path.suffix == ".txt":
                res[".txt files"] += 1
            elif path.suffix == ".npy":
                res[".npy files"] += 1
            elif path.suffix == ".md":
                res[".md files"] += 1
            else:
                res["other files"] += 1
        elif path.is_dir():
            res["subdirectories"] += 1

    return res


def display_diagnostics(dir: str | Path, contents: Dict[str, int]) -> None:
    """Display diagnostics for the directory tree, with root directory pointed to by dir.
        Objects to display: files, subdirectories, .csv files, .txt files, .npy files, .md files, other files.

    Parameters:
        dir (str or pathlib.Path) : Absolute path the directory of interest
        contents (Dict[str, int]) : a dictionary of the same type as return type of get_diagnostics, has the form:

            .. highlight:: python
            .. code-block:: python

                {
                    "files": 0,
                    "subdirectories": 0,
                    ".csv files": 0,
                    ".txt files": 0,
                    ".npy files": 0,
                    ".md files": 0,
                    "other files": 0,
                }

    Returns:
        None
    """

    dir = validate_directory(dir)

    if not isinstance(contents, Dict):
        raise TypeError(f"Expected dictionay, but received {type(contents).__name__}")

    print(f"Diagnostics for: {dir.name}\n")

    for k, v in contents.items():
        print(f"Number of {k}: {v}")


def display_directory_tree(dir: str | Path, maxfiles: int = 3) -> None:
    """Display a directory tree, with root directory pointed to by dir.
       Limit the number of files to be displayed for convenience to maxfiles.
       This tree is built with inspiration from the code written by "Flimm" at https://stackoverflow.com/questions/6639394/what-is-the-python-way-to-walk-a-directory-tree

    Parameters:
        dir (str or pathlib.Path) : Absolute path to the directory of interest
        maxfiles (int) : Maximum number of files to be displayed at each level in the tree, default to three.

    Returns:
        None

    """

    dir = validate_directory(dir)

    if not isinstance(maxfiles, int):
        raise TypeError(f"Expected integer, but received {type(maxfiles)}")

    if maxfiles > 3:
        raise ValueError(f"Cant have more then 3 files, but received {maxfiles}")
    elif maxfiles < 1:
        raise ValueError(f"You need to send it alteast 1 file, but received {maxfiles}")

    print(f"Displaying directory tree for: {dir.name}\n")

    for root, dirs, files in os.walk(dir):
        level = root.replace(str(dir), "").count(os.sep)
        indent = "    " * level
        subindent = "    " * (level + 1)

        print(f"{indent}- {os.path.basename(root)}/")

        for d in dirs:
            print(f"{subindent}- {d}/")

        for i, f in enumerate(files):
            if i < maxfiles:
                print(f"{subindent}- {f}")
            else:
                print(f"{subindent}- ...")
                break


def is_gas_csv(path: str | Path) -> bool:
    """Checks if a csv file pointed to by path is an original gas statistics file.
        An original file must be called '[gas_formula].csv' where [gas_formula] is
        in ['CO2', 'CH4', 'N2O', 'SF6', 'H2'].

    Parameters:
         - path (str of pathlib.Path) : Absolute path to .csv file that will be checked

    Returns
         - (bool) : Truth value of whether the file is an original gas file
    """

    if isinstance(path, str):
        path = Path(path)
    elif not isinstance(path, Path):
        raise TypeError(
            f"Expected to get a path-object, but received {type(path).__name__}"
        )

    if path.suffix != ".csv":
        return False

    gasses = ["CO2", "CH4", "N2O", "SF6", "H2"]

    for name in gasses:
        if name + ".csv" == path.name:
            return True

    return False


def get_dest_dir_from_csv_file(dest_parent: str | Path, file_path: str | Path) -> Path:
    """Given a file pointed to by file_path, derive the correct gas_[gas_formula] directory name.
        Checks if a directory "gas_[gas_formula]", exists and if not, it creates one as a subdirectory under dest_parent.

        The file pointed to by file_path must be a valid file. A valid file must be called '[gas_formula].csv' where [gas_formula]
        is in ['CO2', 'CH4', 'N2O', 'SF6', 'H2'].

    Parameters:
        - dest_parent (str or pathlib.Path) : Absolute path to parent directory where gas_[gas_formula] should/will exist
        - file_path (str or pathlib.Path) : Absolute path to file that gas_[gas_formula] directory will be derived from

    Returns:
        - (pathlib.Path) : Absolute path to the derived directory

    """

    if isinstance(dest_parent, str):
        path_to_parent = Path(dest_parent)
    elif isinstance(dest_parent, Path):
        path_to_parent = dest_parent
    else:
        raise TypeError(
            f"Expected to get a path-object or string, but received {type(dest_parent).__name__}"
        )

    if isinstance(file_path, str):
        path_to_file = Path(file_path)
    elif isinstance(file_path, Path):
        path_to_file = file_path
    else:
        raise TypeError(
            f"Expected to get a path-object or string, but received {type(file_path).__name__}"
        )

    if not path_to_file.is_file():
        raise ValueError(f"Expected file, but received: {type(path_to_file).__name__}")

    if path_to_file.suffix != ".csv":
        raise ValueError(f"Expected a .csv file, but received {path_to_file.suffix}")

    if not path_to_parent.is_dir():
        raise NotADirectoryError(
            f"Did not get a directory, but received {type(path_to_parent).__name__}"
        )

    gas_type = file_path.stem
    dest_name = f"gas_{gas_type}"
    dest_path = path_to_parent / dest_name

    if not dest_path.exists():
        dest_path.mkdir()
        return dest_path

    return dest_path


def merge_parent_and_basename(path: str | Path) -> str:
    """This function merges the basename and the parent-name of a path into one, uniting them with "_" character.
       It then returns the basename of the resulting path.

    Parameters:
        - path (str or pathlib.Path) : Absolute path to modify

    Returns:
        - new_base (str) : New basename of the path
    """
    if isinstance(path, str):
        path = Path(path)
    elif not isinstance(path, Path):
        raise TypeError(f"Expected path object, but received {type(path).__name__}")

    if not path.name:
        raise ValueError(f"Expected path name, but received {path}")

    parent_path = path.parent.name

    if not parent_path:
        raise ValueError(f"Expected path name to parent but received: {parent_path}")

    # New, merged, basename of the path, which will be the new filename
    new_base = f"{parent_path}_{path.name}"
    new_base = new_base.replace(os.sep, "_")

    return new_base


def delete_directories(path_list: List[str | Path]) -> None:
    """Prompt the user for permission and delete the objects pointed to by the paths in path_list if
       permission is given. If the object is a directory, its whole directory tree is removed.

    Parameters:
        - path_list (List[str | Path]) : a list of absolute paths to all the objects to be removed.


    Returns:
    None
    """

    # NOTE: This is an optional task, no points assigned. If you are skipping it, remove `raise NotImplementedError` in the function body
    ...
