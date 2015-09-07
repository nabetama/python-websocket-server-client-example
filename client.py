from websocket import create_connection
ws = create_connection("ws://localhost:9090/ws")
print "Sending 'Hello, world.'"
ws.send("Hello, world.")
print "Sent"

print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()
