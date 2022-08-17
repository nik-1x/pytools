class ExceptionManager:
    def __init__(self):
        pass

    def handle(self, function, args, exception_return, return_print=False):
        try:
            res = function(args)
            return res
        except Exception as e:
            if return_print:
                print(exception_return, e.args)
            else:
                return exception_return, e.args