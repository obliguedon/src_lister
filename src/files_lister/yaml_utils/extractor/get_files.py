import logging
import yaml
import pathlib
import os
import typing

def get_files(all_deps: typing.List[pathlib.PosixPath], item: str, flag: str=None) -> typing.List[pathlib.PosixPath]:
        all_files = list()
        for yaml_file in all_deps:
            # checking the input values
            logging.debug(f"WORK ON FILE {yaml_file}")

            with yaml_file.open('r') as file:
                data_yaml = yaml.load(file, Loader=yaml.FullLoader)

            if item in data_yaml:
                logging.debug(f"found \"{item}\" in \"{yaml_file}\"")
                yaml_file_dir = pathlib.Path(yaml_file).parent
                # logging.info(f"working in dir = {yaml_file_dir}")
                for element in data_yaml[item]:
                    logging.debug(f"Work on {element}")
                    if type(element) is str:
                        abs_element = pathlib.Path(os.path.join(yaml_file_dir, element)).resolve()
                        logging.debug(f"abs element item = {abs_element}")

                        if os.path.exists(abs_element):
                            all_files.insert(0, abs_element)
                        else:
                            logging.error(f"file \"{abs_element}\" not found")
                            raise FileNotFoundError(f"file \"{abs_element}\" not found")

                    elif type(element) is dict:
                        for key in element:
                            logging.debug(f"flag = {element[key]}")
                            # add sources if flag ok
                            if flag == None:
                                logging.debug("no flag specified")
                            elif flag in str(element[key]):
                                [key_source] = element.keys()
                                abs_element = pathlib.Path(os.path.join(yaml_file_dir, key_source)).resolve()
                                logging.debug(f"Add \"{abs_element}\" to the list")

                                if os.path.exists(abs_element):
                                    all_files.insert(0, abs_element)
                                else:
                                    logging.error(f"file \"{abs_element}\" not found")
                                    raise FileNotFoundError(f"file \"{abs_element}\" not found")
            else:
                logging.debug(f"\"{item}\" not found in \"{yaml_file}\"")
        all_files = list(dict.fromkeys(all_files)) # remove duplicate while keeping order
        return all_files
