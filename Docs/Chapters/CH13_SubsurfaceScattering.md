# CH13 SSS와 표면 아래 산란

## 중심 질문

왁스는 왜 두께와 역광에 따라 색과 밝기가 달라질까?

## 먼저 알아둘 답

빛이 표면에서 바로 반사되는 대신 내부를 지나며 흩어지고 흡수되기 때문입니다.

## 왜 알아야 할까

왁스·피부·일부 돌과 식생의 밀도감을 단순 투명도와 구분해 제작하기 위해 배웁니다.

### 예제 학습 목표

한 산란 모델에서 얇은 부분과 두꺼운 부분의 역광 반응을 비교합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part02_MaterialsAndLight/CH13_SubsurfaceScattering/Maps/L_CH13_SubsurfaceScattering`

## 왜 이런 결과가 생길까

Subsurface Scattering은 들어온 빛이 내부에서 산란한 뒤 다른 위치나 방향으로 나오는 현상입니다. 지나온 거리와 물질의 흡수 특성에 따라 나오는 빛의 색과 양이 달라집니다. 얇은 부분과 두꺼운 부분의 반응이 다른 이유입니다. 일반 표면 반사만으로는 이 부드러운 내부 빛 전달을 충분히 표현하기 어렵습니다.

## 제작 중에는 이렇게 나타납니다

알파를 낮춰 뒤 배경이 비치게 하는 것과 빛이 물질 내부를 거쳐 나오는 것은 다릅니다. 왁스의 역광을 만들려고 투명도만 낮추면 재료가 유리처럼 보일 수 있습니다.

![직접 제작 빛 전달 개념도. 얇고 두꺼운 부분에서 달라질 수 있는 내부 경로를 비교합니다. 실제 결과는 재료와 선택한 산란 모델에 달려 있습니다.](../Images/Focused/focus-13.png)

직접 제작 빛 전달 개념도. 얇고 두꺼운 부분에서 달라질 수 있는 내부 경로를 비교합니다. 실제 결과는 재료와 선택한 산란 모델에 달려 있습니다.

## 실습 절차

얇은 돌기와 두꺼운 몸통이 있는 형상에 같은 산란 재질을 적용합니다. 한 가지 SSS 모델을 고정하고 전면광과 역광을 각각 관찰합니다. 일반 불투명 표면 재질과도 비교합니다.

## 예상 결과와 이유

역광에서 얇은 부분의 빛 전달이 두꺼운 몸통과 다르게 보일 것으로 예상합니다. 일반 표면 재질은 같은 내부 산란 반응을 만들지 못할 것입니다.

## 결과를 어떻게 해석할까

예상 차이가 없으면 선택 모델이 두께를 어떻게 근사하거나 입력받는지 확인합니다. 모델의 입력 의미를 먼저 확인하지 않고 Opacity 숫자를 다른 SSS 방식에 옮기지 않습니다.

## 실제 제작에서의 선택

원하는 재료의 두께·스케일·조명 방향을 함께 맞춥니다. 산란색만 붉게 바꿔 모든 밀도감을 해결하려 하지 않습니다.

## 이해한 뒤 확인할 조건

Subsurface, Subsurface Profile, Substrate는 같은 입력값이 같은 의미라고 가정할 수 없습니다. 내부 경로 그림도 현상의 설명이며 선택한 모델의 실제 추적을 재현한 것은 아닙니다.

## 공식 자료와 확장

- [Overview of Substrate Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)
- [Subsurface Profile Shading Model](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
