from .disassemble import disassemble_hangul


def hangul_includes(x, y):
    disassembled_x = disassemble_hangul(x)
    disassembled_y = disassemble_hangul(y)

    return disassembled_y in disassembled_x
