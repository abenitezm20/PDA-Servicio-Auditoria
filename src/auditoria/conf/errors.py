class ApiError(Exception):
    code = 500
    description = "server error"