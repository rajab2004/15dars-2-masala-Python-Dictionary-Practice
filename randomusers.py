def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    results = randomuser_data['results']
    names = []
    for user in results:
        name = user['name']
        full_name = name['first']+" "+ name['last']
        names.append(full_name)
    return names
def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    natija = []
    for user in data.get("results", []):
        if user.get("location", {}).get("country") == country:
            ism = user['name']['first']
            familiya = user['name']['last']
            email = user['email']
            natija.append({
                "name": f"{ism} {familiya}",
                "email": email
            })
    return natija

def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    natija = {}

    for user in data.get("results", []):
        jins = user.get("gender")
        if jins in natija:
            natija[jins] += 1
        else:
            natija[jins] = 1

    return natija

def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    natija = []

    for user in data.get("results", []):
        user_age = user.get("dob", {}).get("age", 0)
        if user_age > age:
            natija.append(user.get("email"))

    return natija

def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    users = data.get("results", [])

    user_list = []
    for user in users:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        age = user.get("dob", {}).get("age", 0)
        user_list.append({"name": full_name, "age": age})

    user_list.sort(key=lambda x: x['age'], reverse=descending)

    return user_list

def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    natija = []

    for user in data.get("results", []):
        username = user.get("login", {}).get("username", "")
        if username.startswith(letter):
            natija.append(username)

    return natija


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    foydalanuvchilar = data.get("results", [])
    jami_yosh = 0
    soni = 0

    for user in foydalanuvchilar:
        yosh = user.get("dob", {}).get("age", 0)
        jami_yosh += yosh
        soni += 1

    if soni == 0:
        return 0.0  

    return jami_yosh / soni

def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    natija = {}

    for user in data.get("results", []):
        millat = user.get("nat", "Unknown")
        if millat in natija:
            natija[millat] += 1
        else:
            natija[millat] = 1

    return natija


def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    koordinatalar = []

    for user in data.get("results", []):
        lat = user.get("location", {}).get("coordinates", {}).get("latitude", "")
        lon = user.get("location", {}).get("coordinates", {}).get("longitude", "")
        koordinatalar.append((lat, lon))

    return koordinatalar

def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    users = data.get("results", [])
    
    if not users:
        return {}

    eng_katta = max(users, key=lambda user: user.get("dob", {}).get("age", 0))

    full_name = f"{eng_katta['name']['first']} {eng_katta['name']['last']}"
    age = eng_katta['dob']['age']
    email = eng_katta['email']

    keys = ["name", "age", "email"]
    values = [full_name, age, email]
    return dict(zip(keys, values))


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    natija = []

    for user in data.get("results", []):
        zona = user.get("location", {}).get("timezone", {}).get("offset", "")
        if zona == offset:
            ism = f"{user['name']['first']} {user['name']['last']}"
            shahar = user.get("location", {}).get("city", "")
            natija.append({"name": ism, "city": shahar})

    return natija

def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    natija = []

    for user in data.get("results", []):
        sana = user.get("registered", {}).get("date", "")
        if sana:
            yil = int(sana[:4]) 
            if yil < year:
                ism = f"{user['name']['first']} {user['name']['last']}"
                ro_yxat_sana = sana.split("T")[0]  
                natija.append({"name": ism, "registered": ro_yxat_sana})

    return natija

def get_full_names(data: dict) -> list[str]:
    return [
        f"{user['name']['first']} {user['name']['last']}"
        for user in data.get("results", [])
    ]

def get_users_by_country(data: dict, country: str) -> list[dict]:
    return [
        {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user["email"]
        }
        for user in data.get("results", [])
        if user.get("location", {}).get("country") == country
    ]
