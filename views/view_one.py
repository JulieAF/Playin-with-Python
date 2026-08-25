import random
import time

available_adventurers = {
    "Knight": {
        "role": "Tank",
        "health": 120,
        "attack": 18,
        "defense": 15,
    },
    "Wizard": {
        "role": "Mage",
        "health": 70,
        "attack": 28,
        "defense": 5,
    },
    "Ranger": {
        "role": "Scout",
        "health": 90,
        "attack": 20,
        "defense": 10,
    },
    "Cleric": {
        "role": "Healer",
        "health": 95,
        "attack": 12,
        "defense": 12,
    },
    "Rogue": {
        "role": "Stealth",
        "health": 80,
        "attack": 24,
        "defense": 8,
    },
}

quests = [
    "Slay the Dragon",
    "Rescue the Prince",
    "Explore the Haunted Ruins",
    "Recover the Lost Relic",
    "Defend the Village",
]

# Give every adventurer a random level and bonus stats
for stats in available_adventurers.values():
    level = random.randint(1, 5)

    stats["level"] = level
    stats["health"] += level * 8
    stats["attack"] += level * 3
    stats["defense"] += level * 2

party = []

print("=== Available Adventurers ===")

for name, stats in available_adventurers.items():
    print(f"\n{name}")
    print(f" Role: {stats['role']}")
    print(f" Level: {stats['level']}")
    print(f" HP: {stats['health']}")
    print(f" ATK: {stats['attack']}")
    print(f" DEF: {stats['defense']}")

    answer = input("Recruit this adventurer? (y/n): ").lower()

    if answer == "y":
        party.append((name, stats))

print("\n=== Quest Party ===")

if len(party) == 0:
    print("No one joined your quest!")
else:
    for name, stats in party:
        print(f"{name} (Level {stats['level']} {stats['role']})")

total_health = sum(stats["health"] for _, stats in party)
total_attack = sum(stats["attack"] for _, stats in party)
total_defense = sum(stats["defense"] for _, stats in party)

print("\n=== Party Stats ===")
print(f"Health : {total_health}")
print(f"Attack : {total_attack}")
print(f"Defense: {total_defense}")

power = total_health + total_attack + total_defense

print(f"\nParty Power: {power}")

if power >= 500:
    print("Legendary party assembled!")
elif power >= 350:
    print("A strong group of adventurers.")
elif power > 0:
    print("Your party may struggle on difficult quests.")

if len(party) >= 3:
    quest = random.choice(quests)

    print("\n=== Quest Assigned ===")
    print(f"Mission : {quest['name']}")
    print(f"Terrain: {quest['terrain']}")
else:
    print("\nYou need at least 3 adventurers before beginning the quest.")
    {"name": "Slay the Dragon", "terrain": "Volcanic Mountains"},
    {"name": "Rescue the Prince", "terrain": "Dark Forest"},
    {"name": "Explore the Haunted Ruins", "terrain": "Ancient Desert"},
    {"name": "Recover the Lost Relic", "terrain": "Crystal Caves"},
    {"name": "Defend the Village", "terrain": "Rolling Plains"},
weather_events = [
    {
        "name": "The Whispering Fog",
        "description": "A thick gray mist crawls across the land. Something moves just beyond sight...",
        "effect": "Visibility reduced. Monsters gain +10 stealth.",
        "danger": 3,
    },
    {
        "name": "Blood Moon Storm",
        "description": "The sky turns crimson as thunder shakes the forgotten valleys.",
        "effect": "Enemies become stronger under the blood moon.",
        "danger": 5,
    },
    {
        "name": "The Hollow Wind",
        "description": "Cold winds howl through empty forests, carrying voices of the lost.",
        "effect": "Travel speed reduced. Morale decreases.",
        "danger": 2,
    },
    {
        "name": "Black Rain",
        "description": "Dark droplets fall from the sky. The earth beneath your feet begins to rot.",
        "effect": "Plants become corrupted. Poison chance increases.",
        "danger": 4,
    },
    {
        "name": "Ghostly Snowfall",
        "description": "Frozen flakes drift downward, glowing with pale spirits.",
        "effect": "Ancient ruins become visible.",
        "danger": 3,
    },
    {
        "name": "Silent Thunder",
        "description": "Lightning flashes across the sky, but no sound follows...",
        "effect": "Rare creatures appear.",
        "danger": 5,
    },
    {
        "name": "Normal Night",
        "description": "The stars shine sparkly above the wilderness.",
        "effect": "Safe travel.",
        "danger": 0,
    },
]


