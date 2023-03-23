""": Start with a copy of user_profile.py from page 153. Build 
a profile of yourself by calling build_profile(), using your first and last names 
and three other key-value pairs that describe you."""


def user_profile(firt, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = firt
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

profile = user_profile("ali", "nawab khan", location="wah cantt", field="Software Engineering", age="21")
print(profile)