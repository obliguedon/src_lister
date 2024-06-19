import pathlib
import yaml
import os
import typing

def get_deps(yaml_file: pathlib.PosixPath) -> typing.List[pathlib.PosixPath]:
        all_deps = list()
        all_deps.append(yaml_file)
        # checking the input values
        
        with open(yaml_file, 'r') as file:
            data_yaml = yaml.load(file, Loader=yaml.FullLoader)

        if "dependencies" in data_yaml:
            # logging.info(f"found \"{"dependencies"}\" in \"{yaml_file}\"")
            parent_yaml_file = pathlib.Path(yaml_file).parent

            for yaml_dep in data_yaml["dependencies"]:
                abs_yaml_dep = pathlib.Path(os.path.join(parent_yaml_file, yaml_dep)).resolve()

                # TODO: check that the files exist before putting it in the list
                all_deps.append(abs_yaml_dep)
                more_deps = get_deps(abs_yaml_dep)
                # avoid putting None value in the list
                if more_deps != None:
                    # avoid nested list by adding item 1 by 1
                    for dep in more_deps:
                        # TODO: check that element exist before putting it in the list
                        all_deps.append(dep)

            all_deps = list(set(all_deps)) # remove duplicate
            return all_deps
