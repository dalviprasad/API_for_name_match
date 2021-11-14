# Import Packages
import requests

# localhost and the defined port + endpoint
url = 'http://127.0.0.1:1080/get_match_perc'

# Test it with different strings
body = {
    "first_string": 'Dalvi Prasad',
    "second_string": 'Prasad Dalvi'
}

# Get Match percentage between two strings
response = requests.post(url, data=body)
response.json()