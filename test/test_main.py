import main
import pytest

def test_main(capsys: pytest.CaptureFixture[str]):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main.main()
    assert pytest_wrapped_e.type == SystemExit
    consol_output = capsys.readouterr()
    consol_output = consol_output.out.split('\n')
    expectedLine1 = "SkibidibidiPy by Yann Le Bezvoet - dev 1"
    expectedLine2 = "\tUsage : skibidibidipy /path/to/skibidibidiPython/code"
    assert consol_output[0] == expectedLine1
    assert consol_output[1] == expectedLine2
    