def get_location_name(city_name, country_name, population=''):
    city_country = f"{city_name}, {country_name} - population {population}"
    return city_country.title()