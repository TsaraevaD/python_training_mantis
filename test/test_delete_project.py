from fixture.project import Project
import random


def test_delete_project(app):
    old_list = app.project.get_project_list()
    if old_list == 0:
        app.project.add(Project(name="test", description="text"))
    project = random.choice(old_list)
    app.project.delete_project(project)
    new_list = app.project.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list) == sorted(new_list)