def generate_weather():
    return random.choice(weather_events)


def display_weather(weather):
    print("\n🌩️ TERRAIN QUEST WEATHER REPORT 🌩️")
    print("-" * 35)
    time.sleep(1)

    print(f"☁️ Event: {weather['name']}")
    time.sleep(0.5)

    print(f"\n{weather['description']}")
    time.sleep(0.5)

    print(f"\n⚔️ Effect: {weather['effect']}")
    print(f"☠️ Danger Level: {weather['danger']}/5")


def weather_roll():
    weather = generate_weather()
    display_weather(weather)

    if weather["danger"] >= 4:
        print("\n⚠️ Warning: Something dangerous approaches...")
    elif weather["danger"] == 0:
        print("\n✨ The land feels strangely peaceful...")


# Run weather system
weather_roll()
print("🧙 Potion Quest")
print("You need to gather ingredients for a healing potion.")

ingredients = []
print("Your ingredient bag is empty.")
print("🧙 Potion Quest")
print("You need to gather ingredients for a healing potion.")

ingredients = []

print("🌸 You found a Moonflower!")
ingredients.append("Moonflower")

print("Ingredients:", ingredients)
print("🧙 Potion Quest")
print("You need to gather ingredients for a healing potion.")

ingredients = []

print("🌸 You found a Moonflower!")
ingredients.append("Moonflower")

print("💧 You collected Crystal Water from a nearby spring!")
ingredients.append("Crystal Water")

print("Ingredients:", ingredients)
print("🧙 Potion Quest")
print("You need to gather ingredients for a healing potion.")

ingredients = []

print("🌸 You found a Moonflower!")
ingredients.append("Moonflower")

print("💧 You collected Crystal Water from a nearby spring!")
ingredients.append("Crystal Water")

print("🐉 You discovered a Dragon Scale!")
ingredients.append("Dragon Scale")

print("Ingredients:", ingredients)
print("🧙 Potion Quest")
print("You need to gather ingredients for a healing potion.")

ingredients = []

print("🌸 You found a Moonflower!")
ingredients.append("Moonflower")

print("💧 You collected Crystal Water from a nearby spring!")
ingredients.append("Crystal Water")

print("🐉 You discovered a Dragon Scale!")
ingredients.append("Dragon Scale")

required_ingredients = ["Moonflower", "Crystal Water", "Dragon Scale"]

print("\n🧪 Checking ingredients...")

if all(item in ingredients for item in required_ingredients):
    print("✨ You have everything you need!")
    print("🧪 The healing potion is ready to brew!")
else:
    print("❌ You're still missing an ingredient.")

print("\nYour ingredients:")
for ingredient in ingredients:
    print(f"- {ingredient}")
potions = []

print("🧪 Brewing a Mana Potion...")
potions.append("Mana Potion")

print("Potions:", potions)
potions = []

print("🧪 Brewing a Mana Potion...")
potions.append("Mana Potion")

print("🧪 Brewing a Strength Potion...")
potions.append("Strength Potion")

print("Potions:", potions)
potions = []

print("🧪 Brewing a Mana Potion...")
potions.append("Mana Potion")

print("🧪 Brewing a Strength Potion...")
potions.append("Strength Potion")

print("🧪 Brewing a Protection Potion...")
potions.append("Protection Potion")

print("\nPotions:", potions)
potions = []

print("🧪 Brewing a Mana Potion...")
potions.append("Mana Potion")

print("🧪 Brewing a Strength Potion...")
potions.append("Strength Potion")

print("🧪 Brewing a Protection Potion...")
potions.append("Protection Potion")

required_potions = ["Mana Potion", "Strength Potion", "Protection Potion"]

print("\n🔮 Checking your potion collection...")

