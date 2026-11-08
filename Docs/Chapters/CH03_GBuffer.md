# CH03 GBuffer와 표면 정보

## 무엇인가

GBuffer는 Deferred 조명이 사용할 표면 특성을 화면 위치별로 저장하는 버퍼 묶음입니다. 버퍼는 계산에 쓸 데이터를 보관하는 메모리이며, GBuffer는 최종 사진이 아닌 표면 정보의 중간 저장소입니다.

## 렌더링에서 맡는 역할

표면의 기본 색과 방향·거칠기를 조명 계산과 분리합니다. 이 데이터를 기록한 뒤 여러 조명과 후속 계산이 재사용할 수 있습니다. 재질 입력과 조명 결과를 따로 진단할 수 있는 이유도 여기에 있습니다.

## 입력과 출력

입력은 보이는 표면에서 재질이 계산한 속성입니다. 출력은 해당 화면 위치의 표면 데이터이며, 이후 조명은 깊이·카메라·광원 정보와 함께 이를 읽어 조명된 색을 만듭니다.

## 작동 과정

표면을 그리는 Base Pass에서 텍스처와 재질 입력을 평가합니다. Base Color는 기본 표면색, Roughness는 반사 분포의 거칠기, 법선은 표면 방향을 나타냅니다.

계산한 속성을 정해진 형식으로 저장합니다. Scene Depth는 별도의 깊이 정보입니다. 모든 속성이 각각 독립된 이미지 하나에 저장되는 것은 아니며, 채널 배치는 렌더러와 저장 형식에 따라 달라집니다.

조명 단계가 저장한 값을 읽고 빛의 방향·세기와 표면 반응을 결합합니다. 같은 표면 데이터도 조명이 바뀌면 최종 색이 달라집니다. Buffer Visualization은 일부 정보를 관찰용으로 표시합니다.

![외부 시각화 이미지 · 같은 장면의 위치·법선·Albedo·Specular를 분리해 표시한 GBuffer 예시입니다.](../Images/External/gbuffer-print.png)

외부 시각화 이미지 · 같은 장면의 위치·법선·Albedo·Specular를 분리해 표시한 GBuffer 예시입니다.

읽을 곳  왼쪽 위는 위치에 따라, 오른쪽 위는 표면 방향에 따라 색이 달라집니다. 아래쪽은 재질의 색과 반사 입력입니다. 진단용 색을 최종 외관이나 UE 채널 구성으로 읽지 않습니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 39](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 왜 배경 제작에 필요한가

벽의 번들거림은 Roughness, 반사의 방향 오류는 World Normal, 고정된 색 얼룩은 Base Color부터 확인할 수 있습니다. 진단이 의도와 다르면 재질 입력을, 입력이 맞으면 조명과 반사 환경을 조사합니다.

## 성능과 제작 비용

저장할 화면 픽셀 수와 픽셀당 데이터가 메모리 사용과 대역폭을 좌우합니다. 머티리얼 노드 수가 많아졌다는 사실만으로 GBuffer의 바이트 수가 같은 비율로 늘지는 않습니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

거칠기 변경과 광원 변경이 서로 다른 진단 화면에 나타나는지 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH03_GBuffer/Maps/L_CH03_GBuffer`

### 실습 절차

같은 벽의 Material Instance 두 개를 만들고 Roughness만 0.2와 0.8로 둡니다. Material Instance는 원본 재질의 구조를 공유하며 설정값을 바꾸는 변형입니다. 같은 구도에서 Roughness, Base Color, Lit 순서로 비교합니다.

### 예상 결과와 이유

Roughness 진단은 달라지고 Base Color는 유지되며, Lit에서는 반사의 퍼짐이 달라질 것입니다. 다음으로 라이트 위치만 바꾸면 Lit는 달라져도 두 표면 입력은 유지될 것입니다.

### 결과를 어떻게 해석할까

첫 비교는 재질 입력이 결과에 미치는 영향을, 두 번째 비교는 같은 입력에 조명이 미치는 영향을 보여 줍니다. 진단 표시색을 실제 저장 바이트 배열로 해석할 필요는 없습니다.

## 이 챕터에서 기억할 것

GBuffer는 조명이 읽는 표면 데이터입니다. 표면 자체의 오류와 빛을 계산한 뒤의 결과를 구분하는 데 사용합니다.

## 이해한 뒤 확인할 조건

GBuffer의 채널과 저장량은 렌더러·플랫폼·Substrate 설정에 따라 달라집니다. 해상도와 메모리 비용의 관계는 이 실험과 별개의 성능 확인 항목입니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Programming with Substrate GBuffer Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
