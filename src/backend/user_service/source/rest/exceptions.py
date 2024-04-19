from fastapi import HTTPException, status


class UnauthorizedError(HTTPException):
    def __init__(self,
                 detail: str = "Not logged in.",
                 status_code: int = status.HTTP_401_UNAUTHORIZED,
                 *args):
        super().__init__(status_code=status_code, detail=detail, *args)
