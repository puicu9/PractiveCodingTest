import numpy as np

lottos = np.random.choice(np.arange(1, 46), 7)
lottoSixNumber = lottos[:-1] # 당첨번호 6개
lottoBonusNumber = lottos[-1] # 보너스 번호

print(lottoSixNumber)
print(lottoBonusNumber)

