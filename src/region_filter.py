import requests

class RegionFilter:
    def __init__(self, region_codes: list):
        self.region_codes = region_codes

    def is_in_region(self, ip: str) -> bool:
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if 'region' in data:
                    return data['region'] in self.region_codes
            return False
        except Exception:
            return False
