football = {"Abu", "Daniyar", "Zhanarys", "Zhasik"}
basketball = {"Nurtas", "Rustam", "Daulet", "Daniyar"}

res = len(football.intersection(basketball))
names = football.intersection(basketball)

print(f"Number of people who like both sports: {res} {names}")

