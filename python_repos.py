import requests

# созданиие вызова API и сохранение ответа

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


# сохранение ответа API в переменной
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

#анализ инфоррмации о репозиториях
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
# API GitHub возвращает подробную информацию о каждом репозитории: в repo_
# dict 73 ключа. Просмотр ключей дает представление о том, какую информацию
# можно извлечь о проекте. (Чтобы узнать, какую информацию можно получить
# через API, следует либо прочитать документацию, либо проанализировать инфор-
# мацию в коде, как мы и поступаем.)