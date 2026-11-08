# CH03 GBuffer와 표면 정보

## 중심 질문

벽이 번들거릴 때 왜 최종 색보다 Roughness 화면을 먼저 볼까?

## 먼저 알아둘 답

GBuffer는 조명을 계산하기 전의 표면 정보를 보관하므로, 재질 입력 문제와 조명 결과를 나눠 볼 수 있습니다.

## 왜 알아야 할까

반사가 어색할 때 재질을 수정해야 하는지 조명을 수정해야 하는지 판단하기 위해 배웁니다.

### 예제 학습 목표

거칠기 변경과 광원 변경이 서로 다른 진단 화면에 나타나는지 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH03_GBuffer/Maps/L_CH03_GBuffer`

## 왜 이런 결과가 생길까

Deferred 렌더러는 보이는 불투명 표면의 기본 색, 표면 방향인 법선, 거칠기 같은 정보를 기록합니다. 조명 단계는 이 값을 읽어 반사의 색과 분포를 계산합니다. 같은 표면 정보라도 광원의 위치와 밝기가 달라지면 최종 색은 달라집니다. Buffer Visualization은 그 입력 정보를 따로 확인하는 통로입니다.

## 제작 중에는 이렇게 나타납니다

Roughness는 반사가 퍼지는 정도를 조절하는 값입니다. 벽의 반사가 좁고 강해 보일 때 거칠기가 의도보다 낮은지 먼저 보면, 라이트를 임의로 약하게 만들어 재질 오류를 가리는 일을 줄일 수 있습니다.

![외부 시각화 이미지 · 같은 장면의 위치·법선·Albedo·Specular를 분리해 표시한 GBuffer 예시입니다.](../Images/External/gbuffer-print.png)

외부 시각화 이미지 · 같은 장면의 위치·법선·Albedo·Specular를 분리해 표시한 GBuffer 예시입니다.

읽을 곳  왼쪽 위는 위치에 따라, 오른쪽 위는 표면 방향에 따라 색이 달라집니다. 아래쪽은 재질의 색과 반사 입력입니다. 진단용 색을 최종 외관이나 UE 채널 구성으로 읽지 않습니다.

[© Joey de Vries · LearnOpenGL · @JoeyDeVriez · 출처 39](https://learnopengl.com/Advanced-Lighting/Deferred-Shading)

원본 전체와 비율 유지

[이용 조건 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 실습 절차

같은 벽의 Material Instance 두 개를 만들고 Roughness만 0.2와 0.8로 둡니다. Material Instance는 원본 재질의 구조를 공유하며 설정값을 바꾸는 변형입니다. 같은 구도에서 Roughness, Base Color, Lit 순서로 비교합니다.

## 예상 결과와 이유

Roughness 진단은 달라지고 Base Color는 유지되며, Lit에서는 반사의 퍼짐이 달라질 것입니다. 다음으로 라이트 위치만 바꾸면 Lit는 달라져도 두 표면 입력은 유지될 것입니다.

## 결과를 어떻게 해석할까

첫 비교는 재질 입력이 결과에 미치는 영향을, 두 번째 비교는 같은 입력에 조명이 미치는 영향을 보여 줍니다. 진단 표시색을 실제 저장 바이트 배열로 해석할 필요는 없습니다.

## 실제 제작에서의 선택

입력 진단이 의도와 다르면 텍스처·값·연결을 고칩니다. 입력이 맞으면 반사 환경과 광원, 노출을 조사합니다.

## 이해한 뒤 확인할 조건

GBuffer의 채널과 저장량은 렌더러·플랫폼·Substrate 설정에 따라 달라집니다. 해상도와 메모리 비용의 관계는 이 실험과 별개의 성능 확인 항목입니다.

## 공식 자료와 확장

- [Render Dependency Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-dependency-graph-in-unreal-engine)
- [Programming with Substrate GBuffer Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
