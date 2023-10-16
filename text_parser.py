from uas import UAV

import re
BETWEEN_PAR =  r'\(([^()]+)\)' #r'\((.*?)\)'

input_text = """
std (
    instant := 0
);

var (
    a := uav[id=001][resource=100],
    b := uav[id=002][resource=200],
    netzone_x := netzone[x=2|y=3][users=13],
    netzone_y := netzone[x=5|y=2][users=3]
);

rel (
    a: attached -> netzone_x,
    b: attached -> netzone_y,
    a: linked -> b
);
"""









class TextParser:
    @staticmethod
    def parse(input_text) -> list:
        parsed_objects = dict()
        text: str = input_text.replace(" ", "").replace("\n", "")
        for block in text.split(";"):
            if not len(block):
                continue

            block_content = re.search(BETWEEN_PAR, block)
            if not block_content:
                continue
            block_lines = block_content.group(1).split(",")

            if block.startswith("std"):
                parsed_objects.update(TextParser.parse_std_block(block_lines))
            elif block.startswith("var"):
                parsed_objects.update(TextParser.parse_var_block(block_lines))
            elif block.startswith("rel"):
                parsed_objects.update(TextParser.parse_rel_block(block_lines))

        return parsed_objects

    @staticmethod
    def parse_std_block(block_lines: list) -> dict:
        return dict()

    @staticmethod
    def parse_var_block(block_lines: list) -> dict:
        parsed_objects = []
        for line in block_lines:
            var_name, var_value = line.split(":=")
            if var_value.startswith("uav"):
                uav = UAV(
                    name=var_name,
                    battery_level=0,
                    serving_zone=None
                )
                parsed_objects[f"{var_name}_{id(uav)}"] = uav

        return parsed_objects

    @staticmethod
    def parse_rel_block(block_lines: list) -> dict:
        return dict()
