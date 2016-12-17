#!/usr/bin/python

wire_cache = {}
gate_cache = []

class SourceClass:
    def value(self):
        raise Exception

    @classmethod
    def parseSourceString(cls, source_string):
        src_parts = source_string.split(' ')
        if len(src_parts) == 1:
            try:
                return ValueSource(int(src_parts[0]))
            except ValueError:
                if src_parts[0] in wire_cache:
                    return wire_cache[src_parts[0]]
                return WireSource(src_parts[0])
        else:
            return GateClass.parseParts(src_parts)

class GateClass(SourceClass):
    @classmethod
    def parseParts(cls, src_parts):
        if len(src_parts) == 2:
            return NotGate(src_parts[1])
        else:
            if src_parts[1] == 'AND':
                return AndGate(src_parts[0], src_parts[2])
            if src_parts[1] == 'OR':
                return OrGate(src_parts[0], src_parts[2])
            if src_parts[1] == 'LSHIFT':
                return LeftShiftGate(src_parts[0], src_parts[2])
            if src_parts[1] == 'RSHIFT':
                return RightShiftGate(src_parts[0], src_parts[2])

    def value(self):
        raise Exception

class NotGate(GateClass):
    def __init__(self, val_str):
        self._inputs = [SourceClass.parseSourceString(val_str)]
        gate_cache.append(self)

    def value(self):
        return ~self._inputs[0].value() % 65536

class TwoInputGateClass(GateClass):
    _oper = None

    def __init__(self, val1_str, val2_str):
        self._inputs = [
            SourceClass.parseSourceString(val1_str),
            SourceClass.parseSourceString(val2_str)
        ]
        self._calculated = None
        gate_cache.append(self)

class AndGate(TwoInputGateClass):
    _oper = "AND"

    def value(self):
        if self._calculated is None:
            self._calculated = self._inputs[0].value() & self._inputs[1].value()
        return self._calculated

class OrGate(TwoInputGateClass):
    _oper = "OR"

    def value(self):
        if self._calculated is None:
            self._calculated = self._inputs[0].value() | self._inputs[1].value()
        return self._calculated

class LeftShiftGate(TwoInputGateClass):
    _oper = "LSHIFT"

    def value(self):
        if self._calculated is None:
            self._calculated = self._inputs[0].value() << self._inputs[1].value()
        return self._calculated

class RightShiftGate(TwoInputGateClass):
    _oper = "RSHIFT"

    def value(self):
        if self._calculated is None:
            self._calculated = self._inputs[0].value() >> self._inputs[1].value()
        return self._calculated

class WireSource(SourceClass):
    def __init__(self, wire):
        self._wire_name = wire
        self._inputs = []
        self._calculated = None
        wire_cache[self._wire_name] = self

    def set_input(self, input):
        self._inputs = [input]

    def value(self):
        if len(self._inputs) == 0:
            raise Exception
        elif self._calculated is None:
            self._calculated = self._inputs[0].value()
        return self._calculated
            

class ValueSource(SourceClass):
    def __init__(self, val):
        self._inputs = [val]

    def value(self):
        return self._inputs[0]

with open('instructions') as f:
    for line in f:
        src, target = line.strip().split(' -> ')
        output = SourceClass.parseSourceString(target)
        output.set_input(SourceClass.parseSourceString(src))

val_a = wire_cache['a'].value()
print "WIRE: a -> {0}".format(val_a)

print "\nRESET"
print "{0} -> b\n".format(val_a)

for gate in gate_cache:
    gate._calculated = None
for wire in wire_cache:
    wire_cache[wire]._calculated = None
wire_cache['b']._inputs = [ValueSource(val_a)]

new_val_a = wire_cache['a'].value()
print "WIRE: a -> {0}".format(new_val_a)
