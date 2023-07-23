

class multifuntions():
    def subfields():
        subfields = ["machine learning", "neural learning", "vision", "robotics", "speech processing", "natural language processing"]
        print("Sub-field in AI:")
        for i in subfields:
            print(i)
    
    def OddEven():
        num=int(input("enter the no"))
        if num%2==0:
            print("even no")
        else:
            print("odd no")
    
    def Eligible():
        gender = input(str("Your gender: "))
        age = int(input("Your age:"))
        if age >= 18:
            print("Eligible for marriage")
        else:
            print("Not eligible")

    
    def percentage():
        subject_scores = [23, 45, 34, 23, 23]
        total = sum(subject_scores)
        total_marks_possible = 500 
        percentage = (total / total_marks_possible) * 100
        dic = {
        "Subject1": subject_scores[0],
        "Subject2": subject_scores[1],
        "Subject3": subject_scores[2],
        "Subject4": subject_scores[3],
        "Subject5": subject_scores[4],
        "Total": total,
        "Percentage": percentage,
         }

        for key in dic:
            value = dic[key]
            print(f"{key}= {value}")
            

    def triangle():
        h=int(input("hieght"))
        b=int(input("weight"))
        hieght1=int(input("hieght1"))
        hieght2=int(input("hieght2"))
        area =(h*b)/2
        print("area of triangle:",area)
        print("hieght1:", hieght1)
        print("hieght2:", hieght2)
        print("breath:",b)
        perimeter=hieght1+hieght1+b
        print("perimeter of triangle:",perimeter)