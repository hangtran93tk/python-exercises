from ContactClass import Contact

hang = Contact(
    name="Tran Thu Hang",
    phones=["123","456"],
    emails=["tranthuhang@hotmail.com"],
    address="Hai Duong",
    note="Nothing",
    tags=["dong nghiep", "ban be"]
)
hang.phones = "Who care"
hang.set_field("name", "Tran")
print(hang.get_info())
print(hang.check_tag("ban be"))