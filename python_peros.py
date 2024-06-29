import requests

# create api search

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# save response
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# analyze info about repo
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

print(f'\nSelected information about each repository:')
for repo_dict in repo_dicts:
    # analyze first repo
    print(f'\nName: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repositories: {repo_dict["html_url"]}')
    print(f'Description: {repo_dict["description"]}')


