import json
import os
import sys
import yaml


YAML_EXTENSIONS = [".yaml", ".yml"]


def find_all_yaml_paths(source):
    paths = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(tuple(YAML_EXTENSIONS)):
                paths.append(os.path.join(root, file))
    return paths


def create_subdirectories(paths):
    dir_paths = []

    for path in paths:
        dir_path, _ = os.path.split(path)
        dir_paths.append(dir_path)

    for path in dir_paths:
        if not os.path.exists(path):
            os.makedirs(path)


def load_yaml_files(paths):
    files = []
    for path in paths:
        with open(path, 'r') as file:
            files.append(yaml.safe_load(file))
    return files


def convert_to_json(yaml_files, target_paths):
    for data, path in zip(yaml_files, target_paths):
        with open(path, 'w') as file:
            json.dump(data, file)


def get_relative_paths(paths, rel_path):
    rel_paths = []
    for path in paths:
        rel_paths.append(os.path.relpath(path, rel_path))
    return rel_paths


def get_json_paths(rel_yaml_paths, target_path):
    json_paths = []
    for path in rel_yaml_paths:
        json_path = os.path.join(target_path, os.path.splitext(path)[0] + ".json")
        json_paths.append(json_path)
    return json_paths


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    yaml_paths = find_all_yaml_paths(source_path)
    rel_yaml_paths = get_relative_paths(yaml_paths, source_path)
    json_paths = get_json_paths(rel_yaml_paths, target_path)
    yaml_files = load_yaml_files(yaml_paths)

    create_subdirectories(json_paths)

    convert_to_json(yaml_files, json_paths)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        raise Exception("Invalid arguments. Please provide a valid source and destination directory.")
    source, target = args
    main(source, target)