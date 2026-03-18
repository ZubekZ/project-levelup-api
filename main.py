from fastapi import FastAPI

app = FastAPI(title="Project LevelUp API")

@app.get("/")
def read_root():
    return {"status": "Mestre de RPG online e aguardando jogadores!"}