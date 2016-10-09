"""Error for API APP Unispan."""


class HTTPError(Exception):
    """Custom class for HTTPError."""

    def __init__(self, status_code,
                 developer_message="",
                 user_message="",
                 error_code="",
                 more_info=""):
        """Initialize of error messages and error code."""
        self.status_code = status_code
        self.developer_message = developer_message
        self.user_message = user_message
        self.error_code = error_code
        self.more_info = more_info

    @staticmethod
    def handle(ex, req, resp, params):
        """Handle for message."""
        response = {}
        response.update({"status": ex.status_code})
        if ex.dev_msg:
            response.update({"developer_message": ex.developer_message})
        if ex.user_msg:
            response.update({"user_message": ex.user_message})
        if ex.error_code:
            response.update({"error_code": ex.error_code})
        if ex.more_info:
            response.update({"more_info": ex.more_info})

        resp.body = response
        resp.status = str(ex.status_code)
