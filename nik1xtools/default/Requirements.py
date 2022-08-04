from threading import Thread


def requirements(rq_list: list):
    for rq in rq_list:
        Thread(target=pip_install, args=(rq,), name=rq, daemon=True).start()


def pip_install(requirement_name):
    import subprocess
    subprocess.call([
        "pip", "install", requirement_name
    ])
