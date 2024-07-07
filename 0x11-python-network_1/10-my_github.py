#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.

FUNCTIONALITY

1.import the required packages, requests and sys.

2. get the username and password (personal access token)
    from the command line arguments using the sys module.

3. set up the API endpoint URL to retrieve the user information.

4. set up the Basic Authentication header with the provided
    credentials using the base64 encoding.

5. make the API call using the requests.get method and
    passing the URL and headers as parameters.

6. check the response status code to ensure that the
    API call was successful.

7.  API call was successful, we display the user id by
    accessing the 'id' key of the JSON response.

8.  API call was not successful, we display the error status code.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
