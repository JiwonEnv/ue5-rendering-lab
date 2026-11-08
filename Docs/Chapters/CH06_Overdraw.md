# CH06 Overdraw와 화면 겹침

## 중심 질문

삼각형을 줄인 풀 카드가 왜 더 느릴 수 있을까?

## 먼저 알아둘 답

풀의 비용은 삼각형 수뿐 아니라 잎이 없는 영역과 겹친 층에서 반복하는 화면 계산에도 달려 있습니다.

## 왜 알아야 할까

식생과 파티클의 모양을 다듬을 때 폴리곤 수와 화면 낭비 사이의 균형을 잡기 위해 배웁니다.

### 예제 학습 목표

삼각형을 더 쓴 카드가 빈 화면 영역의 처리를 줄일 수 있는지 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH06_Overdraw/Maps/L_CH06_Overdraw`

## 왜 이런 결과가 생길까

큰 사각형 카드에 작은 잎을 그리면 사각형 안에서 어느 부분을 남길지 마스크를 검사해야 합니다. 빈 영역이 넓거나 카드가 여러 겹이면 화면의 비슷한 위치를 반복 처리할 수 있습니다. Overdraw는 이런 중복 처리와 관련된 개념입니다. 잎 윤곽대로 메시를 다듬으면 삼각형은 늘어도 검사할 빈 영역은 줄어듭니다.

## 제작 중에는 이렇게 나타납니다

가까이서 화면을 크게 덮는 식생에서는 삼각형 몇 개를 아끼는 것보다 카드의 빈 공간을 줄이는 편이 유리할 수 있습니다. 반대로 지나치게 세분한 형상은 정점과 작은 삼각형 처리 부담을 늘립니다.

![외부 진단 화면 · Android Developers가 소개한 Unreal Editor의 Quad Overdraw 시각화입니다.](../Images/External/overdraw-print.png)

외부 진단 화면 · Android Developers가 소개한 Unreal Editor의 Quad Overdraw 시각화입니다.

읽을 곳  겹친 영역의 진단색과 아래 범례를 같이 봅니다. 작은 화면 묶음에서의 처리 비효율을 찾는 화면이며 실제 GPU 시간은 아닙니다. 원본은 이전 에디터 UI로 UE 5.8의 메뉴 배치는 다를 수 있습니다.

[Android Developers · Google · 출처 48](https://developer.android.com/games/optimize/materials)

원본 전체 유지 · 투명 배경은 흰색으로 표시

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 실습 절차

같은 잎 텍스처를 쓰는 큰 사각형 카드와 윤곽을 다듬은 카드를 만듭니다. 잎의 실제 크기·배치·재질·그림자는 같게 두고 가까운 구도에서 비교합니다. Shader Complexity와 가능한 Quad Overdraw를 본 뒤 진단을 끄고 GPU 시간을 기록합니다.

## 예상 결과와 이유

윤곽을 다듬은 버전은 빈 영역의 진단 부담이 줄 것으로 예상합니다. 픽셀 처리가 병목이라면 삼각형이 늘어도 실행 시간이 줄 수 있습니다.

## 결과를 어떻게 해석할까

진단색 감소는 낭비 영역을 찾는 단서입니다. 실행 시간과 같은 단위가 아니므로 비용 감소는 별도로 확인합니다. 원거리에서도 같은 결론인지 다시 봅니다.

## 실제 제작에서의 선택

메시를 무조건 사각형으로 줄이지 말고, 보이는 잎 면적에 비해 빈 영역이 얼마나 큰지 먼저 확인합니다.

## 이해한 뒤 확인할 조건

Quad Overdraw는 작은 화면 묶음의 처리 비효율도 보여 줍니다. 일반 Overdraw와 완전히 같은 지표는 아니며 Nanite는 전용 시각화를 함께 사용합니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Viewport Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
