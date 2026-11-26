from fastapi import FastAPI, Query
app = FastAPI(title="Simple Interest API")
@app.get("/")
def home():
    return {"message": "Interest API is running. Developed By : Ankit Patel"}

@app.get("/getInterest")
def getInterest(
    amount: float = Query(..., gt=0),
    rate: float = Query(..., ge=0),
    year: float = Query(..., gt=0)
):
    interest = (amount * rate * year) / 100
    return {
        "amount": amount,
        "rate": rate,
        "year": year,
        "simple_interest": round(interest, 2)
    }
# http://127.0.0.1:8000/getInterest?amount=10000&rate=5&year=2
# https://interest-api-sjxd.onrender.com/getInterest?amount=25000&rate=11&year=5