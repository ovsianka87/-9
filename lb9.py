from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'
db = SQLAlchemy(app)

@app.route('/create_db', methods=['POST'])
def create_db():
    db_name = request.json['db_name']
    # Логика создания базы данных
    return jsonify({'message': 'Database created'})

@app.route('/execute_query', methods=['POST'])
def execute_query():
    query = request.json['query']
    # Логика выполнения запроса
    return jsonify({'result': 'Query executed'})

if __name__ == '__main__':
    app.run(debug=True)
