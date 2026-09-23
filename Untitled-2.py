def place_order(item, spice="medium",
                 address="Home"):
    print(item, "|", spice, "|", address)

place_order("Biryani")
place_order("Biryani", "extra hot")
place_order("biryani", "medium hot")
place_order("veg biryani",(item:Any,spice:str="medium"))
