from app import create_app, db

# Cria a aplicação Flask
app = create_app()

with app.app_context():
    db.create_all() 

if __name__ == '__main__':
    app.run(debug=True)
