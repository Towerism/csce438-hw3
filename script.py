#! python3
# Run the client with one follower, figure out maximum RPC calls
import subprocess

def main():
				print("In main function");
				proc = subprocess.Popen(["ls", "-l"], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
				output = proc.communicate()[0]
				print(output)
				
				

if __name__ == "__main__":
				main()
