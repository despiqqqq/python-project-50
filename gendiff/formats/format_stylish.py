from gendiff.diff_tree import get_key, get_value, get_children, get_type

TRANSLATOR = {True: "true", False: "false", None: "null"}
INDENT = 4


def translate(value):
    is_bool_or_none = bool(isinstance(value, bool) or value is None)
    return TRANSLATOR.get(value) if is_bool_or_none else value


def prepare_indent(depth, sym, replacer=" "):
    return f"{(depth * INDENT - 2) * replacer}{sym} "


def pretty_print(value, depth):
    if isinstance(value, dict):
        deep_lines = [
            prepare_indent(depth, " ") + (f'{key}:'
                                          f' {pretty_print(val, depth + 1)}')
            for key, val in value.items()
        ]
        result = "\n".join(deep_lines)
        return f"{{\n{result}\n" + prepare_indent(depth - 1, ' ') + "}"

    return str(translate(value))


def make_stylish(diff_tree, depth=0):
    node_type = get_type(diff_tree)
    children = get_children(diff_tree)

    if node_type == "root":
        lines = map(lambda node: make_stylish(node, depth + 1), children)
        lines = "\n".join(lines)
        return f"{{\n{lines}\n}}"

    key = get_key(diff_tree)
    values = get_value(diff_tree)

    if node_type == "parent":
        line = prepare_indent(depth, " ") + f"{key}: "
        ends = make_stylish_parent(children, depth)
        line += f"{{\n{ends}\n" + prepare_indent(depth, ' ') + "}"
        return line

    elif node_type in ["changed", "same", "added", "deleted"]:
        if node_type == "changed":
            return make_stylish_changed(key, values, depth)

        elif node_type == "same":
            return make_stylish_same(key, values, depth)

        elif node_type == "added":
            return make_stylish_added(key, values, depth)

        elif node_type == "deleted":
            return make_stylish_deleted(key, values, depth)

    else:
        raise ValueError("Unknown node type")


def make_stylish_parent(children, depth):
    ends = map(lambda node: make_stylish(node, depth + 1), children)
    ends = "\n".join(ends)
    return ends


def make_stylish_changed(key, values, depth):
    lines = []
    for sym, val in zip(("-", "+"), values):
        indent = prepare_indent(depth, sym)
        line = indent + f"{key}: {pretty_print(val, depth + 1)}"
        lines.append(line)
    return "\n".join(lines)


def make_stylish_same(key, values, depth):
    indent = prepare_indent(depth, " ")
    return indent + f"{key}: {pretty_print(values, depth + 1)}"


def make_stylish_added(key, values, depth):
    indent_plus = prepare_indent(depth, "+")
    return indent_plus + f"{key}: {pretty_print(values, depth + 1)}"


def make_stylish_deleted(key, values, depth):
    indent_minus = prepare_indent(depth, "-")
    return indent_minus + f"{key}: {pretty_print(values, depth + 1)}"
