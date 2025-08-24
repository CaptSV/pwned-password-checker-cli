import requests
import hashlib
import sys

# request pwnedpassword api data with our 5 char hashed password
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res

def get_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

# hashes password and splits hash to check against pwnedpassword api
# retrieves leaked count of passwords
def pwned_api_check(password_from_main):
    sha1password = hashlib.sha1(password_from_main.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    api_res = request_api_data(first5_char)
    return get_leak_count(api_res, tail)

# main fn to input password to check and display results

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.')
        else:
            print(f'{password} was NOT found.')
    return "FINISHED"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))