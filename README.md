Ce projet est une application Django multilingue avec intégration de chatbot utilisant un modèle de langage (GPT) et une fonctionnalité de recherche augmentée par intelligence artificielle (RAG).


Installez les dépendances Python à l'aide de pip :

pip install -r requirements.txt

Créez un fichier `.env` à la racine du projet avec les clés API et autres configurations sensibles :

SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_api_key

Appliquez les migrations pour créer les tables de la base de données :

python manage.py migrate

Maintenant que l'installation est terminée, vous pouvez utiliser le projet en lançant le serveur de développement :

python manage.py runserver

Assurez-vous de visiter `http://localhost:8000` dans votre navigateur pour voir l'application en action.
