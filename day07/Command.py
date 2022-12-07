import FileSystem as fs


class Command:
    def execute(self, file_system):
        pass


class CreateFileCommand(Command):
    def __init__(self, file_name, file_size):
        self.file_name = file_name
        self.file_size = file_size

    def execute(self, file_system):
        if not file_system.current_directory.contains_name(self.file_name):
            file_system.current_directory.add_component(fs.File(self.file_name,
                                                                self.file_size, file_system.current_directory))


class CreateDirectoryCommand(Command):
    def __init__(self, directory_name, directory_size):
        self.directory_name = directory_name
        self.directory_size = directory_size

    def execute(self, file_system):
        if not file_system.current_directory.contains_name(self.directory_name):
            file_system.current_directory.add_component(fs.Directory(self.directory_name,
                                                                     self.directory_size,
                                                                     file_system.current_directory))


class ChangeDirectoryCommand(Command):
    def __init__(self, target_directory_name):
        self.target_directory_name = target_directory_name

    def execute(self, file_system):
        if self.target_directory_name == '/':
            file_system.current_directory = file_system.home_directory
        elif self.target_directory_name == "..":
            file_system.current_directory = file_system.current_directory.parent
        elif file_system.current_directory.contains_name(self.target_directory_name):
            file_system.current_directory = \
                file_system.current_directory.get_component_by_name(self.target_directory_name)

