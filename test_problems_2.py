from problems_2 import get_names, total_marks

def test_get_names():
    users = [
        {
            "name" : "Rohit", "age" : 30
        },
        {
            "name" : "Asha", "age" : 25
        }
    ]
    assert get_names(users) == ["Rohit","Asha"]
    
    users = [ { "name" : "Rohit", "age" : 30} ]
    assert get_names(users) == ["Rohit"]

    users = []
    assert get_names(users) == []


def test_total_marks():
    student = {"name": "Rohit", "marks": [100,100,80]}
    assert total_marks(student) == 280

    student = {"name": "Rohit", "marks": []}
    assert total_marks(student) == 0

    student = {"name": "Rohit"}
    assert total_marks(student) == 0