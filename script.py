#! python3
# Run the client with one follower, figure out maximum RPC calls
import subprocess

def launchServer():
	proc = subprocess.Popen(["./fbsd", "-p", "12323"], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	return proc

def main():
	server = launchServer()
	proc = subprocess.Popen(["ls", "-l"], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	output = proc.communicate()[0]
	print(output)
				
				

if __name__ == "__main__":
				main()
