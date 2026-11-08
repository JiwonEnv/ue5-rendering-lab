# Depth와 Early Z 가려진 표면의 계산은 언제 멈출까

벽 뒤의 소품은 화면에 보이지 않습니다. 그렇다고 그 소품과 관련된 모든 GPU 작업이 처음부터 없었던 것은 아닙니다. 올바르게 가리는 일과, 가려질 계산을 일찍 줄이는 일의 차이가 Depth와 Early Z를 이해하는 핵심입니다.

Depth Buffer는 화면 샘플의 앞뒤 관계를 판정하는 깊이 데이터를 보관합니다. Early Z는 그 깊이 판정을 재질 계산보다 일찍 적용해 가려진 후보의 계산을 생략하는 처리입니다.

깊이 검사는 불투명 표면의 올바른 가림을 만들고, 조기 깊이 검사는 불필요한 픽셀 계산을 줄일 기회를 줍니다. Depth Prepass는 깊이를 미리 준비하는 작업으로 Early Z 자체와는 구분됩니다.

## 앞뒤 판정과 조기 생략은 다른 역할이다

표면을 투영하면서 얻은 깊이는 이미 기록된 깊이와 비교됩니다. 그 결과에 따라 후보가 남거나 탈락하며, 가능한 조건에서는 비싼 픽셀 셰이더 계산 전에 탈락시킬 수 있습니다.

표면을 화면에 투영하면 위치별 깊이도 얻습니다. 깊이 검사로 같은 화면 위치의 앞뒤를 비교하고 설정한 규칙에 맞는 표면을 남깁니다. Prepass를 사용하는 경로에서는 먼저 깊이를 그립니다. 이후 표면 계산이 준비된 깊이를 이용할 수 있습니다. 깊이 준비 없이도 Early Z가 가능한 조건이 있으므로 두 용어를 같은 뜻으로 쓰지 않습니다. 일찍 탈락시킬 수 있는 후보는 재질 계산을 건너뛰게 할 수 있습니다. 재질이 깊이나 가시성 결정에 영향을 주는 경우에는 적용 조건이 달라집니다.

![외부 깊이 검사 비교는 앞뒤 판정의 역할을 보여 줍니다. 이것만으로 Early Z의 절감 시간까지 입증되는 것은 아닙니다.](../Images/External/depth-print.png)

외부 깊이 검사 비교는 앞뒤 판정의 역할을 보여 줍니다. 이것만으로 Early Z의 절감 시간까지 입증되는 것은 아닙니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 47](https://learnopengl.com/Advanced-OpenGL/Depth-testing)

동일 범위의 원본을 나란히 배치 · 표제 추가

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 벽 하나가 줄일 수 있는 일

밀집 실내에서 벽이 뒤의 소품을 가리는 효과, 식생의 빈 영역 처리와 가림의 차이를 이해할 때 필요합니다. 최종 화면에 안 보인다는 사실만으로 모든 작업이 사라졌다고 생각하지 않습니다.

비싼 표면이 앞의 불투명 벽에 가려질 때 조기 깊이 제거가 유효하다면 그 표면의 픽셀 계산을 줄일 수 있습니다. 하지만 정점 처리와 별도 그림자 작업까지 같은 방식으로 모두 없어지는 것은 아닙니다. 화면에서 사라진 양과 절약된 전체 시간은 같지 않습니다.

## 깊이를 먼저 준비하는 대가

Prepass는 지오메트리를 다시 처리하는 선행 비용이 있습니다. 줄인 표면 계산이 이 비용보다 큰지 봐야 하며, 깊이 표시가 올바르다는 것과 성능 개선은 별도로 확인합니다.

깊이 버퍼는 보이는 앞면을 정하고 Early Z는 그 정보를 일찍 활용할 기회를 만듭니다. 가려짐의 정확성과 계산 절감을 나눠 이해해야 깊이 프리패스를 만능 최적화로 받아들이지 않게 됩니다.

## 참고 자료

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine)

[포스트 목록](../../README.md#포스트-목록) · [용어 찾아보기](../Glossary.md) · [이미지 출처](../Images/Sources.md)
