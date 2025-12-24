#   -   -   -   -   -   -   -   -   #
from src.app import app
from src.config import CONFIG
from src.views.runner import blueprint as runner
from src.views.master import blueprint as master
from src.views.index import blueprint as index
#   -   -   -   -   -   -   -   -   #
for blueprint in (runner, master, index):
    app.register_blueprint(blueprint)
#   -   -   -   -   -   -   -   -   #
if __name__ == '__main__':    
    app.run(**CONFIG)
#   -   -   -   -   -   -   -   -   #