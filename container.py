import os
import subprocess
import sys
from typing import List, Optional

class Container:
    def __init__(self, rootfs: str, command: str, args: List[str] = None, env: Optional[dict] = None):
        self.rootfs = rootfs
        self.command = command
        self.args = args or []
        self.env = env or {}

    def run(self) -> int:
        """Run the containerized command"""
        try:
            # Prepare the command
            cmd = [self.command] + self.args
            
            # Set up the process
            process = subprocess.Popen(
                cmd,
                stdin=sys.stdin,
                stdout=sys.stdout,
                stderr=sys.stderr,
                env={**os.environ, **self.env},
                preexec_fn=self._setup_process
            )
            
            # Wait for the process to complete
            return process.wait()
        except Exception as e:
            print(f"Error running container: {e}", file=sys.stderr)
            return 1

    def _setup_process(self):
        """Setup process isolation (Unix-like systems only)"""
        try:
            # Set process group ID
            os.setpgid(0, 0)
        except Exception as e:
            print(f"Warning: Could not set process group: {e}", file=sys.stderr)

def run_container(command: str, args: List[str] = None, env: dict = None) -> int:
    """Helper function to create and run a container"""
    container = Container("", command, args, env)
    return container.run() 