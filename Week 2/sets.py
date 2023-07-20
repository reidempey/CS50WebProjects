def main():
    # Create an empty set
    s = set()

    # Add elements to set
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(3)

    s.remove(2)
    print(s)

    print(f"Length of set: {len(s)}")



if __name__ == "__main__":
    main()