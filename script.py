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
	subprocess.Popen(["rm", "-rf", " *.txt"])
	server = launchServer()
	time.sleep(.5) # Give the server time to initialize before client tries to connect
	# Initialize user and follower
	testClient = "user"	
	user = launchUser(testClient)
	clientResponse = user.stdout.readline() # Login successful
#	print(clientResponse)
	clientResponse = user.stdout.readline() # Enter commands:
#	print(clientResponse)
	user.stdin.write("CHAT\n")
	user.stdin.write("Initialization message\n")
	user.kill()
	# initialize follower
	testFriend = "friend"
	follower = launchUser(testFriend)
	#print(testFriend)
	friendResponse = follower.stdout.readline() # Welcome back new User
	friendResponse = follower.stdout.readline() # Enter commands: 
	follower.stdin.write("JOIN " + testClient + "\n")
	friendResponse = follower.stdout.readline() # Succesfully joined 
	print(friendResponse)
	follower.stdin.write("CHAT\n") 
	friendResponse = follower.stdout.readline() # Enter messages to chat
	#friendResponse = follower.stdout.readline()
	#friendResponse = follower.stdout.readline()
	# Test the limits of the system
	user = launchUser(testClient)
	clientResponse = user.stdout.readline() # Welcome back User!
	clientResponse = user.stdout.readline() # Enter commands:
	user.stdin.write("CHAT\n")
	clientResponse = user.stdout.readline() # Enter messages to chat 
	message = " This is a test message. Do you copy?\n"
	print("Talker last message: ", clientResponse )
	print("Follower last message: ", friendResponse)
	for i in range(1,500):
		user.stdin.write(message)
		print("Sent: " + message)
		time.sleep(5/i)
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
