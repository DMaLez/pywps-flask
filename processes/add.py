from pywps import Process, LiteralInput, LiteralOutput


class Addition(Process):
    def __init__(self):
        inputs = [LiteralInput(identifier='first_arg', title='first Input', data_type='integer', abstract="Erster Summand"),
                  LiteralInput(identifier='second_arg', title='second Input', data_type='integer', abstract="Zweiter summand")]
        outputs = [LiteralOutput(identifier='response', title='Output response', data_type='integer', abstract="Summe")]

        super(Addition, self).__init__(
            self.handler,
            identifier='addition',
            title='Addition Process',
            abstract='Addiert zwei eingegebene ganze Zahlen (integers)',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['response'].data = request.inputs['first_arg'][0].data + request.inputs['second_arg'][0].data
        return response
