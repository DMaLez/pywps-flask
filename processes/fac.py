from pywps import Process, LiteralInput, LiteralOutput


class Factorial(Process):
    def __init__(self):
        inputs = [LiteralInput(identifier='arg', title='Argument', data_type='integer', abstract="Argument")]
        outputs = [LiteralOutput(identifier='response', title='Output response', data_type='integer', abstract="Summe")]

        super(Factorial, self).__init__(
            self.handler,
            identifier='factorial',
            title='Factorial Process',
            abstract='Berechnet die Fakultät Funktion einer eingegebenen ganzen Zahl',
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def handler(self, request, response):
        number = request.inputs['first_arg'][0].data
        response.outputs['response'].data = self.factorial(number)
        return response

    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)
