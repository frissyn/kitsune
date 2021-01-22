def with_includes(*args) -> dict:
    return {"includes": ",".join(args)}


def with_fields(name: str, *args) -> dict:
    value = ",".join(args)

    return {f"fields[{name}]": value}


def with_filter(**kws) -> dict:
    if len(kws) > 1:
        raise ValueError
    else:
        name = tuple(kws.keys())[0]
        value = tuple(kws.values())[0]

        return {f"filter[{name}]": value}


def with_sorting(*args) -> dict:
    value = ""

    for a in args:
        value += f"-{a}"

        if not a == args[-1]:
            value += ","
    
    return {"sort": value}
