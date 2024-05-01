# Create a bridge pattern to handle messages sent over different communication protocols (e.g., HTTP, WebSocket, MQTT).

# Scenario: In this exercise, the Bridge pattern is used to abstract the complexities of different communication
# protocols. Systems often need to communicate over various channels, such as HTTP, WebSocket, or MQTT, depending on
# the use case (e.g., IoT devices might prefer MQTT due to its low power and bandwidth usage, while a web application
# might use WebSockets for real-time communication).
#
# Explanation: By implementing a bridge between the high-level logic of sending messages and the low-level details of
# each communication protocol, the system can switch protocols without any impact on the message-sending code. This
# separation enhances the flexibility and scalability of the communication system.
#






if __name__ == '__main__':
    http_communicator = HTTPCommunicator()
    websocket_communicator = WebSocketCommunicator()

    message_sender = MessageSender(http_communicator)
    message_sender.send("Hello over HTTP!")

    message_sender.switch_protocol(websocket_communicator)
    message_sender.send("Hello over WebSocket!")
