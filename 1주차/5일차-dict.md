
# 📚 배열 `list(리스트)` & `dict(딕셔너리)` 

---


## 1. 딕셔너리 (dict) 필수 메서드

| 메서드                        | 시간 복잡도        | 테스터가 노리는 함정 → 대응법                                                        |              |
| -------------------------- | ------------- | ------------------------------------------------------------------------ | ------------ |
| `get(겟)`                   | **O(1)**      | `KeyError` 방어 + 기본값.<br>`freq[x] = freq.get(x,0)+1` 패턴 암기.               |              |
| `setdefault(셋디폴트)`         | **O(1)**      | 그룹핑 `d.setdefault(k, []).append(v)` 한 줄.<br>단, default 객체는 **한 번만** 생성됨. |              |
| `items(아이템즈)`              | **O(1)** view | 순회 중 변경 금지 → `list(items)` 복사.                                           |              |
| `keys(키즈)` / `values(밸류즈)` | **O(1)** view | `if k in d` 대신 `k in d` 가 더 빠름.                                          |              |
| `pop`                      | **O(1)**      | 예외 없이 삭제 + 반환. queue 필터링에 유용.                                            |              |
| `update(업데이트)`             | **O(m)**      | 두 dict 병합. Py 3.9 이상 \`                                                  | =\` 연산자와 동일. |
| `fromkeys(프롬키즈)`           | **O(n)**      | 동일 초깃값으로 대량 키 초기화. **별로 안 씀** – 참고만.                                     |              |
| `Counter(카운터)` *(표준 lib)*  | **O(n)**      | 1 줄 빈도 집계. 내부적으로 `get`+`+=1` 최적화.                                        |              |
| `defaultdict(디폴트딕트)`       | **O(1)**      | 다단계 중첩 기본값. BFS 레벨별 큐·트라이 구축 때 필수.                                       |              |

---

## 2. ‘필수 패턴’ 4 개 

| 패턴         | 예시 코드                                    | 피해야 할 느린 코드                   |
| ---------- | ---------------------------------------- | ----------------------------- |
| **빈도 집계**  | `freq[k] = freq.get(k,0)+1`              | `if k in freq: … else:`       |
| **그룹핑**    | `groups[v] = groups.get(v,[])+[k]`       | `append` 대상 리스트를 먼저 `if` 로 생성 |
| **해시 2‑키** | `d[(x,y)] = …`                           | 중첩 dict 남발로 KeyError 폭탄       |
| **필터링 삭제** | `d = {k:v for k,v in d.items() if cond}` | 순회 중 `del d[k]`               |

---

## 3. 알고리즘 실전 적용 Check‑List

1. **슬라이딩 윈도우**   `deque` 로 인덱스·값 동시에 관리 → `max O(n)`
2. **투 포인터**   정렬된 리스트에서 `sort` + 양쪽 포인터 이동
3. **해시 + 정렬**   “빈도 기준 정렬” 시험 단골 → `Counter.most_common()`
4. **우선순위 큐**   `heapq` pop = O(log n) → 리스트에 `sort` 매번 돌리지 마라.
5. **LRU 캐시**   `OrderedDict` or `collections.deque` + `dict` 병용

---












