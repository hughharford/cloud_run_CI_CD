from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "From the cloud! \n \
            Can I update automatically?: CI/CD"}
