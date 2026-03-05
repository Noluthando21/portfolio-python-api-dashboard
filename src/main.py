import requests

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def fetch_bitcoin_price():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        usd_price = data["bpi"]["USD"]["rate"]
        updated_time = data["time"]["updated"]

        print("\nBitcoin Price Dashboard")
        print("-----------------------")
        print(f"Updated: {updated_time}")
        print(f"BTC Price (USD): {usd_price}")

    except requests.exceptions.RequestException as e:
        print("\nBitcoin Price Dashboard")
        print("-----------------------")
        print("Could not reach the API (network/DNS issue).")
        print(f"Error: {e}")


def main():
    fetch_bitcoin_price()


if __name__ == "__main__":
    main()