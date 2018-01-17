from pywps import Process, LiteralInput, LiteralOutput


class Increment(Process):
    def __init__(self):
        inputs = [LiteralInput('arg', 'Input number', data_type='integer')]
        outputs = [LiteralOutput('response', 'Output response', data_type='integer')]

        super(Increment, self).__init__(
            self.handler,
            identifier='increment',
            title='Increment Process',
            abstract='Inkrementiert den Input',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['response'].data = request.inputs['arg'][0].data + 1
        return response
