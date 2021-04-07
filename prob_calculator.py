import copy
import random
# Consider using the modules imported above.


class Hat:
    # 可変長のキーワード付き引数を取るため、**kwargs を利用
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value

    def draw(self, num):
        contents = self.contents
        if num > len(self.contents):
            retval = self.contents
            self.contents = []
            return retval

        # test_moduleではシードを固定しているので、いつも同じ値がサンプリングされる
        retval = random.sample(self.contents, num)

        # 配列の中で最初に一致した要素を削除していく
        for target in retval:
            contents.remove(target)
        self.contents = contents

        return retval


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    actual = 0
    keyword = {}
    contents = hat.contents
    for i in contents:
        if i in keyword.keys():
            val = keyword[i]
            keyword[i] = val + 1
        else:
            keyword[i] = 1

    for i in range(0, num_experiments):
        # オブジェクト（可変長、map) を引数に渡すので、**を利用
        # 取得したhatをそのままdrawすると、どんどん残りがなくなるので試行の度に生成します
        new_hat = Hat(**keyword)
        result = new_hat.draw(num_balls_drawn)
        correct = True
        for key, value in expected_balls.items():
            if result.count(key) < value:
                correct = False
        if correct == True:
            actual += 1

    # 確率を産出（組み合わせで）
    return actual / num_experiments
