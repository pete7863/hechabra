from web import app
from database.mysql import client

# Initialize the database connection
client.init()

if __name__ == '__main__':
    app.run(debug=True)