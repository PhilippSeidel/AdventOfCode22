def get_all_contained_directories(component):
    contained_directories = []
    if isinstance(component, Directory):
        for c in component.components:
            contained_directories.extend(get_all_contained_directories(c))
        contained_directories.append(component)
    return contained_directories


class FileSystem:
    def __init__(self, home_directory, current_directory):
        self.home_directory = home_directory
        self.current_directory = current_directory

    def update_sizes(self):
        self.home_directory.update_size()

    def get_all_directories(self):
        return get_all_contained_directories(self.home_directory)


class Component:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def set_size(self, new_size):
        self.size = new_size

    def update_size(self):
        pass


class File(Component):
    pass


class Directory(Component):
    def __init__(self, name, size, parent):
        super().__init__(name, size, parent)
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def contains_name(self, name):
        for c in self.components:
            if c.name == name:
                return True
        return False

    def get_component_by_name(self, name):
        for c in self.components:
            if c.name == name:
                return c

    def update_size(self):
        self.size = 0
        for c in self.components:
            c.update_size()
            self.size += c.size

    def __lt__(self, other):
        return self.size < other.size
