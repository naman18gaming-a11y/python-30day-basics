"""Check whether Anaconda/conda and the current Python environment work."""

import os
import shutil
import subprocess
import sys


def run_command(command):
	try:
		result = subprocess.run(
			command, capture_output=True, text=True, check=False
		)
		return result.returncode, (result.stdout or result.stderr).strip()
	except OSError as error:
		return 1, str(error)


def main():
	print("Anaconda/conda and virtual environment check\n")

	conda = shutil.which("conda")
	if conda:
		code, output = run_command([conda, "--version"])
		print(f"[{'OK' if code == 0 else 'FAIL'}] Conda: {output}")
		code, output = run_command([conda, "info", "--envs"])
		print(f"[{'OK' if code == 0 else 'FAIL'}] Conda environments:")
		print(output or "No environments found.")
	else:
		print("[FAIL] Conda was not found on PATH.")
		print("       Open Anaconda Prompt or add Anaconda to PATH.")

	print(f"\n[OK] Python executable: {sys.executable}")
	print(f"[OK] Python version: {sys.version.split()[0]}")
	print(f"[OK] Active environment: {os.environ.get('CONDA_DEFAULT_ENV', 'not a conda environment')}")
	print(f"[OK] Virtual environment prefix: {sys.prefix}")

	if sys.prefix != sys.base_prefix:
		print("[OK] A Python virtual environment is active.")
	elif os.environ.get("CONDA_PREFIX"):
		print("[OK] A conda environment is active.")
	else:
		print("[INFO] No virtual or conda environment is currently active.")

	code, output = run_command([sys.executable, "-c", "import sys; print('Python can run code successfully')"])
	print(f"[{'OK' if code == 0 else 'FAIL'}] Python execution: {output}")


if __name__ == "__main__":
	main()
