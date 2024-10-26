def part_one():
    with open("1-input.txt", "r") as file:
        tot = 0

        for line in file:
            nums = []
            for i in line:
                if i.isnumeric():
                    nums.append(str(i))

            num = nums[0]+nums[-1]
            tot += int((num))
    
    return (tot)
def part_two():
    with open("1-input.txt", "r") as file:
        tot = 0

        for line in file:
            nums = []
            for index in range(0,len(line)):
                if line[index].isnumeric():
                    nums.append(str(line[index]))
                elif index <= (len(line)-3) and line[index:index+3] == "one":
                    nums.append("1")
                elif index <= (len(line)-3) and line[index:index+3] == "two":
                    nums.append("2")
                elif index <= (len(line)-5) and line[index:index+5] == "three":
                    nums.append("3")
                elif index <= (len(line)-4) and line[index:index+4] == "four":
                    nums.append("4")
                elif index <= (len(line)-4) and line[index:index+4] == "five":
                    nums.append("5")
                elif index <= (len(line)-3) and line[index:index+3] == "six":
                    nums.append("6")
                elif index <= (len(line)-5) and line[index:index+5] == "seven":
                    nums.append("7")
                elif index <= (len(line)-5) and line[index:index+5] == "eight":
                    nums.append("8")
                elif index <= (len(line)-4) and line[index:index+4] == "nine":
                    nums.append("9")
            print(nums)
            num = nums[0]+nums[-1]
            tot += int((num)) 
    return (tot)



if __name__ == "__main__":
    print(part_one())
    print(part_two())
