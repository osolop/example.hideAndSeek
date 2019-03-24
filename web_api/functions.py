def get_locations(map_json, exclude=None):
    locations = list(map_json.keys())
    if exclude:
        for location in exclude:
            locations.remove(location)
    return ', '.join(locations)


def description(map_json, location):
    if location in map_json:
        items = ', '.join(map_json[location])
        msg = f'There are such items in the {location}: {items}.'
    else:
        msg = f'There is no location like {location}. Use map.'
    return {'description': msg}
