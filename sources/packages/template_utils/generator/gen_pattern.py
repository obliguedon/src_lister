import re
import typing
import pathlib
import logging

def gen_pattern(param: re.Match, files_list: typing.List[pathlib.PosixPath]) -> str:
    logging.debug(f"gen_pattern.param = {param}")
    logging.debug(f"gen_pattern.files_list = {files_list}")
    if not files_list:
        logging.warning(f"no file found for variable \"{param.group()}\", will be erased from output")
        return ""
    else:
        string = str()
        file_found = False

        for file in files_list:
            string += " "

            logging.debug(f"item suffix = {pathlib.Path(file).suffix}")
            logging.debug(f"regex suffix = {param.group('extension')}")

            if (pathlib.Path(file).suffix == param.group("extension")):
                file_found = True
                if (param.group("prefix") != None):
                    string += param.group("prefix")

                string += str(file)

                if (param.group("suffix") != None):
                    string += param.group("suffix")

        if file_found:
            return string
        else:
            logging.warning(f"no file found for variable \"{param.group()}\" with extension \"{param.group('extension')}\", will be erased from output")
            return ""
