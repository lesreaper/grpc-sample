## Sample GRPC Install

### Install
```
pip install grpcio-tools
pip install grpcio
```

### Running
Compile the protobufs:
```
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto
```

Run the server: `python greet_server.py`

Run the cilent: `python greet_client.py`