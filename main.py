import fastapi
import uvicorn
from api import motd
from views import home # New
from starlette.staticfiles import StaticFiles
from environs import Env

main_app = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_env_vars()


def configure_env_vars():
    env = Env()
    env.read_env()
    if not env("ENV_SECRET"):
        print(f"WARNING: environment variable ENV_SECRET not found")
        raise Exception("environment variable ENV_SECRET not found.")
    else:
        home.secret = env("ENV_SECRET")


def configure_routing():
    main_app.mount('/static', StaticFiles(directory='static'), name='static') 
    main_app.include_router(motd.router)
    main_app.include_router(home.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(main_app, host='0.0.0.0', port=8000)
else:
    configure()
