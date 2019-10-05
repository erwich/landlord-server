from config import config
import json
import flask

# Import all api modules and their routes
from api.accounts import accounts 

#Initialize Flask
app = flask.Flask(config['web_server']['flask_app_name'])

# Attach API routes to flask webservice
def init_routes(app, blueprints):
    for namespace, blueprint in blueprints:
        app.register_blueprint(
            blueprint,
            url_prefix="{}/{}".format(
                config["web_server"]["url_prefix"],
                namespace
            )
        )
        print("Loaded {}".format(namespace))

init_routes(
    app, [
        ("accounts", accounts)
    ]
)

print("Dumping valid URL paths")
print( app.url_map )

if __name__ == '__main__':
    app.logger.info('API Starting')
    app.run(host=config['web_server']['host'], port=config['web_server']['port'], debug=config['web_server']['debug'])
