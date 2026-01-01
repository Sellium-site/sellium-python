from sellium import SelliumClient, APIError

BASE_URL = "https://sellium.site/api/v1"

with SelliumClient("API_KEY", "STORE_ID", base_url=BASE_URL) as client:
    try:
        data, meta = client.products.list(page=1, limit=20)
        print("Products:", len(data["data"]["products"]))
        if meta.rate_limit:
            print("Rate remaining:", meta.rate_limit.remaining)
    except APIError as e:
        print("API Error:", e)
