import requests

BTC_API = "https://api.coinbase.com/v2/prices/spot?currency=USD"
TIME_API = "http://worldtimeapi.org/api/timezone/Etc/UTC"


def fetch_data():
    try:
        btc_res = requests.get(BTC_API, timeout=10)
        time_res = requests.get(TIME_API, timeout=10)

        btc_res.raise_for_status()
        time_res.raise_for_status()

        btc_data = btc_res.json()
        time_data = time_res.json()

        btc_price = btc_data["data"]["amount"]
        current_time = time_data["datetime"]

        print("\n=== API DASHBOARD ===")
        print("----------------------")
        print(f"Time (UTC): {current_time}")
        print(f"Bitcoin Price (USD): {btc_price}")

    except requests.exceptions.RequestException as e:
        print("\n=== API DASHBOARD ===")
        print("----------------------")
        print("Network/API error occurred")
        print(f"Error: {e}")


def main():
    fetch_data()


if __name__ == "__main__":
    main()