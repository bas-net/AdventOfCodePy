import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    def func(string_to_parse: str) -> int:
        state = 'NORMAL'
        inmem_count = 0

        hex_read = ''

        for c in string_to_parse:
            if state == 'NORMAL':
                if c == '"':
                    pass
                elif c == '\\':
                    state = 'ESCAPED'
                else:
                    inmem_count += 1
            elif state == 'ESCAPED':
                if c == '\\':
                    inmem_count += 1
                    state = 'NORMAL'
                elif c == 'x':
                    state = 'HEX'
                    hex_read = ''
                elif c == '"':
                    inmem_count += 1
                    state = 'NORMAL'
                else:
                    raise Exception()
            elif state == 'HEX':
                if len(hex_read) == 0:
                    hex_read = c
                elif len(hex_read) == 1:
                    hex_read += c
                    inmem_count += 1
                    state = 'NORMAL'
                else:
                    Exception()

        return len(string_to_parse) - inmem_count

    return solutions.y2015.lib2015.process_by_line_aggregate(input_string, func, sum)


def p2(input_string: str) -> str:
    pass
