import threading


class InitMS:

    def __init__(self):
        self.microservices = []
        self.threads = []

    def register(self, name, func, args=()):
        self.microservices.append({
            "id": name,
            "func": func,
            "args": args
        })
        return self

    def run_microservices(self):
        for service in self.microservices:
            def service_initiator():
                service["func"](args=service["args"])
            service_ = threading.Thread(name=service["id"], target=service_initiator, args=())
            service_.start()
            self.threads.append(service_)
        return self