all: clean user_service

user_service: user_service.proto
	mkdir -p rpc/proto
	mkdir -p proto
	cp user_service.proto rpc/proto
	cp user_service.proto proto

	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. rpc/proto/user_service.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. proto/user_service.proto

	mkdir -p ../user_service/source/rpc/proto/
	mkdir -p ../post_service/source/proto/

	cp rpc/proto/user_service_*.py ../user_service/source/rpc/proto/
	cp proto/user_service_*.py ../post_service/source/proto/

	rm -rf rpc/
	rm -rf proto/

clean:
	rm -rf ../post_service/source/proto/*
	rm -rf ../user_service/source/rpc/proto/*
