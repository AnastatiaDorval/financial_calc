import requests

url = 'http://localhost:5001'

def test_get(username):
    data = {
        'user': username
    }

    response = ''
    try:
        response = requests.get('http://localhost:5001/401K/percents', params=data)
        if response.status_code == 201:
            print(f'{username} was found')
            print(response)
        else:
            print(f'{username} was not found')
            print(response)
    except Exception as e:
        print(e)

def test_post(username, before_tax, after_tax, roth):
    data = {
        'user': username,
        'pretax': before_tax,
        'aftertax': after_tax,
        'roth': roth
    }

    response = ''
    try:
        response = requests.post('http://localhost:5001/401K/percents', params=data)
        if response.status_code == 201:
            print(f'{username} was successfully added')
            print(response)
        else:
            print(f'{username} was not added')
            print(response)
    except Exception as e:
        print(e)


def test_delete(username):
    data = {
        'user': username
    }

    response = ''
    try:
        response = requests.delete('http://localhost:5001/401K/percents', params=data)
        if response.status_code == 201:
            print(f'Able to delete {username}')
        else:
            print(f'Unable to delete {username}')
    except Exception as e:
        print(e)

# test_post('Anastatia', '.05', '0', '.15')
# test_get('Anastatia')
# test_delete('Anastatia')