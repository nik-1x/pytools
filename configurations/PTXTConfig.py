from dataclasses import dataclass
from ..default.FileManager import File


@dataclass
class PTXT:
    config_file: str
    empty_config: str = "#\n# That is config, for pyquiz.\n# pytools-txt config format\n#\n# Format of messages:\n#\n#    <question>:<answer_type>\n#\n# <question> - any string message, can contains emoji, any symbols, telegram text markdown, and n\n# <answer_type> - type of answer, can be string,integer,float,bool2(yes/true/no/false)\n#"

    def data(self):
        data = File(self.config_file, on_empty_write_data="# FILL", create_if_not_exists=True)
        values = data.read().split("\n")
        variables = []
        for str_ in values:
            if not str_.startswith("#"):
                variables.append(str_)
        data_found = []
        for var in variables:
            vardata = var.split(":")  # [0] - text, [required_type]
            text, type_ = vardata[0], vardata[1]
            if type_ not in "string,integer,float,bool2".split(","):
                raise Exception("Incorrect type")
            data_found.append({
                "text": text,
                "type": type_
            })
        return data_found