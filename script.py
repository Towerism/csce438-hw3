#! python3
# Run the client with one follower, figure out maximum RPC calls
import subprocess
import time
portNumber = 12323

def launchServer():
	proc = subprocess.Popen(["./fbsd", "-p", str(portNumber)], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	return proc

def launchUser(username):
	proc = subprocess.Popen(["./fbc", "-h", "localhost", "-p",str(portNumber), "-u", username], stderr = subprocess.PIPE, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
	return proc

def main():
	server = launchServer()
	time.sleep(.5) # Give the server time to initialize before client tries to connect
	# Initialize user and follower
	testClient = "talker"
	user = launchUser(testClient)
	user.stdin.write("CHAT\n")
	print(user.stdout.readline())
	user.stdin.write("Initialization message\n")
	print(user.stdout.readline())
	user.kill()
	# initialize follower
	testClient = "follower"
	follower = launchUser(testClient)
	follower.stdin.write("JOIN " + testClient + "\n")
	print(follower.stdout.readline())
	follower.stdin.write("CHAT\n")
	print(follower.stdout.readline())
	# Test the limits of the system
	user = launchUser(testClient)
	user.stdin.write("CHAT\n")
	message = " This is a test message. Do you copy?\n"
	for i in range(1,500):
		user.stdin.write(message)
		print("Sent: " + message)
		time.sleep(1/i)
		response = follower.stdout.readline()
		print("Received: " + response)
		if response is not message:
			print("Maximum rate before packets dropped found: 1/" + str(i))
			break
	# Close up shop
	user.kill()
	follower.kill()
	server.kill()
			
				

if __name__ == "__main__":
				main()
