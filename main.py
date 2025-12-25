#   -   -   -   -   -   -   -   -   #
from src.app import app
import src.views as _
from src.config import APP_CONFIG
from src.decorators.blueprint import BLUEPRINTS
#   -   -   -   -   -   -   -   -   #
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)
#   -   -   -   -   -   -   -   -   #
if __name__ == '__main__':    
    app.run(**APP_CONFIG)
#   -   -   -   -   -   -   -   -   #