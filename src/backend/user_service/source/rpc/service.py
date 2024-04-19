from rpc.proto import user_service_pb2, user_service_pb2_grpc
from rpc.dependencies import UserServiceWrapper
from models import User

import grpc


class GRPCUserService(user_service_pb2_grpc.UserServicer):
    @staticmethod
    def __generate_response(request: user_service_pb2.UserInfoByTokenRequest | user_service_pb2.UserInfoByIdRequest,
                            context: grpc.aio.ServicerContext,
                            user: User | None) -> user_service_pb2.UserInfoResponse:
        response = user_service_pb2.UserInfoResponse()

        if user is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            return response

        for field in request.fields.paths:
            setattr(response, field, getattr(user, field))

        return response

    async def GetUserInfoByToken(self,
                                 request: user_service_pb2.UserInfoByTokenRequest,
                                 context: grpc.aio.ServicerContext) -> user_service_pb2.UserInfoResponse:
        async with UserServiceWrapper() as user_service:
            user = await user_service.get_current_user(request.user_token)
            return GRPCUserService.__generate_response(request, context, user)

    async def GetUserInfoById(self,
                              request: user_service_pb2.UserInfoByIdRequest,
                              context: grpc.aio.ServicerContext) -> user_service_pb2.UserInfoResponse:
        async with UserServiceWrapper() as user_service:
            user = await user_service.get_user_by_id(request.user_id)
            return GRPCUserService.__generate_response(request, context, user)
