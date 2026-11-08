# CH05 Depth와 Early Z

## 무엇인가

Depth Buffer는 화면 샘플의 앞뒤 관계를 판정하는 깊이 데이터를 보관합니다. Early Z는 그 깊이 판정을 재질 계산보다 일찍 적용해 가려진 후보의 계산을 생략하는 처리입니다.

## 렌더링에서 맡는 역할

깊이 검사는 불투명 표면의 올바른 가림을 만들고, 조기 깊이 검사는 불필요한 픽셀 계산을 줄일 기회를 줍니다. Depth Prepass는 깊이를 미리 준비하는 작업으로 Early Z 자체와는 구분됩니다.

## 입력과 출력

입력은 투영된 표면의 깊이와 이미 기록된 깊이입니다. 비교 결과에 따라 후보가 남거나 탈락하며, 허용되는 조건에서는 비싼 픽셀 셰이더 실행을 줄일 수 있습니다.

## 작동 과정

표면을 화면에 투영하면 위치별 깊이도 얻습니다. 깊이 검사로 같은 화면 위치의 앞뒤를 비교하고 설정한 규칙에 맞는 표면을 남깁니다.

Prepass를 사용하는 경로에서는 먼저 깊이를 그립니다. 이후 표면 계산이 준비된 깊이를 이용할 수 있습니다. 깊이 준비 없이도 Early Z가 가능한 조건이 있으므로 두 용어를 같은 뜻으로 쓰지 않습니다.

일찍 탈락시킬 수 있는 후보는 재질 계산을 건너뛰게 할 수 있습니다. 재질이 깊이나 가시성 결정에 영향을 주는 경우에는 적용 조건이 달라집니다.

![외부 비교 이미지 · 왼쪽은 깊이 비교를 항상 통과, 오른쪽은 앞쪽 깊이를 선택한 OpenGL 예시입니다.](../Images/External/depth-print.png)

외부 비교 이미지 · 왼쪽은 깊이 비교를 항상 통과, 오른쪽은 앞쪽 깊이를 선택한 OpenGL 예시입니다.

읽을 곳  왼쪽에서 바닥이 큐브를 잘못 덮는 부분과 오른쪽의 올바른 가림을 비교합니다. 깊이 검사의 필요성을 보여 주며, Early Z로 몇 ms를 절약했는지 입증하는 이미지는 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 47](https://learnopengl.com/Advanced-OpenGL/Depth-testing)

동일 범위의 원본을 나란히 배치 · 표제 추가

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 왜 배경 제작에 필요한가

밀집 실내에서 벽이 뒤의 소품을 가리는 효과, 식생의 빈 영역 처리와 가림의 차이를 이해할 때 필요합니다. 최종 화면에 안 보인다는 사실만으로 모든 작업이 사라졌다고 생각하지 않습니다.

## 성능과 제작 비용

Prepass는 지오메트리를 다시 처리하는 선행 비용이 있습니다. 줄인 표면 계산이 이 비용보다 큰지 봐야 하며, 깊이 표시가 올바르다는 것과 성능 개선은 별도로 확인합니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

가림 범위가 깊이 표시와 뒤쪽 재질 처리 시간에 미치는 영향을 구분합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH05_DepthEarlyZ/Maps/L_CH05_DepthEarlyZ`

### 실습 절차

비교용 전통 불투명 메시의 뒤 패널에 계산이 많은 재질을 둡니다. 카메라를 고정하고 앞의 단순한 가림판으로 패널을 절반, 대부분 가리는 두 상태를 만듭니다. Prepass 설정은 유지하고 Scene Depth와 Base Pass 시간을 봅니다.

### 예상 결과와 이유

Scene Depth에는 가림판이 앞면으로 보일 것입니다. 조기 깊이 제거가 유효하고 뒤 패널의 픽셀 계산 비중이 크다면, 더 많이 가린 상태에서 해당 계산 시간이 줄 것으로 예상합니다.

### 결과를 어떻게 해석할까

시간이 그대로면 뒤 표면이 원래 싸거나, 다른 일이 지배적이거나, 조기 제거 조건이 다를 수 있습니다. 깊이 표시가 맞는다는 것만으로 최적화 효과를 입증하지 않습니다.

## 이 챕터에서 기억할 것

깊이는 앞뒤를 정하고 Early Z는 가려진 계산을 줄일 기회를 만듭니다. 깊이를 미리 그리는 비용과 절감 효과를 함께 판단합니다.

## 이해한 뒤 확인할 조건

Masked, 깊이를 바꾸는 Pixel Depth Offset, 반투명은 조건이 다릅니다. 먼저 불투명 재질에서 기본 관계를 이해한 뒤 별도로 비교합니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
