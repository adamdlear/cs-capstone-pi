from sql_connector import SQLConnection


def send_data():
    conn = SQLConnection()
    conn = conn.get_connection()
    cursor = conn.cursor()
    # Query to retrieve existing PotholeIDs
    query = "SELECT PotholeID FROM Potholes.PotholeLocation"
    cursor.execute(query)
    existing_ids = cursor.fetchall()
    used_ids = set(id[0] for id in existing_ids if id[0] is not None)

    # Find the minimum available PotholeID starting from 1
    pothole_id = 1
    while pothole_id in used_ids:
        pothole_id += 1

    coordinates = ... #get_coords
    latitude = 41.541409
    longitude = -90.365754

    # Insert the new pothole record into the database
    insert_query = """INSERT INTO Potholes.PotholeLocation (PotholeID, Latitude, Longitude) VALUES (?, ?, ?)"""
    cursor.execute(insert_query, (pothole_id, latitude, longitude))
    conn.commit()
    cursor.close()
    return "Entry added successfully"
