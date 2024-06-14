import uvicorn

from .app import app

def run():
    config = uvicorn.Config(app, host='0.0.0.0', port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()