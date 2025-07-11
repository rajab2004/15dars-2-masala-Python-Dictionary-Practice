from data import randomuser_data
from randomusers import (
    get_full_names,
    get_users_by_country,
    count_users_by_gender,
    get_emails_of_older_than,
    sort_users_by_age,
    get_usernames_starting_with,
    get_average_age,
    get_all_coordinates,
    get_oldest_user,
    find_users_in_timezone,
    get_registered_before_year
)

def run_functions() -> None:
    print(" Full Names:")
    print(get_full_names(randomuser_data))

    print("\n Users from Netherlands:")
    print(get_users_by_country(randomuser_data, "Netherlands"))

    print("\n Gender Count:")
    print(count_users_by_gender(randomuser_data))

    print("\n Emails of users older than 60:")
    print(get_emails_of_older_than(randomuser_data, 60))

    print("\n Sorted users by age (descending):")
    print(sort_users_by_age(randomuser_data, descending=True))

    print("\n Usernames starting with 'g':")
    print(get_usernames_starting_with(randomuser_data, "g"))

    print("\n Average age:")
    print(get_average_age(randomuser_data))

    print("\n All coordinates:")
    print(get_all_coordinates(randomuser_data))

    print("\n Oldest user:")
    print(get_oldest_user(randomuser_data))

    print("\n Users in timezone +5:30:")
    print(find_users_in_timezone(randomuser_data, "+5:30"))

    print("\n Registered before 2010:")
    print(get_registered_before_year(randomuser_data, 2010))

run_functions()
