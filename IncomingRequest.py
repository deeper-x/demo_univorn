class IncomingRequest:
    def __init__(self, scope):
        self._scope = scope
    async def __call__(self, receive, send):
        body = f"received {self._scope['method']} - {self._scope['path']} - {self._scope}" 
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': body.encode('utf-8')
        })


