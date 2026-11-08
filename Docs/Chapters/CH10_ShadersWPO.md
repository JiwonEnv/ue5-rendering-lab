# CH10 셰이더와 WPO

## 중심 질문

재질에서 풀을 흔들면 왜 형상과 그림자가 함께 달라질까?

## 먼저 알아둘 답

WPO는 텍스처를 움직이는 대신 기존 정점의 위치를 바꾸므로, 변형된 형상이 표면과 그림자 계산에 전달됩니다.

## 왜 알아야 할까

식생과 천의 움직임을 만들 때 정점 배치와 변형 범위가 결과를 어떻게 제한하는지 이해하기 위해 배웁니다.

### 예제 학습 목표

같은 변위 함수에서 정점의 구간 수가 굽힘에 미치는 영향을 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part02_MaterialsAndLight/CH10_ShadersWPO/Maps/L_CH10_ShadersWPO`

## 왜 이런 결과가 생길까

셰이더는 GPU에서 실행하는 계산 프로그램입니다. 머티리얼 그래프는 그 계산을 노드로 작성하는 도구입니다. World Position Offset은 정점 위치에 더할 이동량을 지정합니다. 밑부분은 0, 끝부분은 큰 이동량을 주면 줄기가 휘어 보입니다. 단, 기존 정점 사이의 삼각형은 그대로 연결되므로 정점이 없는 곳에 새로운 굽힘 구간을 만들지는 않습니다.

## 제작 중에는 이렇게 나타납니다

정점이 적은 긴 풀은 끝만 움직이거나 판 전체가 꺾여 보일 수 있습니다. 텍스처 해상도를 올려도 이런 실루엣 문제는 해결되지 않습니다. 움직인 정점이 그림자에 참여하면 그림자 모양도 바뀝니다.

![직접 제작 기하 예시. 정점 사이를 직선으로 잇기 때문에 같은 변위 함수라도 정점 배치에 따라 굽힘 표현이 달라집니다.](../Images/Focused/focus-10.png)

직접 제작 기하 예시. 정점 사이를 직선으로 잇기 때문에 같은 변위 함수라도 정점 배치에 따라 굽힘 표현이 달라집니다.

## 실습 절차

길이 방향으로 1구간인 카드와 여러 구간인 카드를 만듭니다. 같은 높이 기반 가중치와 같은 바람 함수를 연결합니다. 변형 크기를 고정하고 옆면 실루엣과 바닥 그림자를 비교합니다.

## 예상 결과와 이유

여러 구간 카드는 중간 정점도 이동해 휘어 보이고, 1구간 카드는 중간 굽힘을 표현하지 못할 것입니다. WPO를 끄면 두 카드가 원래 형상으로 돌아옵니다.

## 결과를 어떻게 해석할까

외관 비교 뒤 정점 수와 그림자 조건을 기록하고 비용을 따로 봅니다. 움직임이 화면 가장자리에서 사라지면 메시를 감싸는 판정 범위인 Bounds도 확인합니다.

## 실제 제작에서의 선택

가까이 읽히는 굽힘에 필요한 곳에 정점을 배치합니다. 먼 식생의 변형과 그림자 갱신을 줄일지는 CH22의 원리와 함께 판단합니다.

## 이해한 뒤 확인할 조건

셰이더 순열은 설정 조합별로 준비하는 프로그램 변형입니다. 실행 중 WPO 비용과 컴파일·쿠킹 준비 비용은 다른 문제이므로 이 실습의 결론에 섞지 않습니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Material Editor UI](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-ui)
- [Material Inputs](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-inputs-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
