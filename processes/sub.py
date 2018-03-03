from pywps import Process, LiteralInput, LiteralOutput


class Substraction(Process):
    def __init__(self):
        inputs = [LiteralInput(identifier='first_arg', title='first Input', data_type='integer', abstract="Minuend"),
                  LiteralInput(identifier='second_arg', title='second Input', data_type='integer', abstract="Subtrahend")]
        outputs = [LiteralOutput(identifier='response', title='Output response', data_type='integer', abstract="Differenz")]

        super(Substraction, self).__init__(
            self.handler,
            identifier='substraction',
            title='Substraction Process',
            abstract='Substrahiert zwei eingegebene ganze Zahlen',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['response'].data = request.inputs['first_arg'][0].data - request.inputs['second_arg'][0].data
        return response
