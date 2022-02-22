def try_int(text) -> int:
    try:
        return int(text)
    except Exception:
        return 0
