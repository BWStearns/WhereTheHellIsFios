from requests import Session
import json

class VerizonData(object):

    def __init__(self, json_file_name=None):
        json_data = self.get_all_available_city_data()

        self.regions = {}
        self.locations = {}
        self._raw = {}

        self.json_file_name = json_file_name or ".preserved_fios_data.json"
        try:
            self._load()
        except :
            self._raw = self.get_all_available_city_data()
            self
            self._save()

    def _save(self):
        json_file = file(self.json_file_name, "w")
        json_file.write(json.dumps(self._raw))
        json_file.close()

    def _load(self):
        json_file = open(self.json_file_name)
        self._raw = json.loads(json_file.read())
        make_loc_objects()
        

    def make_loc_objects(self):
        for addr, l in self._raw.items():
            r = self.regions.get(l["region"], None)
            if not self.regions.get(r, None):
                r  = Region(l["region"])
                self.regions[l["region"]] = r
                print "Making region {0}".format(r.name)
            loc = Location(l["a"], l["lat"], l["lng"], l["n"], r)
            self.locations[loc.address] = loc
            r.served_addresses[loc.address] = loc

    def get_all_available_city_data(self):

        s = Session()
        req_dest = lambda city: "http://musthavefios.verizon.com/scripts/data/fios_geo_data_compact_{0}.js".format(city)

        fios_cities = ["albany", "baltimore", "boston", "buffalo", "centralpa", "dallas", "dc", "harrisburg", "la", "nyc", "palmsprings", "philly", "pittsburgh", "providence", "richmond", "southva", "sussex", "syracuse", "tampa"]

        # clearly having some fun here.
        alllll_the_cities = {}

        for c in fios_cities:
            print "Collecting {0} data now!".format(c)
            res_json = s.get(req_dest(c))
            if res_json.ok:
                try:
                    res_json = res_json.json()["locations"]
                    for l in res_json:
                        l["region"] = c
                        alllll_the_cities[l["a"]] = l
                except Exception, e:
                    print "ERROR: {0}".format(e)
        return alllll_the_cities


class Region(object):
    def __init__(self, name):
        self.name = name
        self.served_addresses = {}
    

class Location(object):
    def __init__(self, address, lat, lon, name, region=None):
        self.address = address
        self.lat = lat
        self.lon = lon
        self.name = name
        self.region = region
        if self.region:
            self.region.served_addresses[self.address] = self

    def __repr__(self):
        return unicode(self.name)
