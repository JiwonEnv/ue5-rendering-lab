# CH05 Depth와 Early Z

## 중심 질문

앞에 벽이 있으면 뒤의 비싼 재질 계산도 하지 않을까?

## 먼저 알아둘 답

깊이 검사는 가려짐을 판정하고, 그 판정을 재질 계산보다 일찍 할 수 있을 때 뒤 표면의 불필요한 계산을 줄입니다.

## 왜 알아야 할까

실내·밀집 건축·식생에서 가림이 실제로 어떤 일을 줄이는지 이해하기 위해 배웁니다.

### 예제 학습 목표

가림 범위가 깊이 표시와 뒤쪽 재질 처리 시간에 미치는 영향을 구분합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH05_DepthEarlyZ/Maps/L_CH05_DepthEarlyZ`

## 왜 이런 결과가 생길까

화면의 한 위치에 여러 불투명 표면이 겹치면 가까운 표면이 남아야 합니다. 깊이 버퍼는 이 비교에 쓸 깊이를 보관합니다. Early Z는 깊이로 탈락할 후보를 비싼 픽셀 계산 전에 제외하는 처리입니다. Depth Prepass는 깊이를 먼저 그려 준비하는 별도 작업이며, Early Z 자체와 같은 뜻은 아닙니다.

## 제작 중에는 이렇게 나타납니다

깊이를 먼저 준비하면 뒤의 재질 계산을 줄일 기회가 생기지만, 앞서 깊이를 그리는 일도 비용입니다. 따라서 최종 화면에서 가려졌다는 사실과 GPU 일이 얼마나 줄었는지는 별개입니다.

![외부 비교 이미지 · 왼쪽은 깊이 비교를 항상 통과, 오른쪽은 앞쪽 깊이를 선택한 OpenGL 예시입니다.](../Images/External/depth-print.png)

외부 비교 이미지 · 왼쪽은 깊이 비교를 항상 통과, 오른쪽은 앞쪽 깊이를 선택한 OpenGL 예시입니다.

읽을 곳  왼쪽에서 바닥이 큐브를 잘못 덮는 부분과 오른쪽의 올바른 가림을 비교합니다. 깊이 검사의 필요성을 보여 주며, Early Z로 몇 ms를 절약했는지 입증하는 이미지는 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 47](https://learnopengl.com/Advanced-OpenGL/Depth-testing)

동일 범위의 원본을 나란히 배치 · 표제 추가

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 실습 절차

비교용 전통 불투명 메시의 뒤 패널에 계산이 많은 재질을 둡니다. 카메라를 고정하고 앞의 단순한 가림판으로 패널을 절반, 대부분 가리는 두 상태를 만듭니다. Prepass 설정은 유지하고 Scene Depth와 Base Pass 시간을 봅니다.

## 예상 결과와 이유

Scene Depth에는 가림판이 앞면으로 보일 것입니다. 조기 깊이 제거가 유효하고 뒤 패널의 픽셀 계산 비중이 크다면, 더 많이 가린 상태에서 해당 계산 시간이 줄 것으로 예상합니다.

## 결과를 어떻게 해석할까

시간이 그대로면 뒤 표면이 원래 싸거나, 다른 일이 지배적이거나, 조기 제거 조건이 다를 수 있습니다. 깊이 표시가 맞는다는 것만으로 최적화 효과를 입증하지 않습니다.

## 실제 제작에서의 선택

불투명 가림을 활용하되 Prepass만 늘리면 빨라진다고 결정하지 않습니다. 가려진 픽셀 계산을 줄인 이득과 깊이 준비 비용을 함께 봅니다.

## 이해한 뒤 확인할 조건

Masked, 깊이를 바꾸는 Pixel Depth Offset, 반투명은 조건이 다릅니다. 먼저 불투명 재질에서 기본 관계를 이해한 뒤 별도로 비교합니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
