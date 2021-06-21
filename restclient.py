import requests

myToken = 'b0f96b05ba2a148be62416a4cd6ca44d36714f3f'
headers = {'Authorization': 'token {}'.format(myToken)}

def _url(path):
    return 'http://localhost:8000' + path

def get_tasks():
    return requests.get(_url('/api/v1/questions/'))


def describe_task(task_id):
    return requests.get(_url('/api/v1/questions/{:d}'.format(task_id)))

def add_task(question, pub_date):
    return requests.post(_url('/api/v1/questions/'), headers=headers, json={
        'question_text': question,
        'pub_date': pub_date,
        })

def task_done(task_id):
    return requests.delete(_url('/api/v1/questions/{:d}'.format(task_id)),headers=headers)

def update_task(task_id, question, pub_date):
    url = _url('/api/v1/questions/{:d}'.format(task_id))
    return requests.put(url, json={
        'question_text': question,
        'pub_date': pub_date,
        }, headers=headers)

