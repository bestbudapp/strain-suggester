# Imports
from dotenv import load_dotenv
from flask import Flask, request
from .predict import suggest_strains

# Initialize .env file
load_dotenv()

# Insert debugger for development debugging
# import pdb; pdb.set_trace()


def create_app():
    """Create and configure instances of the Flask suggester app."""
    app = Flask(__name__)

    @app.route('/')
    def root():
        """ Generate text for landing page just for fun. """
        return '<h2>API Landing Page.</h2>'

    @app.route('/suggest', methods=['POST'])
    def suggest():
        """
        Generate strain suggestion from user input.
        Output JSON with 5 strain suggestions.
        """
        input = request.get_json(force=True)
        suggestion = suggest_strains(input)[0]
        return str(suggestion)

# Deprecated format to convert to JSON
        # return jsonify(
        #     strain1=str(suggestion[0][0]),
        #     strain2=str(suggestion[0][1]),
        #     strain3=str(suggestion[0][2]),
        #     strain4=str(suggestion[0][3]),
        #     strain5=str(suggestion[0][4])
        #     )

    @app.route('/test')
    def test():
        """ Generate test page for baseline API tests. """
        return '<h1>Success!</h1>'

    return app
