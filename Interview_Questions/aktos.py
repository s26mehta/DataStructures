import csv
import json

consumers_data = {}
previous_jobs_count_map = {}
status_map = {}

class Consumer:
    def __init__(self, id, street, status, previous_jobs_count, amount_due, lat, long):
        self.id = id
        self.street = street
        self.status = status
        self.previous_jobs_count = previous_jobs_count
        self.amount_due = amount_due
        self.lat = lat
        self.long = long

class Properties:
    def __init__(self, id, amount_due, previous_jobs_count, status, street):
        self.id = id
        self.amount_due = amount_due
        self.previous_jobs_count = previous_jobs_count
        self.status = status
        self.street = street
    
    def create_json(self):
        self.__dict__

class Point:
    def __init__(self, coordinates):
        self.type = "Point"
        self.coordinates = coordinates

    def create_json(self):
        self.__dict__

class Feature:
    def __init__(self, geometry, properties):
        self.type = "Feature"
        self.geometry = geometry
        self.properties = properties

    def create_json(self):
        self.__dict__

class GeoJson:
    def __init__(self, features):
        self.type = "FeatureCollection"
        self.features = features

    def create_json(self):
        self.__dict__

class JsonConverter(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

with open('./consumers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        consumers_data[row['id']] = Consumer(
            row['id'],
            row['street'],
            row['status'],
            row['previous_jobs_count'],
            row['amount_due'],
            row['lat'],
            row['lng']
        )
        if row['previous_jobs_count'] not in previous_jobs_count_map:
            previous_jobs_count_map[row['previous_jobs_count']] = set()
        previous_jobs_count_map[row['previous_jobs_count']].add(row['id'])
        if row['status'] not in status_map:
            status_map[row['status']] = set()
        status_map[row['status']].add(row['id'])



def get_consumers(min_previous_jobs_count = 0, max_previous_jobs_count = float('inf'), status = None):
    result_ids = set()
    for prev_job_count, consumer_ids in previous_jobs_count_map.items():
        if int(prev_job_count) >= min_previous_jobs_count and int(prev_job_count) <= max_previous_jobs_count:
            result_ids = result_ids.union(consumer_ids)
    if status != None:
        result_ids = result_ids.intersection(status_map[status])
    
    features = []
    for id in result_ids:
        id_data = consumers_data[id]
        features.append(
            Feature(
                geometry = Point(
                    coordinates = [id_data.lat, id_data.long]
                ),
                properties = Properties(
                    id = id_data.id,
                    amount_due = id_data.amount_due,
                    previous_jobs_count = id_data.previous_jobs_count,
                    status = id_data.status,
                    street = id_data.street
                )
            )
        )
    geo_json = GeoJson(features)

    return json.dumps(geo_json, cls=JsonConverter)

print(get_consumers(1,1, 'collected'))