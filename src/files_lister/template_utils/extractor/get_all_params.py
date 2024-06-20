import re
import typing

def get_all_params(template: str) -> typing.Dict[str, typing.List[re.Match]]:
    
    if not isinstance(template, str):
        raise TypeError("template must be a string")
    # get all match in the template
    params = dict()

    pattern = re.compile(r"(?:{{1,2}(?:(?P<prefix>[a-zA-Z0-9\-\+\_\\]+){)?(?P<key>[a-zA-Z0-9\-]*)(?:\=(?P<extension>\.[a-zA-Z0-9]+))?(?:}(?P<suffix>[a-zA-Z0-9\-\+\_\\]+))?}{1,2})")
    
    for match in re.finditer(pattern, template):
        params[match.group("key")] = match

    return params