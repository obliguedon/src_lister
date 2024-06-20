# Test get_all_params()

this function should extract those pattern :
- `{key}`
- `{key=extension}`
- `{prefix{key}}`
- `{{key}suffix}`
- `{prefix{key}suffix}`
- `{prefix{key=extension}}`
- `{{key=extension}suffix}`
- `{prefix{key=extension}suffix}`

and fail on anything else by returning a `None` value

also those parameters must be composed of the following characters:
- `key` = [a-z][A-Z][0-9][-]
- `extension` = [.][a-z][A-Z][0-9]
- `prefix` and `suffix` = [a-z][A-Z][0-9][-+_\\]

otherwise the function should fail