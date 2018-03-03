from pywps import Process, LiteralInput, LiteralOutput


class Multiplication(Process):
    def __init__(self):
        inputs = [LiteralInput('first_arg', 'Multiplier', data_type='integer'),
                  LiteralInput('second_arg', 'Multiplicand', data_type='integer')]
        outputs = [LiteralOutput('response', 'Output response', data_type='integer')]

        super(Addition, self).__init__(
            self.handler,
            identifier='multiplication',
            title='Multiplication Process',
            abstract='Multipliziert zwei ganze Zahlen',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['response'].data = request.inputs['first_arg'][0].data * request.inputs['second_arg'][0].data
        return response
