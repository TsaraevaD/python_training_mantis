from fixture.project import Project


def test_add_project(app):
    old_list = app.project.get_project_list()
    theme = Project(name="test", description="text")
    app.project.add(theme)
    new_list = app.project.get_project_list()
    assert len(old_list) + 1 == len(new_list)
