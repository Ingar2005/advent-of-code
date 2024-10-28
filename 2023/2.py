
def part_one():
    with open("2-input.txt", "r") as file:

        tot = 0 
        for line in file:

            red_cont = 12
            green_cont = 13
            blue_cont = 14
            game_id = ((line.split(":")[0]))
            game_id = int(game_id.split()[1])
            contents = (line.split(":")[1])[:-1].replace(";", ",").split(",")

            real = True
            for i in contents:
                split = i.split()
                num = int(split[0])
                color = split[1]

                if color == "red" and num > red_cont:
                    real = False 
                elif color == "green" and num > green_cont:
                    real = False 
                elif color == "blue" and num > blue_cont:
                    real = False 
            if real is True:
                tot += game_id
        return tot 


def part_two():
    with open("2-input.txt", "r") as file:
        tot = 0
        for line in file:
           
            red_min = 0
            green_min = 0
            blue_min = 0
            game_id = ((line.split(":")[0]))
            game_id = int(game_id.split()[1])
            contents = (line.split(":")[1])[:-1].replace(";", ",").split(",")

            for i in contents:
                split = i.split()
                num = int(split[0])
                color = split[1]
    
                if color == "red" and num > red_min:
                    red_min = num 
                elif color == "green" and num > green_min:
                    green_min = num 
                elif color == "blue" and num > blue_min:
                    blue_min = num 
                power = red_min * green_min * blue_min 
            tot += power
               
        return tot


if __name__ == "__main__":
        print(part_one())
        print(part_two())

