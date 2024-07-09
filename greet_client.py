import greet_pb2_grpc
import greet_pb2
import time
import grpc


def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            request = greet_pb2.HelloRequest(greeting="Hello", name="Adam 7k")
            reply = stub.SayHello(request)
            print("Say Hello response received: ", reply.message)
        elif choice == "2":
            request = greet_pb2.HelloRequest(greeting="Hello", name="Adam 8k")
            replies = stub.ParrotSaysHello(request)

            for hello_reply in replies:
                print("ParrotSaysHello Response Received:")
                print(hello_reply)
        elif choice == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

            print("ChattyClientSaysHello Response Received:")
            print(delayed_reply)
        elif choice == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("InteractingHello Response Received: ")
                print(response)



if __name__ == "__main__":
    run()
