from model.project import Project
import random
import string


def test_add_project(app):
    old_list = app.soap.get_project_list()
    project = Project(name=''.join(random.choice(string.ascii_letters) for i in range(8)), description="text")
    app.project.add_project(project)
    new_list = app.soap.get_project_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(project)
    assert sorted(old_list, key=lambda x: x.name) == sorted(new_list, key=lambda x: x.name)
