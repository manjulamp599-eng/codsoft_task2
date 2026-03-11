import pandas as pd

print("==============================================")
print("        SMART PRODUCT RECOMMENDATION SYSTEM")
print("==============================================\n")


data = {
    "User": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Laptop": [1, 1, 0, 1, 0],
    "Smartphone": [1, 0, 1, 0, 1],
    "Headphones": [1, 0, 1, 0, 1],
    "Tablet": [0, 1, 0, 0, 1],
    "Smartwatch": [0, 1, 0, 1, 0],
    "Camera": [0, 0, 1, 1, 0],
    "Bluetooth Speaker": [1, 0, 1, 0, 1],
    "Gaming Console": [0, 1, 0, 0, 1],
    "VR Headset": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.set_index("User", inplace=True)


def recommend_products(user):

    if user not in df.index:
        print("System: User not found.\n")
        return

    print("\nSystem: Analyzing preferences for", user)

    user_products = df.loc[user]

    liked = []
    for product in df.columns:
        if user_products[product] == 1:
            liked.append(product)

    print("System: Products you like:")
    for p in liked:
        print("-", p)

    print("\nSystem: Searching for similar users...\n")

    recommendations = {}

    for other_user in df.index:

        if other_user != user:

            other_products = df.loc[other_user]

            similarity = (user_products & other_products).sum()

            if similarity > 0:

                print("Similar user found:", other_user)

                for product in df.columns:

                    if other_products[product] == 1 and user_products[product] == 0:
                        recommendations[product] = recommendations.get(product, 0) + similarity

    print("\nSystem: Generating recommendations...\n")

    sorted_rec = sorted(recommendations, key=recommendations.get, reverse=True)

    if sorted_rec:
        print("Recommended Products:\n")
        for product in sorted_rec:
            print("-", product)
    else:
        print("No recommendations available.")

    print("\n--------------------------------------\n")



while True:

    user_input = input("Enter user name (Alice, Bob, Charlie, David, Eva) or type 'exit': ")

    if user_input.lower() == "exit":
        print("\nSystem: Thank you for using the recommendation system.")
        break

    recommend_products(user_input)