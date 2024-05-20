#In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?
#make_negative(1);  # return -1
#make_negative(-5); # return -5
#make_negative(0);  # return 0

#Notes

#The number can be negative already, in which case no change is required.
#Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.


def return_negative(x: int) -> int:
    if x < 0:
        return x
    if x == 0:
        return 0
    if x > 0:
        return x * (-1)

print(return_negative(10))


def return_negative2(x: int) -> int:
    return -x if x>0 else x

print(return_negative2(10))
print(return_negative2(0))
print(return_negative2(-2))