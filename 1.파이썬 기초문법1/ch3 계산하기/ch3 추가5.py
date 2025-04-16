import time
fseconds = time.time()
fminutes = fseconds // 60
fhours = fminutes // 60
nminute = int(fminutes % 60)
nhour = int(fhours % 24)
print(f"현재 시간(영국 그리니치 시각): {nhour}시{nminute}분")