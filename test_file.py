from file import helloProgram,byeProgram

def test_helloProgram():
  assert helloProgram() == "Hello world"
  assert byeProgram() == "Bye world"