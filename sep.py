def grad(grad1 , grad2 , grad3):
    average = (grad1 + grad2 + grad3) / 3
    return average


def check_grad(average):

    if average >= 18:
        return "very good"

    elif average >= 15:
        return "good"

    elif average >= 10:
        return "pass"

    else:
        return "Faild!"

def show(name , average , status):
    print("====== student report =====")
    print()
    print("Name:" , name)
    print("Average:" , average)
    print("status:" , status)
    print()
    print("===========================")



name = input("Enter your name:")

grad1 = float(input("enter grad 1 :"))
grad2 = float(input("enter grad 2 :"))
grad3 = float(input("enter grad 3 :"))



if (0 <= grad1 <= 20 and 0 <= grad2 <= 20 and 0 <= grad3 <= 20):

        average = grad(grad1 , grad2 , grad3)
        status = check_grad(average)
        show(name , average , status)


else:
     print("invalid")


