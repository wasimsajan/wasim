from github import Github
import os

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

def extract_PR(project_full_name):
    try:
        current_user = g.get_user()

        repo = g.get_repo(project_full_name)
        PRs_list = repo.get_pulls(state='all')
        subject= "Summary of PR's"
        from_email = "was.sajan@gmail.com"
        to_email = "test@gmail.com"
        print(f'From Email : # {from_email}')
        print(f'Subject : # {subject}')
        print(f'To  Email : # {to_email}')
        print(f"Please find below summary of PR for {project_full_name}")
        for pr in PRs_list:
            print(f'The PR number is {pr.number}')
            print(f'The PR id is {pr.id}')
            print(f'The no of files changed are {pr.changed_files}')
            print(f'The PR title is {pr.title}\n')
    except BadCredentialsException as e:
        print(e.status)
        print('Bad credentials exception')
    except UnknownObjectException as e:
        print(e.status)
        print('Unknown object exception')

    except GithubException as e:
        print(e.status)
        print('General exception')


extract_PR('wasimsajan/devops_training')

