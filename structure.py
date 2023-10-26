import os
import shutil
from pathlib import Path

root_dir = "."  # replace this with your directory path
out_file = "structure.txt"  # rename the output file to structure.txt
extensions = [
    ".js",
    ".handlebars",
    ".json",
    ".py",
    ".txt",
]  # file extensions to collect content from
files_to_copy = [
    "web_scrape.py",
    "web_search.py",
    "llm_utils.py",
    "prompts.py",
    "research_agent.py",
    "run.py",
    "__init__.py,",
    "config.py",
    "singleton.py",
    "editor.py",
    "reviser.py",
    "gpt_researcher.py",
    "search_api.py",
    "writer.py",
    "research_team.py",
    "researcher.py",
    "test.py",
    "html.py",
    "text.py",
    "main.py",
]  # list of filenames to copy

destination_folder = "FOLDER"  # Name of the folder where files will be copied to
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


def is_excluded(directory, path):
    """Check if a path should be excluded from processing."""
    exclusions = ["node_modules", ".git", "package-lock.json", "outputs"]
    full_path = os.path.join(directory, path)
    for exclusion in exclusions:
        if full_path.endswith(exclusion):
            return True
    return False


def print_tree(directory, file_output, indent=""):
    if is_excluded(directory, ""):
        return
    contents = sorted(os.listdir(directory))
    pointers = ["├── " if item != contents[-1] else "└── " for item in contents]
    for pointer, path in zip(pointers, contents):
        if is_excluded(directory, path):
            continue
        full_path = os.path.join(directory, path)
        print(indent + pointer + path, file=file_output)
        if os.path.isdir(full_path):
            next_indent = "│   " if pointer.startswith("├") else "    "
            print_tree(full_path, file_output, indent=indent + next_indent)


def print_file_contents(directory, file_output, indent=""):
    if is_excluded(directory, ""):
        return
    contents = sorted(os.listdir(directory))
    for path in contents:
        if is_excluded(directory, path):
            continue
        full_path = os.path.join(directory, path)
        if os.path.isfile(full_path) and Path(full_path).suffix in extensions:
            print("\n" + "=" * 30 + "\n", file=file_output)  # separator line
            print("-" + Path(full_path).name, file=file_output)
            with open(full_path, "r") as content_file:
                print(content_file.read(), file=file_output)
        elif os.path.isdir(full_path):
            print_file_contents(full_path, file_output, indent=indent + "    ")


def copy_files(directory):
    """Search and copy the specific files to the destination folder."""
    contents = sorted(os.listdir(directory))
    for path in contents:
        if is_excluded(directory, path):
            continue
        full_path = os.path.join(directory, path)
        if os.path.isfile(full_path) and path in files_to_copy:
            shutil.copy(full_path, destination_folder)
        elif os.path.isdir(full_path):
            copy_files(full_path)


copy_files(root_dir)

with open(out_file, "w", encoding="utf-8") as f:  # specify utf-8 encoding
    print_tree(root_dir, f)
    print_file_contents(root_dir, f)
