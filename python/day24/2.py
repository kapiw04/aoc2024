import os
import random
import readline
import re
from dataclasses import dataclass
from typing import Counter
from rich import print


@dataclass
class Output:
    wire1: str
    op: str
    wire2: str
    name: str

    def operate(self, wires, outputs):
        self.ensure_wires(wires, outputs)
        assert self.wire1 in wires.keys() and self.wire2 in wires.keys()
        if self.op == "AND":
            return wires[self.wire1] & wires[self.wire2]
        if self.op == "OR":
            return wires[self.wire1] | wires[self.wire2]
        if self.op == "XOR":
            return wires[self.wire1] ^ wires[self.wire2]
        else:
            raise ValueError(f"invalid op: {self.op}")

    def ensure_wires(self, wires, outputs):
        for wire in [self.wire1, self.wire2]:
            if wire in wires.keys():
                continue
            found = find_in_outputs(wire, outputs)
            wires[found.name] = found.operate(wires, outputs)

    def __lt__(self, other):
        return self.name < other.name

    def has_wire(self, wire):
        return wire in [self.wire1, self.wire2]

    def __str__(self):
        return f"{self.name} = {self.wire1} {self.op} {self.wire2}"


def find_in_outputs(key, outputs):
    for out in outputs:
        if out.name == key:
            assert isinstance(out, Output)
            return out


def find_depending(wire):
    for out in outputs:
        if out.has_wire(wire):
            print(f"{out} depends on {wire}")


def inspect(wire, max_depth=0):
    o = find_in_outputs(wire, outputs)
    assert o is not None
    w1, w2 = o.wire1, o.wire2
    res = f"{o}; includes {w1}, {w2}"

    if max_depth > 0:
        if not w1.startswith(("x", "y", "z")) and not w1.endswith("32"):
            res += f"\n {inspect(w1, max_depth=max_depth - 1)}"
        if not w2.startswith(("x", "y", "z")) and not w2.endswith("32"):
            res += f"\n {inspect(w2, max_depth=max_depth - 1)}"

    return res


def parsed_outputs(outputs):
    for output in outputs:
        w1, op, w2, name = re.findall(r"(\S+) (\S+) (\S+) -> (\S+)", output)[0]
        yield w1, op, w2, name


def update_wires():
    with open("day24/input") as f:
        wires, outputs = f.read().split("\n\n")
    wires = wires.splitlines()
    outputs = outputs.splitlines()

    wires_dict = {w.split(": ")[0]: random.choice((0, 1)) for w in wires[:-1]}
    wires_dict[wires[len(wires) // 2].split(": ")[0]] = int(wires[-1].split(": ")[1])
    wires_dict[wires[-1].split(": ")[0]] = int(wires[-1].split(": ")[1])
    outputs = [Output(w1, op, w2, name) for w1, op, w2, name in parsed_outputs(outputs)]
    for o in outputs:
        wires_dict[o.name] = o.operate(wires_dict, outputs)

    return wires_dict, outputs


wires, outputs = update_wires()


def assert_inspects_up_to(n):
    for i in range(1, n + 1):
        o = find_in_outputs(f"x{i:02}", outputs)
        assert o is not None, f"x{i:02} is none"
        assert o.op == "XOR"


def swap(wire1, wire2):
    with open("day24/input", "r") as f:
        lines = f.readlines()

    line_i1, line_i2 = None, None
    for i, line in enumerate(lines):
        if re.search(rf"->\s+{wire1}$", line):
            line_i1 = i
        if re.search(rf"->\s+{wire2}$", line):
            line_i2 = i

    line1 = lines[line_i1].rstrip()
    line2 = lines[line_i2].rstrip()

    gate1 = re.match(r"(.+) -> " + re.escape(wire1), line1).group(1)
    gate2 = re.match(r"(.+) -> " + re.escape(wire2), line2).group(1)

    lines[line_i1] = f"{gate1} -> {wire2}\n"
    lines[line_i2] = f"{gate2} -> {wire1}\n"

    with open("day24/input", "w") as f:
        f.writelines(lines)

    print(f"swapped {wire1} with {wire2}")


def reset(input_file="day24/input", original_input_file="day24/input_original"):
    with open(original_input_file, "r") as source_file:
        new_content = source_file.read()
    confirmation = input(
        f"Replace content of '{input_file}' with '{original_input_file}'? ([y]/n): "
    ).lower()
    if confirmation != "y" and confirmation:
        print("Operation cancelled.")
    else:
        with open(input_file, "w") as target_file:
            target_file.write(new_content)
        print("File content replaced.")


def diff(expected_bit_length=None):
    wires, outputs = update_wires()

    xs = filter(lambda w: w.startswith("x"), wires.keys())
    ys = filter(lambda w: w.startswith("y"), wires.keys())

    xs = sorted(xs, key=lambda x: int(x[1:]), reverse=True)
    ys = sorted(ys, key=lambda y: int(y[1:]), reverse=True)

    outputs.sort(reverse=True)

    result = "".join([str(wires[i.name]) for i in outputs if i.name.startswith("z")])

    x_binary = "".join(str(wires[x]) for x in xs)
    y_binary = "".join(str(wires[y]) for y in ys)

    x = int(x_binary, 2)
    y = int(y_binary, 2)

    d = (x + y) ^ int(result, 2)
    d_binary = bin(d)

    if expected_bit_length:
        d_binary = d_binary.zfill(expected_bit_length + 2)

    c = Counter(d_binary)
    print(c)
    print(f"x     : {bin(x)}")
    print(f"y     : {bin(y)}")
    print(f"x + y: {bin(x + y)}")
    print(f"z    : {bin(int(result, 2))}")

    try:
        first_mismatch = list(reversed(d_binary)).index("1")
        print(f"next fix needed at index {first_mismatch}")
    except ValueError:
        print("No mismatches found. All bits match correctly.")

    return d_binary


HISTORY_FILE = ".command_history"

if os.path.exists(HISTORY_FILE):
    readline.read_history_file(HISTORY_FILE)

while True:
    try:
        user_input = input(">>> ").split()
    except EOFError:
        break
    op, arg1, arg2 = (user_input + [None, None, None])[:3]

    original_input = " ".join(user_input)
    if original_input.strip():
        if (
            not readline.get_current_history_length()
            or readline.get_history_item(readline.get_current_history_length())
            != original_input
        ):
            readline.add_history(original_input)

    try:
        if op == "d":
            print(diff())
        elif op == "s":
            if arg1 is None or arg2 is None:
                print("bad args")
                continue
            swap(arg1, arg2)
        elif op == "i":
            if arg1 is None:
                print("bad arg")
            if arg2 is None:
                arg2 = 0
            print(inspect(arg1, int(arg2)))
        elif op == "a":
            if arg1 is None:
                print("bad arg")
            assert_inspects_up_to(int(arg1))
        elif op == "u":
            wires, outputs = update_wires()
        elif op == "f":
            if arg1 is None:
                print("bad arg")
            find_depending(arg1)
        elif op == "r":
            reset()
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        import traceback

        print(traceback.format_exc())


if HISTORY_FILE:
    readline.write_history_file(HISTORY_FILE)

swaps = "cqm,vjv,z25,mps,vwp,z19,z13,vcv".split(",")
print(",".join(sorted(swaps)))
