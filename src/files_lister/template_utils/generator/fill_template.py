import typing
import pathlib
import logging
from files_lister import template_utils

def fill_template(template: str, files_lists: typing.Dict[str, typing.List[pathlib.PosixPath]]) -> str: 
    logging.debug(f"fill_template.template = {template}")
    logging.debug(f"fill_template.files_lists = {files_lists}")
    output = template
    # replace the variable in the template string
    params = template_utils.extractor.get_all_params(template)
    keys = template_utils.extractor.get_all_values(params)

    for item in keys:
        pattern = template_utils.generator.gen_pattern(params[item], files_lists[item])
        output = output.replace(params[item].group(), pattern)

    return output