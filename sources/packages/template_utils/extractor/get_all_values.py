import typing
import re
def get_all_values(params : typing.Dict[str, typing.List[re.Match]], group: str="key") -> typing.List[str]:
    items = []
    for item, match in params.items():
        if match.group(group) != None:
            items.append(match.group(group))
    return items