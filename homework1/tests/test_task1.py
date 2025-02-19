from tasks.task1 import task_one

def test_hello_world_stdout(capsys) -> None:
    ## Run task one so output is captured in stdout
    task_one()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
