import pytest
from unittest.mock import Mock, patch
from serial_proxy.serial_proxy import SerialProxy


@pytest.fixture
def mock_serial():
    with patch("serial_proxy.serial_proxy.serial.Serial") as mock:
        yield mock


@pytest.fixture
def mock_logger():
    with patch("serial_proxy.serial_proxy.Logger") as mock:
        yield mock


def test_initialization(mock_serial, mock_logger):
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    mock_serial.assert_called_once_with("/dev/ttyUSB0", 9600)
    mock_logger.assert_called_once_with("serial_log.json")


def test_write(mock_serial, mock_logger):
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    proxy.write(b"test")
    mock_serial.return_value.write.assert_called_once_with(b"test")
    mock_logger.return_value.log.assert_called_once_with("WRITE", b"test")


def test_read(mock_serial, mock_logger):
    mock_serial.return_value.read.return_value = b"test"
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    result = proxy.read(4)
    assert result == b"test"
    mock_serial.return_value.read.assert_called_once_with(4)
    mock_logger.return_value.log.assert_called_once_with("READ", b"test")


def test_readline(mock_serial, mock_logger):
    mock_serial.return_value.readline.return_value = b"test\n"
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    result = proxy.readline()
    assert result == b"test\n"
    mock_serial.return_value.readline.assert_called_once()
    mock_logger.return_value.log.assert_called_once_with("READLINE", b"test\n")


def test_readlines(mock_serial, mock_logger):
    mock_serial.return_value.readlines.return_value = [b"test1\n", b"test2\n"]
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    result = proxy.readlines()
    assert result == [b"test1\n", b"test2\n"]
    mock_serial.return_value.readlines.assert_called_once()
    mock_logger.return_value.log.assert_called_once_with(
        "READLINES", [b"test1\n", b"test2\n"]
    )


def test_flush_operations(mock_serial, mock_logger):
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    proxy.flush()
    proxy.flushInput()
    proxy.flushOutput()
    mock_serial.return_value.flush.assert_called_once()
    mock_serial.return_value.flushInput.assert_called_once()
    mock_serial.return_value.flushOutput.assert_called_once()
    mock_logger.return_value.log.assert_has_calls(
        [
            Mock(args=("FLUSH", "")),
            Mock(args=("FLUSH_INPUT", "")),
            Mock(args=("FLUSH_OUTPUT", "")),
        ]
    )


def test_open_close(mock_serial, mock_logger):
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    proxy.open()
    proxy.close()
    mock_serial.return_value.open.assert_called_once()
    mock_serial.return_value.close.assert_called_once()
    mock_logger.return_value.log.assert_has_calls(
        [Mock(args=("OPEN", "")), Mock(args=("CLOSE", ""))]
    )


def test_context_manager(mock_serial, mock_logger):
    with SerialProxy("/dev/ttyUSB0", 9600) as proxy:
        pass
    mock_serial.return_value.close.assert_called_once()


def test_is_open_property(mock_serial):
    mock_serial.return_value.is_open = True

    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    assert proxy.is_open == True


def test_in_waiting(mock_serial):
    mock_serial.return_value.in_waiting = 5
    proxy = SerialProxy("/dev/ttyUSB0", 9600)
    assert proxy.in_waiting() == 5
