from TFS.tfs import  TFS
from pprint import pprint
def main():
    program = TFS('gdfwj4xwjqgvehxx3woomf7b54lvqjiuyfttj2vtq2pbsr2k77wq',
                  'https://tfs.es.gov.br/tfs/DefaultCollection/')
    
    projects = program.get_projects()
    for project in projects:
        pprint (project.__dict__)
    
    teams = program.get_all_team_project_organization()
    for team in teams:
        for t in team:
            pprint (t.__dict__)
    
    team_members = program.get_all_team_members_project()

if __name__ == "__main__":
    main()
