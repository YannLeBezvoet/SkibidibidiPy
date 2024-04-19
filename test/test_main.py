import main
import pytest
from cfg.const import Const
from unittest.mock import patch
import sys

def test_main_NoArg(capsys: pytest.CaptureFixture[str]):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main.main()
    assert pytest_wrapped_e.type == SystemExit
    consol_output = capsys.readouterr()
    consol_output = consol_output.out.split('\n')
    expectedLine1 = Const.terminalUsage1
    expectedLine2 = Const.terminalUsage2
    assert consol_output[0] == expectedLine1
    assert consol_output[1] == expectedLine2

def test_main_OneArg(capsys: pytest.CaptureFixture[str]):
    with patch("sys.argv", [sys.argv[0], "ArgOne"]):
            with pytest.raises(SystemExit) as pytest_wrapped_e:
                main.main()
    assert pytest_wrapped_e.type == SystemExit
    expectedLine = f"{Const.terminalOneArg1}1{Const.terminalOneArg2}"
    consol_output = capsys.readouterr()
    consol_output = consol_output.out.split('\n')
    consol_output[0] = expectedLine
    
def test_main_TooManyArg(capsys: pytest.CaptureFixture[str]):
    with patch("sys.argv", [sys.argv[0], "ArgOne", "ArgTwo", "ArgTree"]):
            with pytest.raises(SystemExit) as pytest_wrapped_e:
                main.main()
    assert pytest_wrapped_e.type == SystemExit
    expectedLine = f"{Const.terminalOneArg1}3{Const.terminalOneArg2}"
    consol_output = capsys.readouterr()
    consol_output = consol_output.out.split('\n')
    consol_output[0] = expectedLine
    