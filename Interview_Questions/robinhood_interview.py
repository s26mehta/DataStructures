"""
For a given service_list find the load for each dependency given an entrypoint

service_list = [
    "logging=", 
    "user=logging", 
    "orders=user|foobar", 
    "recommendations=user|orders", 
    "dashboard=user|orders|recommendations"
]
entrypoint = "dashboard"

Output should be map of list -> load
             orders
           />  ^  \
          /    |    \>
dashboard -----|---> user ---> logging
         \     |     />      
          \>   |    /
           Recommendations

"""

def get_load_map(service_list, entrypoint):

    service_list_map = {}

    for item in service_list:
        item_split = item.split("=")
        service = item_split[0]
        dependencies = item_split[1].split("|")
        service_list_map[service] = dependencies

    service_parent_map = {}

    for service, dependencies in service_list_map.items():
        for dependency in dependencies:
            if dependency in service_list_map:
                if dependency not in service_parent_map:
                    service_parent_map[dependency] = [[], None]
                service_parent_map[dependency][0].append(service)

    service_parent_map[entrypoint] = [[],1]

    for service, value in service_parent_map.items():
        if value[1] == None:
            compute_load(service_parent_map, service)
        
    result = {}
    for service, value in service_parent_map.items():
        result[service] = value[1]
    return result

def compute_load(service_parent_map, node):
    total_load = 0

    for parent in service_parent_map[node][0]:
        if service_parent_map[parent][1] == None:
            compute_load(service_parent_map, parent)
        total_load += service_parent_map[parent][1]
    
    service_parent_map[node][1] = total_load

service_list = [
    "logging=", 
    "user=logging", 
    "orders=user|foobar", 
    "recommendations=user|orders", 
    "dashboard=user|orders|recommendations"
]
entrypoint = "dashboard"

print(get_load_map(service_list, entrypoint))
    


