"""
An script to configure install all the runtime dependencies required of the
Let's Sched It application-space.

@author: Elias Gabriel
@revision: v1.0
"""
import subprocess


def cmd(command, capture=False):
	""" Executes the given command as a subprocess with the given arguments. """
	return subprocess.run(command, shell=True, check=False, capture_output=capture)


def header(message):
	print("\n\33[95m ===== " + message + "...\33[0m")


if __name__ == "__main__":
	# Confirm that Node.js is installed
	if cmd("node -v && npm -v", True).returncode != 0:
		print("\n\33[91m *** \33[4mInstallation error!\33[0m\33[91m ***")
		print("Node.js and npm are required by the frontend architecture.\nPlease install Node.js and npm using your package manager\n or manually by source, then retry installation.\n")
		exit(1)

	# Confirm that MySQL (MariaDB) is installed
	if cmd("mysql --print-defaults", True).returncode != 0:
		print("\n\33[91m *** \33[4mInstallation error!\33[0m\33[91m ***")
		print("MySQL is required by the backend architecture.\nPlease install MySQL, preferably MariaDB, using \n your package manager, then retry installation.\nDetailed instructions can be found on the official README.\n")
		exit(1)

	# Download Node dependencies
	header("Installing node dependencies")
	cmd("cd ./source/web && npm install")

	# Download Python dependencies
	header("Installing pre-built Python dependencies")
	cmd("pip install -r ./source/api/requirements.txt")

	# Configure MySQL database
	header("Configuring the MySQL database")
	cmd("cd ./source/api && python .pyinitdb")

	print("\n*** \33[92mDependency installation complete!\33[0m ***")
