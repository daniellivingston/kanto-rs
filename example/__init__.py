from kanto._native import ffi, lib


def test():
    return lib.a_function_from_rust()