if all(potion in potions for potion in required_potions):
    print("✨ You have collected all the required potions!")
    print("🧙 You may visit the Wizard.")
else:
    print("❌ You don't have enough potions.")
    potions = []

print("🧪 Brewing a Mana Potion...")
potions.append("Mana Potion")

print("🧪 Brewing a Strength Potion...")
potions.append("Strength Potion")

print("🧪 Brewing a Protection Potion...")
potions.append("Protection Potion")

required_potions = ["Mana Potion", "Strength Potion", "Protection Potion"]

print("\n🔮 Checking your potion collection...")

if all(potion in potions for potion in required_potions):
    print("✨ You have collected all the required potions!")
    print("🧙 You may visit the Wizard.")

    print("\n🏰 You arrive at the Wizard's tower.")
    print("🧙‍♂️ Wizard: 'Ah! You have brought the potions I requested.'")
    print("🧙‍♂️ Wizard: 'I have something important to tell you...'")
else:
    print("❌ You don't have enough potions.")
    print("🚫 The Wizard will not see you yet.")
print("🏰 You enter the Wizard's tower.")
print("The room is filled with glowing books and bubbling cauldrons.")
print("🧙‍♂️ A mysterious wizard approaches you.")

wizard_met = True

if wizard_met:
    print("✨ You have met the Wizard!")
print("🏰 You enter the Wizard's tower.")
print("The room is filled with glowing books and bubbling cauldrons.")

wizard_met = True

if wizard_met:
    print("✨ You have met the Wizard!")
    print("🧙‍♂️ Wizard: Welcome, brave adventurer.")
    print("🧙‍♂️ Wizard: I have been expecting you.")
wizard_name = "Eldrin"

print("🏰 You enter the Wizard's tower.")
print("The room is filled with glowing books and bubbling cauldrons.")

wizard_met = True

if wizard_met:
    print(f"✨ You have met Wizard {wizard_name}!")
    print(f"🧙‍♂️ {wizard_name}: Welcome, brave adventurer.")
    print(f"🧙‍♂️ {wizard_name}: I have been expecting you.")
wizard_name = "Eldrin"

print("🏰 You enter the Wizard's tower.")

wizard_met = True

if wizard_met:
    print(f"✨ You have met Wizard {wizard_name}!")
    print(f"🧙‍♂️ {wizard_name}: Welcome, brave adventurer.")
    print(f"🧙‍♂️ {wizard_name}: I have been expecting you.")
    print(f"🧙‍♂️ {wizard_name}: The forest has become dangerous.")
    print(f"🧙‍♂️ {wizard_name}: I need you to investigate what is happening.")
wizard_name = "Eldrin"

print("🏰 You enter the Wizard's tower.")

wizard_met = True
quest_accepted = False

if wizard_met:
    print(f"✨ You have met Wizard {wizard_name}!")
    print(f"🧙‍♂️ {wizard_name}: Welcome, brave adventurer.")
    print(f"🧙‍♂️ {wizard_name}: I have a quest for you.")
    print(f"🧙‍♂️ {wizard_name}: The forest has become dangerous.")

    quest_accepted = True

if quest_accepted:
    print("\n📜 QUEST ACCEPTED!")
    print("Investigate the mysterious forest.")
print("You walk confidently into the forest...")
print("CRACK!")
print("You fall into a hidden pitfall.")
health = 100

print("The fall hurts!")
health -= 15

print(f"Health: {health}")
import time

print("You find a quiet clearing and decide to rest.")
time.sleep(3)
print("You wake up feeling slightly better.")
stamina = 100

print("The journey has been exhausting.")
stamina -= 30

print(f"Stamina remaining: {stamina}")
directions = ["north", "south", "east", "west"]

print("You check your map.")
print("Unfortunately, the map is upside down.")
print("You have no idea where you are.")
print("You discover a mysterious trail.")
print("A sign reads: 'SHORTCUT - probably safe.'")
print("You decide to take your chances.")
print("The shortcut seemed like a good idea...")
print("It was not.")
print("You step on a pressure plate.")
health = 85

potion = 20
health += potion

print("You drink a healing potion.")
print(f"Health restored to {health}.")
