scart =[
    {"name":"Alice","age":20,"total_purchase":150},
    {"name":"Bob","age":50,"total_purchase":130},
    {"name":"charlie","age":35,"total_purchase":225}
]

updated_price= lambda scart: {
    "name": scart["name"],"age":scart["age"], "total_purchase": round(
        scart["total_purchase"] * 0.90 if 18 <= scart["age"] <= 25 else
        scart["total_purchase"] * 0.95 if 26 <= scart["age"] <= 40 else
        scart["total_purchase"], 2)
}

updated_shopping_price=list(map(updated_price,scart))

print(updated_shopping_price)