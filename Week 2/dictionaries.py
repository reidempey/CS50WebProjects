

def main():
    houses = {"Harry": "Gryffindor", "Draco":"Slytherin"}

    houses["Hermione"] = "Gryffindor"

    print(houses["Harry"])
    for n,h in houses.items():
        print(f"{n}: {h}")


if __name__ == "__main__":
    main()