"""generate api call"""


def generate_api_call(user_query: str):
    """this function generates api call based on user query"""
    return "get_prod_var('Desk3', 'May 13 2024')"


def return_data_from_api_call(api_call: str):
    """this function returns data from api call"""
    return eval(api_call)


def get_prod_var(desk: str, date: str):
    """Sample API function, it returns VaR of a desk on a given date"""
    return 0.5


if __name__ == '__main__':
    user_query = "Find VaR of Desk 3 for May 13 2024"
    generated_api_call = generate_api_call(user_query)
    print(generated_api_call)
    returned_data = return_data_from_api_call(generated_api_call)
    print(returned_data)
