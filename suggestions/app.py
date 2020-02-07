# Imports
from dotenv import load_dotenv
from flask import Flask, request
from .predict import Suggester

# Initialize .env file
load_dotenv()

# Insert debugger for optional development debugging
# import pdb; pdb.set_trace()


def create_app():
    """Create and configure instances of the Flask suggester app."""
    app = Flask(__name__)

    @app.route('/')
    def root():
        """ Generate text for landing page. """
        return '<h2>API Landing Page.</h2>'

    @app.route('/suggest', methods=['POST'])
    def suggest():
        """
        Generate strain suggestion from user input as JSON.
        Output space-separated string with 5 strain suggestions.
        """
        input = request.get_json(force=True)
        suggester = Suggester()
        suggestion = suggester.strain_suggester(input["input"])
        string_suggestion = " ".join(str(i) for i in suggestion)

        return string_suggestion

    @app.route('/test')
    def test():
        """ Generate test page for baseline API tests. """
        return '<h1>Success!</h1>'

    return app
