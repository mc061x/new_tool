class RunConfig:
    def __init__(self) -> None:
        self.TimeLimit = 2
        self.MemoryLimit = 64 * 1024
        self.InputFilePath = ''
        self.OutputFilePath = ''

        self.BuildCommand = f'g++ $FILENAME'
        self.BuildArgs = '-std=c++20 -fdiagnostics-color=always -fmax-errors=2 -o $FILENAME.out'

        self.RunCommand = f'./$FILENAME.out'
        self.RunArgs = ''
        self.clearExecutable = True

        self.RunnerPollTime = 0.05
    
    def format_commands(self, pattern_old: str, pattern_new: str) -> None:
        old_dict: dict = self.__dict__
        for key in old_dict:
            old_instance: str = getattr(self, key)
            if type(old_instance) != str:
                continue
            setattr(self, key, old_instance.replace(pattern_old, pattern_new))
    
    def format_run_command(self):
        if self.InputFilePath != '':
            self.RunCommand += f'< {self.InputFilePath}'
        if self.OutputFilePath != '':
            self.RunCommand += f'> {self.OutputFilePath}'