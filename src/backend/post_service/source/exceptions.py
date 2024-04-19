from fastapi import HTTPException, status


class UnauthorizedError(HTTPException):
    def __init__(self,
                 detail: str = "Not logged in.",
                 status_code: int = status.HTTP_401_UNAUTHORIZED,
                 *args):
        super().__init__(status_code=status_code, detail=detail, *args)


class DeleteForbiddenError(HTTPException):
    def __init__(self,
                 detail: str = "You cannot delete this content because you are not its author.",
                 status_code: int = status.HTTP_403_FORBIDDEN,
                 *args):
        super().__init__(status_code=status_code, detail=detail, *args)


class PostNotFoundError(HTTPException):
    def __init__(self,
                 detail: str = "Post not found.",
                 status_code: int = status.HTTP_404_NOT_FOUND,
                 *args):
        super().__init__(status_code=status_code, detail=detail, *args)
