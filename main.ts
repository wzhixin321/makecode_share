input.onButtonPressed(Button.A, function () {
    basic.showString("" + 猫 + "=" + 人)
})
let 人 = 0
let 猫 = 0
猫 = 1
人 = 20
for (let index = 0; index < 11; index++) {
    猫 += 1
    人 += 4
}
