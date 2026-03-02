import pytest
from main_module import calculate_area, process_list, Student

def test_calculate_area_valid():
    assert calculate_area(2) == pytest.approx(12.566370614359172)

def test_calculate_area_invalid():
    assert calculate_area(-1) is None

def test_calculate_area_type_error():
    with pytest.raises(ValueError):
        calculate_area("bad")

def test_process_list_even():
    assert process_list([1, 2, 3, 4]) == 6

def test_process_list_type_error():
    with pytest.raises(ValueError):
        process_list([1, "bad", 3])

def test_student_display(capsys):
    s = Student("Alice", 22)
    s.display()
    captured = capsys.readouterr()
    assert "Alice" in captured.out and "22" in captured.out