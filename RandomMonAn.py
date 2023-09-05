import random

# Danh sách đồ ăn
food_list = ["Bún chả", "Phở", "Cơm tấm", "Bánh mì", "Bún bò Huế", "Bánh xèo", "Gỏi cuốn", "Bún mọc", "Bún thang", "Bún sườn", "Mì xào","Bún ốc","Bún riêu","Bún lòng","Bún đậu mắm tôm","Bánh cuốn","Cơm thố","Cơm rang","Bún ngan"]

def choose_food():
    return random.choice(food_list)

def main():
    print("Hôm nay ăn gì?")
    selected_food = choose_food()
    print(f"Hôm nay bạn nên ăn: {selected_food}")

if __name__ == "__main__":
    main()