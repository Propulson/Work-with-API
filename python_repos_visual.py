import requests
from plotly import offline
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
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# create visual
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars
}]
my_layout = {
    'title': 'GitHub Repositories',
    'xaxis': {'title': 'Repository Name'},
    'yaxis': {'title': 'Stars'}
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python-repos-chart.html')


