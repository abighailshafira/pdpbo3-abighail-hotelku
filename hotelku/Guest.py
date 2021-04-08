class Guest:
    def __init__ (self, guest_name, guest_number, total_guest, room_type, room_number, additional_dish, additional_bed, room_price, filename, image):
        super().__init__()
        self.guest_name = guest_name
        self.guest_number = guest_number
        self.total_guest = total_guest
        self.room_type = room_type
        self.room_number = room_number
        self.additional_dish = additional_dish
        self.additional_bed = additional_bed
        self.room_price = room_price
        self.filename = filename
        self.image = image

    def get_image(self):
        return self.image