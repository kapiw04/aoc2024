import sys
import re
from dataclasses import dataclass

wires, outputs = sys.stdin.read().split("\n\n")
wires = wires.splitlines()
outputs = outputs.splitlines()


@dataclass
class Output:
    wire1: str
    op: str
    wire2: str
    name: str

    def operate(self):
        self.ensure_wires()
        assert self.wire1 in wires.keys() and self.wire2 in wires.keys()
        if self.op == "AND":
            return wires[self.wire1] & wires[self.wire2]
        if self.op == "OR":
            return wires[self.wire1] | wires[self.wire2]
        if self.op == "XOR":
            return wires[self.wire1] ^ wires[self.wire2]
        else:
            raise ValueError(f"invalid op: {self.op}")

    def ensure_wires(self):
        for wire in [self.wire1, self.wire2]:
            if wire in wires.keys():
                continue
            found = find_in_outputs(wire)
            wires[found.name] = found.operate()

    def __lt__(self, other):
        return self.name < other.name


def find_in_outputs(key):
    for out in outputs:
        if out.name == key:
            return out


def parsed_outputs():
    for output in outputs:
        w1, op, w2, name = re.findall(r"(\S+) (\S+) (\S+) -> (\S+)", output)[0]
        yield w1, op, w2, name


wires = {w.split(": ")[0]: int(w.split(": ")[1]) for w in wires}
outputs = [Output(w1, op, w2, name) for w1, op, w2, name in parsed_outputs()]

for o in outputs:
    wires[o.name] = o.operate()


outputs.sort()

outputs.reverse()
# outputs = list(filter(lambda x: x.name.startswith("z"), outputs))

result = "".join([str(wires[i.name]) for i in outputs if i.name.startswith("z")])

print(int(result, base=2))
