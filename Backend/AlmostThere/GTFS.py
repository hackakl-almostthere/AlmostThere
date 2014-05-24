from APIConnection import makeConnection

def gtfs_query(query):
    return makeConnection('gtfs/' + query)