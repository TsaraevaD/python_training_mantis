from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.project_cache = None

    def fill_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").c
        lear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def open_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def delete_project(self, name):
        wd = self.app.wd
        self.open_project()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None


    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("tr.row-1, tr.row-2"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)


