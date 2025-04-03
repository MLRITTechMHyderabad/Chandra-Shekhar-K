emp=[
    {"name":"Alice","salary":50000,"rating":5},
    {"name":"Bob","salary":40000,"rating":3},
    {"name":"charlie","salary":35000,"rating":2}
]

updated_sal= lambda emp: {
    "name": emp["name"],
    "salary": round(emp["salary"] * 1.10, 2) if emp["rating"] >= 4 else
              round(emp["salary"] * 1.05, 2) if emp["rating"] == 3 else
              round(emp["salary"] * 0.97, 2),
    "rating": emp["rating"]
}

updated_emp=list(map(updated_sal,emp))

print(updated_emp)