
def build_common_url(url: str, common_params: dict) -> str:
    url += "?"
    for key, value in common_params.items():
        if value != -1:
            url += f"{key}={value}&"

    return url

def add_specific_params(url: str, specific_params: dict) -> str:
    for key, value in specific_params.items():
        if value != -1:
            url += f"{key}={value.replace(" ", "_")}&"

    return url