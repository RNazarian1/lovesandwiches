import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data)
# print("\n\tHello")

# def get_sales_data():
#     """
#     Get sales figures input from the user.
#     """
#     print("Please enter sales data from the last market.")
#     print("Data should be six numbers, separated by commas.")
#     print("Example: 10,20,30,40,50,60\n")

#     data_str = input("Enter your data here: ")
#     print(f"The data provided is {data_str}")

# get_sales_data()


def get_sales_data():
    """
    Get sales figures input from the user.
 
    """

    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")
    validate_data(sales_data)
    return sales_data
    
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:

        print(values)
        [int(value) for value in values]
        print(values)
        if len(values) != 6:
            raise ValueError(
                f"\nExactly 6 values required, \n\tyou provided {len(values)} \n\t\t \
                         or \n\t\t\tthere is no (,) between the values")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        get_sales_data()
    print("Input is valid")
    
data = get_sales_data()
sales_data = [int(num) for num in data]
print(sales_data)
# sales_data = [int(num) for num in data]
