# CH06 Overdraw와 화면 겹침

## 무엇인가

Overdraw는 화면의 같은 영역에 여러 표면 후보가 그려져 반복 처리되는 현상입니다. 앞뒤 표면의 겹침, 마스크 검사와 반투명 층 합성 등에서 생길 수 있으며 반복 처리 모두가 불필요한 것은 아닙니다.

## 렌더링에서 맡는 역할

삼각형 개수만으로 설명되지 않는 화면 단위의 작업량을 이해하는 개념입니다. 깊이로 일찍 제거할 수 없는 표면이나 여러 층이 필요한 합성에서는 중복 비용이 남기 쉽습니다.

## 입력과 출력

입력은 겹친 삼각형의 화면 범위와 재질·깊이 조건입니다. 결과는 위치별로 실행되는 표면 처리와 합성이며, 비용은 겹침뿐 아니라 각 처리의 계산량에도 달려 있습니다.

## 작동 과정

삼각형이 화면을 덮으면 표면 후보가 생깁니다. Opaque는 불투명, Masked는 마스크로 남길 부분을 결정하고, Translucent는 뒤의 색과 섞는 표현입니다.

큰 풀 카드의 빈 부분도 어느 영역을 버릴지 마스크를 확인해야 할 수 있습니다. 잎이 작은데 카드가 크면 잎 바깥의 넓은 영역까지 후보를 만듭니다.

여러 카드나 투명 층이 겹치면 비슷한 화면 위치를 반복 처리합니다. 불투명 깊이 제거, 마스크와 반투명 조건에 따라 실제 실행과 생략의 정도가 달라집니다.

![외부 진단 화면 · Android Developers가 소개한 Unreal Editor의 Quad Overdraw 시각화입니다.](../Images/External/overdraw-print.png)

외부 진단 화면 · Android Developers가 소개한 Unreal Editor의 Quad Overdraw 시각화입니다.

읽을 곳  겹친 영역의 진단색과 아래 범례를 같이 봅니다. 작은 화면 묶음에서의 처리 비효율을 찾는 화면이며 실제 GPU 시간은 아닙니다. 원본은 이전 에디터 UI로 UE 5.8의 메뉴 배치는 다를 수 있습니다.

[Android Developers · Google · 출처 48](https://developer.android.com/games/optimize/materials)

원본 전체 유지 · 투명 배경은 흰색으로 표시

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 왜 배경 제작에 필요한가

풀·나뭇잎·연기·머리카락에서 메시의 빈 공간과 겹침을 줄일 때 필요합니다. 윤곽을 다듬어 삼각형을 늘려도 화면 낭비가 줄어 전체가 빨라지는 경우를 설명합니다.

## 성능과 제작 비용

겹치는 면적·층 수·재질 계산이 함께 비용을 만듭니다. Shader Complexity와 Quad Overdraw는 원인 후보를 보는 진단이며 실제 실행 시간과 같은 단위가 아닙니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

삼각형을 더 쓴 카드가 빈 화면 영역의 처리를 줄일 수 있는지 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH06_Overdraw/Maps/L_CH06_Overdraw`

### 실습 절차

같은 잎 텍스처를 쓰는 큰 사각형 카드와 윤곽을 다듬은 카드를 만듭니다. 잎의 실제 크기·배치·재질·그림자는 같게 두고 가까운 구도에서 비교합니다. Shader Complexity와 가능한 Quad Overdraw를 본 뒤 진단을 끄고 GPU 시간을 기록합니다.

### 예상 결과와 이유

윤곽을 다듬은 버전은 빈 영역의 진단 부담이 줄 것으로 예상합니다. 픽셀 처리가 병목이라면 삼각형이 늘어도 실행 시간이 줄 수 있습니다.

### 결과를 어떻게 해석할까

진단색 감소는 낭비 영역을 찾는 단서입니다. 실행 시간과 같은 단위가 아니므로 비용 감소는 별도로 확인합니다. 원거리에서도 같은 결론인지 다시 봅니다.

## 이 챕터에서 기억할 것

Overdraw는 같은 화면 영역을 반복 처리하는 문제입니다. 폴리곤 수와 함께 화면 면적·빈 공간·겹친 층을 봅니다.

## 이해한 뒤 확인할 조건

Quad Overdraw는 작은 화면 묶음의 처리 비효율도 보여 줍니다. 일반 Overdraw와 완전히 같은 지표는 아니며 Nanite는 전용 시각화를 함께 사용합니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Viewport Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
