class BasicUsage():
    def __init__(self, scope):
        self._scope = scope
    
    async def __call__(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain']
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': b'hello, uvicorn'
        })