from web import app
from database.mysql import client

# Initialize the database connection
client.init()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)