# -*- coding: utf-8 -*-
import requests
import datetime

GIT_API_URL = 'https://api.github.com/search/repositories'
TOP_REP_SIZE = 20
NUMBER_OF_DAYS = 7


def string_date_num_days_ago(num_days):
    delta = datetime.timedelta(days=num_days)
    date = datetime.datetime.now() - delta
    return date.strftime('%Y-%m-%d')


def get_trending_repositories(top_size, api_url, num_days):
    request_params = {
        'q': '{}{}'.format('created:>=', string_date_num_days_ago(num_days)),
        'sort': 'stars',
        'order': 'desc'
    }
    trending_repositories_data = requests.get(api_url, params=request_params).json()
    return trending_repositories_data['items'][:top_size]


def print_trending_repositories(trending_repositories_data):
    print(u'Наиболее популярные репозитории за последние {} дней:'.format(NUMBER_OF_DAYS))
    for repository in trending_repositories_data:
        print(u'Репозиторий {}:\nСсылка на репозиторий:{}; Количество звезд:{}; Количество открытых задач:{}'.format(
            repository['name'], repository['html_url'], repository['stargazers_count'],
            repository['open_issues_count']))


if __name__ == '__main__':
    trending_repositories_data = get_trending_repositories(TOP_REP_SIZE, GIT_API_URL, NUMBER_OF_DAYS)
    print_trending_repositories(trending_repositories_data)
