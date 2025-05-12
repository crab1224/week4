material = ''
diameter = 0
thickness = 0
area = 0
weight = 0
Mars_Gravity = 0.38
item = {
    '유리': 2.4, '알류미늄': 2.7, '탄소강': 7.85
}
def sphere_area(diameter,material,thickness):
    radius = (diameter * 100) / 2
    Harea = 2 * 3.141 * radius ** 2
    volume = Harea * thickness 
    Fweight = volume * item[material]
    Cweight = (Fweight / 1000) * Mars_Gravity
    area = round(Harea, 3)
    weight = round(Cweight, 3)

    print(f'재질:{material}, 지름:{round(diameter,3)}, 면적:{area}, 무게:{weight}')
while(1):
    print('exit입력시 종료')
    while(1):
        d = input('지름을 입력해주세요:')
        if d.lower() == 'exit':
            exit()
        if d == 0:
            print('0이 아닌 수를 입력해 주세요')
            continue
        if d == '':
            d = 10
        diameter = float(d)
        break
    while(1):
        m = input('재질을 입력해 주세요(유리, 알류미늄, 탄소강중 택1):')
        if m.lower() == 'exit':
            exit()
        if m in item:
            material = m
            break
        if m == '':
            material = '유리'
            break
        else:
            print("다시 입력해 주세요")
    while(1):
        t = input('두께를 입력해 주세요:')
        if t.lower() == 'exit':
            exit()
        elif t == '':
            thickness = float(1)
            break
        try:
            thickness = float(t)
            break
        except Exception:
            print('다시 입력해 주세요.')
    sphere_area(diameter,material,thickness)
