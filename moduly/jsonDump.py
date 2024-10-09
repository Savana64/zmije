import json
slovník = {
    "František Nepil":"Střevíce z lýčí",
    "Douglas Adams":"Převážně neškodná",
    "James Herriot":"Wet in a spin"
}
with open("data.json","w") as file:
    json.dump(slovník,file)