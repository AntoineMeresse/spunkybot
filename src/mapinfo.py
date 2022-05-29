import json

def load_maps():
    with open('src/maplist.json') as f:
        data = json.load(f)
        return data

def maps_from_mapper(mapper):
    maplist = load_maps()
    maps = list()
    for m in maplist:
        if mapper.lower().strip() in m['mapper'].lower().strip():
            maps.append(m['file'])
    return maps

def map_infos(mapname):
    maplist = load_maps()
    res = list()
    if (mapname != ""):
        for m in maplist:
            if mapname.lower().strip() in m['file'].lower().strip():
                res.append(m)
    return res