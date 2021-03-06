from pywps import Process, LiteralInput, LiteralOutput


class Square(Process):
    def __init__(self):
        inputs = [LiteralInput(identifier='arg', title='Input number', data_type='integer', abstract="Argument")]
        outputs = [LiteralOutput(identifier='response', title='Output response', data_type='integer', abstract="Result")]

        super(Square, self).__init__(
            self.handler,
            identifier='square',
            title='Square Process',
            abstract='Quadriert den Input',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['response'].data = request.inputs['arg'][0].data ** 2
        return response
