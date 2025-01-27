from fastapi import FastAPI
from routes import ops_user, client_user

app = FastAPI()

# Include route files
app.include_router(ops_user.router, prefix="/ops", tags=["Ops User"])
app.include_router(client_user.router, prefix="/client", tags=["Client User"])
