from pywps import Process, LiteralInput, LiteralOutput


class Addition(Process):
    def __init__(self):
        inputs = [LiteralInput('first_arg', 'first Input', data_type='integer'),
                  LiteralInput('second_arg', 'second Input', data_type='integer')]
        outputs = [LiteralOutput('response', 'Output response', data_type='integer')]

        super(Addition, self).__init__(
            self.handler,
            identifier='addition',
            title='Addition Process',
            abstract='Addiert zwei Input Zahlen (integers)',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['response'].data = 'Result' + str(request.inputs['first_arg'][0].data + request.inputs['second_arg'][0].data)
        return response
