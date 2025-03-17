from model.project import Project
import random


def test_delete_project(app):
    old_list = app.project.get_project_list()
    if len(old_list) == 0:
        app.project.add_project(Project(name="test", description="text"))
    project = random.choice(old_list)
    app.project.delete_project(project.name)
    new_list = app.project.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list, key=lambda x: x.name) == sorted(new_list, key=lambda x: x.name)
