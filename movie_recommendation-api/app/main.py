import datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title = "Movie Recommendation API",
    description = "An API to recommend movies based on user preferences",
    version = "1.0.0",
    contact = { 
           "name": "Basan-ta",
           "email": "basanta.shrestha077@gmail.com"
            },
    license_info = {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
)


#health check endpoint
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Movie Recommendation API!"}

if __name__ == "__main__":
    impport uvicorn 
    uvicorn.run(app, host="0.0.0", port=8000)
    