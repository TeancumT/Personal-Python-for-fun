import random as ra


def addUser(data, username, lvl=0, health=100, money=0, items=eval("{" + "}")):
    for player in data["players"]:
        if player["username"] == username:
            print("Can Not Add" + username)
            break
    else:
        truthy = True
        while truthy:
            truthy = False
            userId = ra.randint(-(64 ** 15), 64 ** 15)
            for player in data["players"]:
                if player["id"] == userId:
                    truthy = truthy or True
        data["players"].append(
            {
                "id": userId,
                "username": username,
                "lvl": lvl,
                "health": health,
                "money": money,
                "items": eval(str(items)),
            }
        )


def removeUserId(data, id):
    for player in data["players"]:
        if player["id"] == id:
            data["players"].remove(player)


def removeUserName(data, username):
    for player in data["players"]:
        if player["username"] == username:
            data["players"].remove(player)


def setItemName(data, username, itemName, number):
    if number > 0:
        for player in data["players"]:
            if player["username"] == username:
                player["items"][itemName] = number
    else:
        for player in data["players"]:
            if player["username"] == username:
                del player["items"][itemName]


def setItemId(data, id, itemName, number):
    for player in data["players"]:
        if player["id"] == id:
            player["items"][itemName] = number
    else:
        for player in data["players"]:
            if player["id"] == id:
                del player["items"][itemName]


def example():
    data = {"players": []}
    addUser(data, "Tim", 0, 100, 0, {"Corn": 10})
    setItemName(data, "Tim", "Corn", 4)
    print(data["players"][0])
    setItemName(data, "Tim", "Corn", -1)
    print(data["players"][0])


if __name__ == "__main__":
    example()
