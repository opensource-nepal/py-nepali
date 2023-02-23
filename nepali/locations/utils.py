import re
from functools import partial

from ._locations import provinces, districts, municipalities


__all__ = [
    "get_province",
    "get_district",
    "get_municipality",
]


def _filter_location(
    *, locations, name=None, name_nepali=None, exact=False, multiple=False
):
    if not name and not name_nepali:
        raise ValueError("name or name_nepali must be passed")

    if exact and multiple:
        raise ValueError("Both the exact and multiple cannot be true")

    # making name as lower case
    if name:
        name = name.lower()

    # taking field and value for filtering
    # eg. field = name and value ="Bagmati Province"
    field, value = ("name", name) if name else ("name_nepali", name_nepali)

    # filtering data
    if exact:
        filtered_locations = [
            location
            for location in locations
            if getattr(location, field).lower() == value
        ]
    else:
        pattern = re.compile(rf".*{value}.*")
        filtered_locations = [
            location
            for location in locations
            if re.match(pattern, getattr(location, field).lower())
        ]

    # returning data if not filtered location is available
    if len(filtered_locations) == 0 and not multiple:
        return None

    return filtered_locations if multiple else filtered_locations[0]


get_province = partial(_filter_location, locations=provinces)
get_district = partial(_filter_location, locations=districts)
get_municipality = partial(_filter_location, locations=municipalities)
