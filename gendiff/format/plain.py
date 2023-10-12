val_st = {
    'removed': ' was removed',
    'add': ' was added with value: ',
    'change': ' was updated. From ',
    'change_to': ' to ',
    'first_word': 'Property '
}
cons = {'False': 'false', 'True': 'true', 'None': 'null', '0': '0'}
val_acs = {'s': 'status', 'o': 'old_value', 'n': 'new_value'}
hid_dict = '[complex value]'


def make_plain(data: dict) -> list:
    res = []

    for key, values in data.items():
        if not isinstance(values, dict):
            continue

        status_keys = values.keys()

        if not val_acs['s'] in values.keys():
            for v in make_plain(values):
                res += [[f"{key}."] + v]
            continue

        if not val_acs['o'] in status_keys:
            n = values[val_acs['n']]
            value = f"'{n}'" if not isinstance(n, dict) else hid_dict

            res += [[key] + [val_st['add']] + [value]]
            continue

        if not val_acs['n'] in status_keys:
            o = values[val_acs['o']]
            value = f"'{o}'" if not isinstance(o, dict) else hid_dict

            res += [[key] + [val_st['removed']]]
            continue

        o = values[val_acs['o']]
        n = values[val_acs['n']]

        old_value = f"'{o}'" if not isinstance(o, dict) else hid_dict
        new_value = f"'{n}'" if not isinstance(n, dict) else hid_dict

        res += [[key]
                + [val_st['change']]
                + [old_value]
                + [val_st['change_to']]
                + [new_value]]

    return res


def plain(data: dict) -> str:

    lines = make_plain(data)
    lines = sorted([''.join(v) for v in lines])
    lines = list(map(lambda x:
                     ' '.join([val_st['first_word']
                               + f"'{x.split()[0]}'"]
                              + x.split()[1:]),
                     lines))

    res = '\n'.join(lines)

    for k, v in cons.items():
        res = res.replace(f"'{k}'", v)

    return res
