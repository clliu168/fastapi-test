from fastapi import FastAPI

app = FastAPI()

point2Risk = {
    24: 0.9993,
    23: 0.9990,
    22: 0.9985,
    21: 0.9979,
    20: 0.9970,
    19: 0.9957,
    18: 0.9938,
    17: 0.9912,
    16: 0.9874,
    15: 0.9820,
    14: 0.9743,
    13: 0.9635,
    12: 0.9484,
    11: 0.9275,
    10: 0.8990,
    9: 0.8610,
    8: 0.8118,
    7: 0.7502,
    6: 0.6764,
    5: 0.5927,
    4: 0.5032,
    3: 0.4136,
    2: 0.3293,
    1: 0.2547,
    0: 0.1922,
    -1: 0.1421,
    -2: 0.1034,
}


@app.get("/")
async def root():
    return {"service": "CAAKI API"}


@app.get("/CAAKI")
async def CAAKI(
    scr: float,
    egfr: float,
    bun: float,
    ca: float,
    age: int,
    ckd: int,
    p: float,
    drug: int,
    dm: int,
    sld: int,
):
    points = 0

    if scr <= 0.68:
        points += 0
    elif 0.68 < scr <= 0.88:
        points += 0
    elif 0.88 < scr <= 1.16:
        points += 1
    else:
        points += 7

    if egfr <= 57.8:
        points += 0
    elif 57.8 < egfr <= 80.3:
        points += 2
    elif 80.3 < egfr <= 102:
        points += 3
    else:
        points += 5

    if bun <= 14.8:
        points += 0
    elif 14.8 < bun <= 16.2:
        points += 0
    else:
        points += 1

    if ca <= 8.85:
        points += 0
    elif 8.85 < ca <= 8.9:
        points += -1
    else:
        points += -2

    if age <= 50:
        points += 0
    elif 50 < age <= 62:
        points += 1
    elif 62 < age <= 74:
        points += 2
    else:
        points += 3

    if ckd == 0:
        points += 0
    else:
        points += 2

    if p <= 3.5:
        points += 0
    elif 3.5 < p <= 3.77:
        points += 1
    else:
        points += 1

    if drug == 0:
        points += 0
    else:
        points += 1

    if dm == 0:
        points += 0
    else:
        points += 1

    if sld == 0:
        points += 0
    else:
        points += 3

    risk_prob = point2Risk[points]

    return {"score": points, "risk_prob": risk_prob}
