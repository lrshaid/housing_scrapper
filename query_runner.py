import sqlite3

conn = sqlite3.connect('properties.db')

# Check to see if we know it
stmt = 'DELETE FROM properties'#WHERE internal_id=:internal_id AND provider=:provider
with conn:
    #for prop in provider.next_prop():
    cur = conn.cursor()
    #logging.info(f"Processing property {prop['internal_id']}")
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    print(result)