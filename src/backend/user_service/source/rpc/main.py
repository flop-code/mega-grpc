import asyncio
import grpc

from config import settings
from rpc.service import GRPCUserService
from rpc.proto import user_service_pb2_grpc


_cleanup_coroutines = []


async def serve() -> None:
    server = grpc.aio.server()
    user_service_pb2_grpc.add_UserServicer_to_server(GRPCUserService(), server)
    server.add_insecure_port(f"[::]:{settings.GRPC_PORT}")
    await server.start()
    print("GRPC Server started.")

    async def graceful_shutdown():
        print("Graceful shutdown countdown...")
        await server.stop(5)
        print("Shutting down...")

    _cleanup_coroutines.append(graceful_shutdown())
    await server.wait_for_termination()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
