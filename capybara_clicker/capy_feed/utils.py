from capybara_clicker.capy_feed.registry import capybaras


def get_capy(count: int) -> tuple[str, str]:
    """Get capy description and image name by click number"""
    capy_keys: list[int] = sorted(list(capybaras.keys()))
    idx: int = 0
    while capy_keys[idx] < count:
        idx += 1

    return capybaras[capy_keys[idx]]
