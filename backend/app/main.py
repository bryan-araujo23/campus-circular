from fastapi import FastAPI       # importa a classe principal do framework.


app = FastAPI(
    title="Campus Circular API",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}  
