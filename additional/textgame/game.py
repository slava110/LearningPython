import re
import os
import sys
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class World:

    def __init__(self):
        self.locations: dict[str, 'WorldLocation'] = {}

    def add_location(self, name, location: 'WorldLocation'):
        self.locations[name] = location

    def validate(self):
        if "начало" not in self.locations:
            raise RuntimeError("Локация `начало` не определена!")
        if "конец" not in self.locations:
            raise RuntimeError("Локация `конец` не определена!")

        dead_ends = []

        for locId, loc in self.locations.items():
            if locId != "конец" and not loc.transitions:
                dead_ends.append((locId, loc))

        if dead_ends:
            for (locId, loc) in dead_ends:
                print(f"Локация `{locId}` (`{loc.name}`) - тупик!")
            raise RuntimeError("Найдены тупики на карте!")

    def generate_graph(self, with_labels=False):
        parts = ["digraph G {\n"]

        for loc_id, loc in self.locations.items():
            parts.append(f"\t\"{loc_id}\" [label=\"{loc.name}\"]\n")
            for trans in loc.transitions:
                parts.append(f"\t\"{loc_id}\" -> \"{trans[2]}\"")
                if with_labels:
                    parts.append(" [label=\"{ trans[0] }\"]\n")
                parts.append("\n")

        parts.append("\n}")

        return ''.join(parts)

    def enter(self):
        self.locations["начало"].enter()


class WorldLocation:

    def __init__(self, world: World, name: str):
        self.world = world
        self.name = name
        self.text = ""
        self.transitions: list[tuple[str, str, str]] = []

    def add_transition(self, text: str, trans_msg: str, dest: str):
        self.transitions.append((text, trans_msg, dest))

    def enter(self):
        print(f"<=== {self.name} ===>")
        print(self.text)

        if self.transitions:
            print("\nПроходы:\n")

            for i, [text, _, _] in enumerate(self.transitions):
                print(f"[{i + 1}] {text}")

            print("\n")

            while True:
                next_num = input("Введите номер следующей комнаты: ")
                if next_num.isdigit():
                    next_num = int(next_num)

                    if next_num < 1 or next_num > len(self.transitions):
                        print("Нет такого прохода!")
                        continue

                    break
                else:
                    print("Я СКАЗАЛ ВВЕДИТЕ НОМЕР!")

            next_num -= 1
            next_trans = self.transitions[next_num]
            next_loc_id = next_trans[2]

            cls()

            print(next_trans[1])
            time.sleep(1)

            cls()

            self.world.locations[next_loc_id].enter()
        else:
            print("Нажмите любую клавишу чтобы выйти")
            input()
            exit(0)


locationDefRegex = r'##\s*\[(.+)\]\(#(.+)\)'
transitionDefRegex = r'\*\s+(.+)\s+\[(.+)]\(#(.+)\)'


def parse_world(world_file: str) -> World:
    world = World()
    locationId: str | None = None
    location: WorldLocation | None = None

    with open(world_file, mode="r", encoding="UTF-8") as file:
        lineIter = iter(file.readline, '')
        for line in lineIter:
            line = line.strip('\n ')
            match = re.search(locationDefRegex, line)
            if match:
                if locationId is not None:
                    world.add_location(locationId, location)

                locationId = convert_to_md_compatible(match.group(2))
                location = WorldLocation(world, match.group(1))
            elif locationId is not None:
                match = re.search(transitionDefRegex, line)
                if match:
                    location.add_transition(match.group(1), match.group(2), match.group(3))
                elif not location.transitions:
                    location.text += line

    if locationId is not None:
        world.add_location(locationId, location)

    return world


def convert_to_md_compatible(name: str):
    return name.lower().replace(' ', '-')


graphMode = False
if "-graph" in sys.argv:
    graphMode = True

pWorld = parse_world("game.md")
try:
    pWorld.validate()
    if graphMode:
        print(pWorld.generate_graph())
    else:
        pWorld.enter()
except RuntimeError as err:
    print(err)
