import json
from datetime import datetime
from typing import Union


class Logger:
    def __init__(self, log_file: str):
        self.log_file = log_file

    def log(self, operation: str, data: Union[str, bytes, List[bytes]]) -> None:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "data": self._format_data(data),
        }
        with open(self.log_file, "a") as f:
            json.dump(log_entry, f)
            f.write("\n")  # Add a newline for readability and to separate entries

    def _format_data(self, data: Union[str, bytes, List[bytes]]) -> str:
        if isinstance(data, bytes):
            return data.hex()
        elif isinstance(data, list):
            return [self._format_data(item) for item in data]
        else:
            return str(data)
