import serial
from typing import Union, List, Optional
from .logger import Logger


class SerialProxy:
    def __init__(self, port: str, baudrate: int, log_file: str = "serial_log.json"):
        self.serial = serial.Serial(port, baudrate)
        self.logger = Logger(log_file)

    def write(self, data: Union[str, bytes]) -> int:
        self.logger.log("WRITE", data)
        return self.serial.write(data)

    def read(self, size: int = 1) -> bytes:
        data = self.serial.read(size)
        self.logger.log("READ", data)
        return data

    def readline(self) -> bytes:
        data = self.serial.readline()
        self.logger.log("READLINE", data)
        return data

    def readlines(self) -> List[bytes]:
        data = self.serial.readlines()
        self.logger.log("READLINES", data)
        return data

    def in_waiting(self) -> int:
        return self.serial.in_waiting

    def flush(self) -> None:
        self.logger.log("FLUSH", "")
        return self.serial.flush()

    def flushInput(self) -> None:
        self.logger.log("FLUSH_INPUT", "")
        return self.serial.flushInput()

    def flushOutput(self) -> None:
        self.logger.log("FLUSH_OUTPUT", "")
        return self.serial.flushOutput()

    def close(self) -> None:
        self.logger.log("CLOSE", "")
        return self.serial.close()

    def open(self) -> None:
        self.logger.log("OPEN", "")
        return self.serial.open()

    def __enter__(self) -> "SerialProxy":
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ) -> None:
        self.close()

    @property
    def is_open(self) -> bool:
        return self.serial.is_open
