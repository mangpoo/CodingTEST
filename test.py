from collections import Counter


result = []
order = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

counter = Counter()

# order 리스트의 각 요소에 대해
for item in order:
    # 다른 요소와 비교
    for other_item in order:
        if item == other_item:
            continue  # 같은 문자열은 비교하지 않음
    for other_item in order:
        # item이 other_item에 있는지 확인
        if all(c in other_item for c in item):
            counter[item] += 1

for i in course:
    test_course = {}  # 딕셔너리 초기화
    for k, v in counter.items():
        if len(k) == i:
            test_course[k] = v  # 키와 값을 딕셔너리에 추가

    # test_course가 비어 있지 않을 때만 로직 수행
    if test_course:
        # 가장 큰 값 찾기
        max_value = max(test_course.values())

        max_value_keys = []  # 가장 큰 값을 갖는 키를 저장할 리스트
        for k, v in test_course.items():
            if v == max_value:
                max_value_keys.append(k)  # 가장 큰 값을 갖는 키를 리스트에 추가

        result.append(max_value_keys)

print(result)



