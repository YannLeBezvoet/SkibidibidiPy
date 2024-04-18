from cfg.const import Const
def test_varType():
    assert isinstance(Const.outPath, str)
    assert isinstance(Const.terminalUsage1, str)
    assert isinstance(Const.terminalUsage2, str)
    assert isinstance(Const.terminalOneArg1, str)
    assert isinstance(Const.terminalOneArg2, str)