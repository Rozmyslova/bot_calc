from correct_enter import get_real
from correct_enter import get_im


def subtraction_real(num):
    result = float(num[0])
    for i in range(1, len(num)):
        result = result - float(num[i])
    return result


def subtraction_im(num):
    if 'j' in num:
        temp = list(num[0])
        last_im = temp[len(temp) - 1]
        del temp[len(temp) - 1]
        temp = ("".join(temp))
        answer = int(temp)
        if len(num) == 1:
            result = str(num[0])
        else:
            for i in range(1, len(num)):
                temp_new = list(num[i])
                last_im_new = temp_new[len(temp_new) - 1]
                if last_im == last_im_new:
                    del temp_new[len(temp_new) - 1]
                    temp_new = ("".join(temp_new))
                    answer = answer - int(temp_new)
                    result = str(answer)+str(last_im_new)
                else:
                    result = 'Error'
                    break
    else:
        result = 0
    return result


def subtraction(num):
    num = num.replace(",", ".")
    num = num.split()
    real_num = get_real(num)
    im_num = get_im(num)
    real_res = subtraction_real(real_num)
    im_res = subtraction_im(im_num)
    if len(im_num) == 0:
        result = str(real_res)
    elif len(real_num) == 0:
        result = str(im_res)
    else:
        result = str(real_res) + "-" + str(im_res)
    return result
