import time

# 현재 UTC 시각 가져오기
utc_time = time.gmtime() # UTC 기준의 현재 시각

# 특정 지역 시각 가져오기 (korea : UTC +9)
korea_hour = (utc_time.tm_hour + 9) % 24

print(f'utc : {utc_time.tm_hour}시 {utc_time.tm_min}분 {utc_time.tm_sec}초')
print(f'korea: {korea_hour}시 {utc_time.tm_min}분 {utc_time.tm_sec}초')
