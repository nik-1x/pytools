from nik1xtools.exceptions.Handling import ExceptionManager

ehandler = ExceptionManager()

def print_(args):
    int(args)

print(
    ehandler.handle(function=print_, args=("dadwa", "dawddaw"), exception_return="Error", return_print=False)
)
