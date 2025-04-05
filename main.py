#!/usr/bin/env python3

import sys
from container import run_container

def run_interactive():
    """Run container in interactive mode"""
    print("Starting interactive container mode. Type 'exit' or 'quit' to end.")
    while True:
        try:
            # Get user input
            user_input = input("container> ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting container...")
                break
                
            # Skip empty input
            if not user_input:
                continue
                
            # Split command and arguments
            parts = user_input.split()
            command = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            
            # Run the command
            print(f"Running: {user_input}")
            run_container(command, args)
            
        except KeyboardInterrupt:
            print("\nExiting container...")
            break
        except Exception as e:
            print(f"Error: {e}")

def run_examples():
    """Run various examples of container usage"""
    examples = [
        # Shell command example
        (["/bin/sh", "-c", "echo 'Hello from container!' && pwd && ls -la"], None),
        
        # Python command example
        (["python3", "-c", "print('Hello from Python!'); import os; print('Current directory:', os.getcwd())"], None),
        
        # System command example
        (["ls", "-la", "/"], None),
        
        # Environment variable example
        (["/bin/sh", "-c", "echo $MY_VAR"], {"MY_VAR": "Hello from env!"}),
    ]
    
    for cmd, env in examples:
        print(f"\nRunning: {' '.join(cmd)}")
        run_container(cmd[0], cmd[1:], env)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py run <command> [args...]")
        print("  python main.py examples")
        print("  python main.py interactive")
        return 1

    if sys.argv[1] == "run":
        if len(sys.argv) < 3:
            print("Error: No command specified")
            return 1
        return run_container(sys.argv[2], sys.argv[3:])
    elif sys.argv[1] == "examples":
        run_examples()
        return 0
    elif sys.argv[1] == "interactive":
        run_interactive()
        return 0
    else:
        print(f"Unknown command: {sys.argv[1]}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 