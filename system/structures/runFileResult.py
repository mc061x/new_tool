class RunFileResult:
    def __init__(self, run_time, run_memory, run_returncode) -> None:
        self.time = run_time
        self.memory = run_memory
        self.returncode = run_returncode
