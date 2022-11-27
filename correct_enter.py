def correct_rational(num):
    if num.replace('.', '').isdigit():
        result = float(num)
    else:
        result = complex(num)
    return result


def get_real(num):
    real_num = []
    for i in range(0, len(num)):
        temp = str(num[i])
        if temp.replace('.', '').isdigit():
            real_num.append(temp)
    return real_num


def get_im(num):
    im_num = []
    for i in range(0, len(num)):
        temp = str(num[i])
        if temp.replace('.', '').isdigit():
            continue
        else:
            im_num.append(temp)
    return im_num
