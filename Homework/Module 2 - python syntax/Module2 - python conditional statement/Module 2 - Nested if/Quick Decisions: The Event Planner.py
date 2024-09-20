




attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
media = "audio system" if attendees > 100 else "projector"
print(media)
vegetarian = input("Do you want vegetarian food yes or no?")
catering = "veggie delight caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(catering)