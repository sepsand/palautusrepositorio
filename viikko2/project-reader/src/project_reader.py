from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # muunna merkkijono tietorakenteeksi
        parsed_content = toml.loads(content)
        #print(parsed_content)

        # poimi tiedot
        projectName = parsed_content["tool"]["poetry"]["name"]
        projectDesc = parsed_content["tool"]["poetry"]["description"]
        projectLicense = parsed_content["tool"]["poetry"]["license"]
        authors = parsed_content["tool"]["poetry"]["authors"]
        dependencies = list(parsed_content["tool"]["poetry"]["dependencies"].keys())
        devDependencies = list(parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(projectName, projectDesc, projectLicense, authors, dependencies, devDependencies)
