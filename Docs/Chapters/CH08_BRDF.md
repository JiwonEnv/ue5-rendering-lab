# CH08 BRDF와 반사 분포

## 챕터 학습 목표

빛이 표면에서 어떤 방향으로 분포하는지 이해합니다. 하이라이트의 폭과 모양을 조정할 때 거칠기, 표면 방향, 광원 크기의 역할을 구분해 원하는 재질감을 설계합니다.

### 예제 학습 목표

구의 거칠기와 라이트 크기를 각각 따로 바꿔 반사 폭을 만드는 두 원인을 비교합니다.

**구현 상태 — 기본 실습 레벨 준비**

바닥, 조명, 카메라와 비교용 기본 도형을 가진 시작 레벨입니다. 아래 항목은 챕터별 예제를 완성할 때 수행할 실습 절차입니다.

레벨 경로 `/Game/RenderingLab/Chapters/Part02_MaterialsAndLight/CH08_BRDF/Maps/L_CH08_BRDF`

## 흐름 개념도

```mermaid
flowchart LR
 N0["들어오는 빛"]
 N1["표면의 반사 특성"]
 N0 --> N1
 N2["보는 방향의 밝기"]
 N1 --> N2
```

## 원리

BRDF는 어느 방향에서 온 빛이 어느 방향으로 얼마나 반사되는지를 나타내는 함수입니다. 함수는 입력 조건에 따라 결과를 정하는 계산 규칙이라는 뜻입니다. BRDF를 이해하면 같은 색의 물체도 거칠기와 관찰 방향에 따라 다르게 보이는 이유를 설명할 수 있습니다.

## 작동 과정

많은 재질 모델은 표면을 아주 작은 거울 조각들의 집합처럼 근사합니다. 이를 미세면 모델이라고 합니다. 조각의 방향이 고르게 모이면 날카로운 반사가, 넓게 흩어지면 퍼진 반사가 나타납니다. 반사율의 각도 변화와 조각 사이의 가림도 함께 반영합니다. 화면 밝기에는 광원의 밝기·크기와 실제 그림자도 영향을 줍니다.

## 아트 실무

돌 바닥의 닳은 길과 거친 가장자리에 같은 기본 색을 사용해도 거칠기 차이로 사용감을 표현할 수 있습니다. 반사광이 지나치게 넓다면 거칠기뿐 아니라 광원의 크기도 봅니다. 표면에서 밝게 반사되어 보이는 부분을 하이라이트라고 부릅니다.

## 성능 비용

같은 셰이더에서 Roughness 값만 바꾸면 계산 구조는 그대로일 수 있습니다. 코팅과 바탕의 반사를 따로 계산하면 평가할 반사 성분이 늘 수 있습니다. 투과까지 포함하는 더 넓은 규칙은 BSDF라고 하며, Substrate에서는 이런 성분을 조합합니다. 수식의 항을 더 읽고 싶다면 보충 주석 2를 참고합니다.

## 언리얼 실습

같은 구에 거칠기 세 단계를 적용합니다. 면 형태의 광원인 Rect Light의 크기를 고정하고 하이라이트 폭을 비교합니다. 다음에는 재질을 고정하고 광원 크기만 바꿉니다. 두 실험을 분리해야 재질의 변화와 광원의 변화를 구분할 수 있습니다.

## 핵심 요약

반사의 모양은 재질과 빛의 조건이 함께 만듭니다. 수식을 외우기보다 각 입력이 화면을 어떻게 바꾸는지 연결합니다.

## 공식 자료

- [Physically Based Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)
- [Overview of Substrate Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)
- [Real Shading in Unreal Engine 4 · Brian Karis](https://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_notes_v2.pdf)

## 관련 개념

- [CH09 Fresnel과 시선 각도](CH09_Fresnel.md)
- [CH11 Substrate와 재질 레이어](CH11_Substrate.md)

## 작업 기록

- 제작한 에셋
- 바꾼 변수와 유지한 조건
- 전후 화면과 실행 시간
- 확인한 기기와 설정


[처음 읽는 방법](../ReadingGuide.md) · [용어집](../Glossary.md) · [보충 주석](../SupplementaryNotes.md) · [챕터 목록](../../README.md#학습-순서)
