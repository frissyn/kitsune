def with_includes(*args) -> dict:
    return {"includes": ",".join(args)}


def with_fields(name: str, *args) -> dict:
    return {f"fields[{name}]": ",".join(args)}


def with_filter(**kws) -> dict:
    if len(kws) > 1:
        raise ValueError
    else:
        name = tuple(kws.keys())[0]
        value = tuple(kws.values())[0]

        return {f"filter[{name}]": value}


def with_sorting(*args) -> dict:
    return {"sort": ",".join([f"-{a}" for a in args])}
