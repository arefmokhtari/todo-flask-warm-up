#   -   -   -   -   -   -   -   -   #
from flask import Blueprint
#   -   -   -   -   -   -   -   -   #
BLUEPRINTS = []
#   -   -   -   -   -   -   -   -   #

def blueprint(name: str,):
    name = name[name.rfind('.')+1:]
    def wrapper(cls):
        blueprint = Blueprint(name.strip('__'), name)
        instance = cls()
        for attr in dir(instance):
            f = getattr(instance, attr)

            if callable(f) and hasattr(f, "_route"):
                blueprint.add_url_rule(
                    f._route,
                    view_func=f,
                    methods=f._methods,)
        BLUEPRINTS.append(blueprint)
        return cls

    return wrapper

#   -   -   -   -   -   -   -   -   #

def route(path, methods: str | list = 'get',):
    if type(methods) is str:
        methods = [ methods, ]
    def wrapper(func):
        func._route = path
        func._methods = map(lambda m: m.upper(), methods)
        return func
    return wrapper

#   -   -   -   -   -   -   -   -   #