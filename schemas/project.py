# def serializeDict(item)->dict:
#     return {
#         "id":str(item['_id']),
#         "name":item['name'],
#         "description":item['description'],
#         "owner_id":item['owner_id'],
#         "internal_temp":item['internal_temp'],
#         "external_temp":item['external_temp'],
#         "internal_humidity":item['internal_humidity'],
#         "external_humidity":item['external_humidity'],
#         "roof_temp":item['roof_temp'],
#         "roof_humidity":item['roof_humidity'],
#         "exhaust_state":item['exhaust_state'],
#         "sprinkeler_state":item['sprinkeler_state']
#     }

# def serializeList(entity)->list:
#     return [serializeDict(item) for item in entity]

def serializeDict(a)->dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity)->list:
    return [serializeDict(a) for a in entity]