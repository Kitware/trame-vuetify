def get_trame_versions():
    import importlib.metadata

    from trame_client.utils.version import get_version

    output = []
    for pkg in importlib.metadata.distributions():
        name = pkg.metadata.get("Name", "")
        if name.startswith("trame"):
            version = get_version(name)
            output.append(f"{name.replace('trame-', '')} == {version}")

    return "\n".join(output)
