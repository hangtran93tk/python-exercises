from ContactClass import Contact

hang = Contact(
    name="Tran Thu Hang",
    phones=["123","456"],
    emails=["tranthuhang@hotmail.com"],
    address="Hai Duong",
    note="Nothing",
    tags=["dong nghiep", "ban be"]
)
lan = Contact(
    name="Vu Thi Lan",
    phones=["123","456"],
    emails=["vuthilan@hotmail.com"],
    address="Hai Duong",
    note="Nothing",
    tags=["dong nghiep", "ban be"]
)
contacts_list= [hang, lan]
for contact in contacts_list:
    if contact.is_friend():
        print(contact)


# hang.phones = "Who care"
# hang.set_field("name", "Tran")
# print(hang.check_tag("ban be"))
# print(hang)