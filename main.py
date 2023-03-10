def on_button_pressed_a():
    basic.show_string("" + str(猫) + "，" + str(人))
input.on_button_pressed(Button.A, on_button_pressed_a)

猫 = 0
人 = 0
人 = 20
猫 = 1

def on_forever():
    global 人, 猫
    for index in range(11):
        人 += 4
        猫 += 1
basic.forever(on_forever)
