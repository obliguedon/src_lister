import yaml
import logging
import pathlib
import typing
import os


class YAML_extractor:
    def __init__(self, top_yaml: pathlib.PosixPath) -> None:
        self.top_yaml = top_yaml
        self.all_deps = []
        self.all_items = []

    #  ██████╗ ███████╗████████╗    ██████╗ ███████╗██████╗ ███████╗
    # ██╔════╝ ██╔════╝╚══██╔══╝    ██╔══██╗██╔════╝██╔══██╗██╔════╝
    # ██║  ███╗█████╗     ██║       ██║  ██║█████╗  ██████╔╝███████╗
    # ██║   ██║██╔══╝     ██║       ██║  ██║██╔══╝  ██╔═══╝ ╚════██║
    # ╚██████╔╝███████╗   ██║       ██████╔╝███████╗██║     ███████║
    #  ╚═════╝ ╚══════╝   ╚═╝       ╚═════╝ ╚══════╝╚═╝     ╚══════╝

    def get_deps(self, yaml_file: pathlib.PosixPath, key: str) -> typing.List[pathlib.PosixPath]:
        # checking the input values
        
        with open(yaml_file, 'r') as file:
            data_yaml = yaml.load(file, Loader=yaml.FullLoader)

        if yaml_file not in self.all_deps:
            self.all_deps.append(yaml_file)

        if key in data_yaml:
            logging.info(f"found \"{key}\" in \"{yaml_file}\"")
            parent_yaml_file = pathlib.Path(yaml_file).parent

            for yaml_dep in data_yaml[key]:
                abs_yaml_dep = pathlib.Path(os.path.join(parent_yaml_file, yaml_dep)).resolve()

                # TODO: check that the files exist before putting it in the list
                self.all_deps.append(abs_yaml_dep)
                more_deps = self.get_deps(abs_yaml_dep, key)
                # avoid putting None value in the list
                if more_deps != None:
                    # avoid nested list by adding item 1 by 1
                    for dep in more_deps:
                        # TODO: check that element exist before putting it in the list
                        self.all_deps.append(dep)

            return list(set(self.all_deps)) # remove duplicate


    #  ██████╗ ███████╗████████╗    ██╗████████╗███████╗███╗   ███╗███████╗
    # ██╔════╝ ██╔════╝╚══██╔══╝    ██║╚══██╔══╝██╔════╝████╗ ████║██╔════╝
    # ██║  ███╗█████╗     ██║       ██║   ██║   █████╗  ██╔████╔██║███████╗
    # ██║   ██║██╔══╝     ██║       ██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║
    # ╚██████╔╝███████╗   ██║       ██║   ██║   ███████╗██║ ╚═╝ ██║███████║
    #  ╚═════╝ ╚══════╝   ╚═╝       ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝

    def search_items_for_target(self, flag=None, item="sources") -> None:

        for yaml_file in self.all_deps:
            # checking the input values
            logging.info(f"WORK ON FILE {yaml_file}")

            with yaml_file.open('r') as file:
                data_yaml = yaml.load(file, Loader=yaml.FullLoader)

            if item in data_yaml:
                logging.info(f"found \"{item}\" in \"{yaml_file}\"")
                yaml_file_dir = pathlib.Path(yaml_file).parent
                # logging.info(f"working in dir = {yaml_file_dir}")
                for element in data_yaml[item]:
                    print(f"Work on {element}")
                    if type(element) is str:
                        abs_element = pathlib.Path(os.path.join(yaml_file_dir, element)).resolve()
                        # TODO: check that element exist before putting it in the list
                        self.all_items.append(abs_element)
                        print(f"abs element item = {abs_element}")
                    elif type(element) is dict:
                        for key in element:
                            print(f"flag = {element[key]}")
                            # add sources if flag ok
                            if flag == None:
                                logging.info("no flag specified")
                            elif flag in str(element[key]):
                                [key_source] = element.keys()
                                abs_element = pathlib.Path(os.path.join(yaml_file_dir, key_source)).resolve()
                                logging.info(f"Add \"{abs_element}\" to the list")
                                # TODO: check that element exist before putting it in the list
                                self.all_items.append(abs_element)
                                print(f"abs element item = {abs_element}")
            else:
                logging.info(f"\"{item}\" not found in \"{yaml_file}\"")
        self.all_items = list(set(self.all_items))
