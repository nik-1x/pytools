import os
import requests


class File:

    def __init__(self, file_path: str, create_if_not_exists: bool = False, on_empty_write_data: str = "{}"):
        self.path = file_path
        if create_if_not_exists:
            if not os.path.exists(file_path):
                if "/" in file_path:
                    print("Creating directory:", os.makedirs("/".join(self.path.split("/")[:-1])))
                with open(self.path, "w") as file:
                    print("Creating file:", self.path)
                    file.write(on_empty_write_data)
                    file.close()

    def read(self) -> str:
        with open(self.path, "r") as file:
            data = file.read()
            file.close()
            return data

    def load(self) -> str or dict:
        if self.path.endswith(".json"):
            data = requests.get(self.path).json()
        else:
            data = requests.get(self.path).content

        return data

    def write(self, data):
        with open(self.path, "w") as file:
            file.write(data)
            file.close()
        return self
