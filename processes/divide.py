from pywps import Process, LiteralInput, LiteralOutput


class Division(Process):
    def __init__(self):
        inputs = [LiteralInput('dividend', 'First Input: Dividend', data_type='integer'),
                  LiteralInput('divisor', 'Second Input: Divisor', data_type='integer')]
        outputs = [LiteralOutput('quotient', 'First Output: Quotient', data_type='integer')]

        super(Division, self).__init__(
            self.handler,
            identifier='division',
            title='Division Process',
            abstract='Dividiert zwei ganze Zahlen',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        response.outputs['quotient'].data = request.inputs['dividend'][0].data // request.inputs['divisor'][0].data
        return response
