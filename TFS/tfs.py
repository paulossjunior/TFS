from vsts.vss_connection import VssConnection
from msrest.authentication import BasicAuthentication
from pprint import pprint

class ProjectDTO(object):

    def __init__(self, project_id, teams):
        self.project_id = project_id
        self.teams = teams

class TFS(object):

    def __init__(self, personal_access_token, organization_url):

        # Create a connection to the org
        self.credentials = BasicAuthentication('', personal_access_token)
        self.connection = VssConnection(base_url=organization_url, creds=self.credentials)


    def get_projects(self):
        # Get a client (the "core" client provides access to projects, teams, etc)
        core_client = self.connection.get_client('vsts.core.v4_0.core_client.CoreClient')

        # Get the list of projects in the org
        projects = core_client.get_projects()
        return projects
    
    def get_all_team_project_organization(self):
        core_client = self.connection.get_client('vsts.core.v4_0.core_client.CoreClient')
        projects = core_client.get_projects()
        
        all_projects_teams = []

        for project in projects:
            teams = core_client.get_teams(project.id)
            project_DTO = ProjectDTO(project.id, teams)
            all_projects_teams.append (project_DTO)     
        
        return all_projects_teams
    
    def get_all_team_members_project(self):
        core_client = self.connection.get_client('vsts.core.v4_0.core_client.CoreClient')
        projects = core_client.get_projects()
        
        all_team_members = []

        # Show details about each project in the console
        for project in projects:
            teams = core_client.get_teams(project.id)
            for team in teams:
                team_members = core_client.get_team_members(project.id,team.id)
                for team_member in team_members:
                    team_member.additional_properties["team"] = team.id
                    all_team_members.append(team_member)
        return all_team_members
