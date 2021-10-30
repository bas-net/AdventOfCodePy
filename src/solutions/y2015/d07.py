import re

import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    # letter : value
    wires = {}
    # output : (s1, s2, op)
    gates = {}

    def func(instruction: str) -> None:
        wire_instr = re.findall(r'^(\d+)\s->\s([a-z]+)$', instruction)
        if wire_instr:
            wires[wire_instr[0][1]] = int(wire_instr[0][0])
            return
        gate_instr = re.search(
            r'^(?P<s1>[a-z0-9]+)?\s?(?P<gate>AND|LSHIFT|RSHIFT|NOT|OR)\s(?P<s2>[a-z0-9]+)\s->\s(?P<dest>[a-z]+)$', instruction)
        if gate_instr:
            gate = gate_instr.group('gate')
            dest = gate_instr.group('dest')
            source_2 = gate_instr.group('s2')
            if gate == 'NOT':
                gates[dest] = (source_2, None, 'NOT')
                return

            source_1 = gate_instr.group('s1')
            gates[dest] = (source_1, source_2, gate)
            return

        direct_instr = re.search(
            r'^(?P<s1>[a-z]+)\s->\s(?P<dest>[a-z]+)$', instruction)

        if direct_instr is not None:
            source_1 = direct_instr.group('s1')
            dest = direct_instr.group('dest')
            gates[dest] = (source_1, None, 'DIRECT')
            return

        raise Exception()

    solutions.y2015.lib2015.process_by_line(input_string, func)

    queue = list(gates)

    while len(queue) > 0:
        dest = queue.pop(0)
        handling = gates[dest]
        has_sources = True
        if handling[0] not in wires and not handling[0].isnumeric():
            has_sources = False
        if handling[2] not in ['NOT', 'DIRECT']:
            if handling[1] not in wires and not handling[1].isnumeric():
                has_sources = False

        if not has_sources:
            queue.append(dest)
            continue

        source_1 = int(handling[0]) if handling[0].isnumeric(
        ) else wires[handling[0]]
        if handling[2] == 'NOT':
            wires[dest] = (~source_1) & 0xFFFF
            continue
        if handling[2] == 'DIRECT':
            wires[dest] = source_1
            continue
        source_2 = int(handling[1]) if handling[1].isnumeric(
        ) else wires[handling[1]]
        if handling[2] == 'AND':
            wires[dest] = (source_1 & source_2) & 0xFFFF
            continue
        if handling[2] == 'LSHIFT':
            wires[dest] = (source_1 << source_2) & 0xFFFF
            continue
        if handling[2] == 'RSHIFT':
            wires[dest] = (source_1 >> source_2) & 0xFFFF
            continue
        if handling[2] == 'OR':
            wires[dest] = (source_1 | source_2) & 0xFFFF
            continue

        raise Exception()

    wire_options = list(wires)
    wire_options.sort()

    return wires[wire_options[0]]


def p2(input_string: str) -> str:
    # letter : value
    wires = {}
    # output : (s1, s2, op)
    gates = {}

    def func(instruction: str) -> None:
        wire_instr = re.findall(r'^(\d+)\s->\s([a-z]+)$', instruction)
        if wire_instr:
            wires[wire_instr[0][1]] = int(wire_instr[0][0])
            return
        gate_instr = re.search(
            r'^(?P<s1>[a-z0-9]+)?\s?(?P<gate>AND|LSHIFT|RSHIFT|NOT|OR)\s(?P<s2>[a-z0-9]+)\s->\s(?P<dest>[a-z]+)$', instruction)
        if gate_instr:
            gate = gate_instr.group('gate')
            dest = gate_instr.group('dest')
            source_2 = gate_instr.group('s2')
            if gate == 'NOT':
                gates[dest] = (source_2, None, 'NOT')
                return

            source_1 = gate_instr.group('s1')
            gates[dest] = (source_1, source_2, gate)
            return

        direct_instr = re.search(
            r'^(?P<s1>[a-z]+)\s->\s(?P<dest>[a-z]+)$', instruction)

        if direct_instr is not None:
            source_1 = direct_instr.group('s1')
            dest = direct_instr.group('dest')
            gates[dest] = (source_1, None, 'DIRECT')
            return

        raise Exception()

    solutions.y2015.lib2015.process_by_line(input_string, func)

    wires['b'] = int(p1(input_string))

    queue = list(gates)

    while len(queue) > 0:
        dest = queue.pop(0)
        handling = gates[dest]
        has_sources = True
        if handling[0] not in wires and not handling[0].isnumeric():
            has_sources = False
        if handling[2] not in ['NOT', 'DIRECT']:
            if handling[1] not in wires and not handling[1].isnumeric():
                has_sources = False

        if not has_sources:
            queue.append(dest)
            continue

        source_1 = int(handling[0]) if handling[0].isnumeric(
        ) else wires[handling[0]]
        if handling[2] == 'NOT':
            wires[dest] = (~source_1) & 0xFFFF
            continue
        if handling[2] == 'DIRECT':
            wires[dest] = source_1
            continue
        source_2 = int(handling[1]) if handling[1].isnumeric(
        ) else wires[handling[1]]
        if handling[2] == 'AND':
            wires[dest] = (source_1 & source_2) & 0xFFFF
            continue
        if handling[2] == 'LSHIFT':
            wires[dest] = (source_1 << source_2) & 0xFFFF
            continue
        if handling[2] == 'RSHIFT':
            wires[dest] = (source_1 >> source_2) & 0xFFFF
            continue
        if handling[2] == 'OR':
            wires[dest] = (source_1 | source_2) & 0xFFFF
            continue

        raise Exception()

    wire_options = list(wires)
    wire_options.sort()

    return wires[wire_options[0]]
