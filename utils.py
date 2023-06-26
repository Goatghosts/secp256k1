def get_public_key(x: int, y: int):
    return b"\x04" + x.to_bytes(32, "big") + y.to_bytes(32, "big")


def decompress_public_key(public_key: bytes):
    x = int.from_bytes(public_key[1:33], "big")
    y = int.from_bytes(public_key[33:], "big")
    return x, y
