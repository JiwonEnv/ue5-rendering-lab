# CH11 Substrate와 물질 적층

## 중심 질문

페인트 위 투명 코팅은 왜 두 재질의 색을 섞는 것만으로 충분하지 않을까?

## 먼저 알아둘 답

위아래 물질은 빛이 차례로 통과하는 관계를 가지므로, 단순한 파라미터 평균과 다른 반응을 만듭니다.

## 왜 알아야 할까

도장·코팅·물기 같은 복합 표면에서 혼합과 적층 중 어떤 구조가 필요한지 선택하기 위해 배웁니다.

### 예제 학습 목표

단일 표면 근사와 위아래 적층의 반응을 여러 각도에서 비교합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part02_MaterialsAndLight/CH11_Substrate/Maps/L_CH11_Substrate`

## 왜 이런 결과가 생길까

두 재료를 나란히 섞은 표면에서는 위치마다 서로 다른 재료가 보입니다. 반면 코팅에서는 빛 일부가 윗면에서 반사되고 나머지가 아래층에 도달한 뒤 다시 나옵니다. 아래층의 빛은 윗층의 영향을 받습니다. Substrate는 빛과 물질의 상호작용을 표현하는 Slab과 연산자를 연결해 이런 관계를 구성합니다.

## 제작 중에는 이렇게 나타납니다

아래 페인트는 거칠고 위 코팅은 매끈한 경우, 위층의 선명한 반사와 아래층의 넓은 반응이 함께 필요할 수 있습니다. 거칠기 하나를 평균하면 그 두 반응을 하나로 바꿔 버립니다.

![직접 제작 개념도. 한 표면의 파라미터 혼합과, 위아래 물질을 통과하는 빛의 관계를 구분합니다.](../Images/Focused/focus-11.png)

직접 제작 개념도. 한 표면의 파라미터 혼합과, 위아래 물질을 통과하는 빛의 관계를 구분합니다.

## 실습 절차

같은 구에 아래층의 색·거칠기를 고정합니다. 하나는 그 위에 별도 Slab을 수직 적층하고, 다른 하나는 단일 Slab의 값을 조정한 근사 버전으로 둡니다. 카메라와 광원을 유지하며 넓은 각도로 관찰합니다.

## 예상 결과와 이유

적층 버전에서는 위층 반사와 아래층 반응을 독립적으로 조절할 여지가 생깁니다. 단일 표면은 한 각도에서 비슷해도 다른 각도에서 두 반응을 동시에 맞추기 어려울 수 있습니다.

## 결과를 어떻게 해석할까

결과가 비슷하다면 조명과 관찰 각도가 층 차이를 드러내는지 확인합니다. 실제 실시간 결과에는 단순화가 개입할 수 있으므로 사용한 설정도 기록합니다.

## 실제 제작에서의 선택

여러 각도에서 읽히는 층 반응이 필요하면 적층을 검토합니다. 차이가 거의 읽히지 않는 원거리 표면은 단순한 재질로 근사하고 비용을 비교합니다.

## 이해한 뒤 확인할 조건

Slab 수만으로 고정 비용을 단정하지 않습니다. 저장 형식·단순화·플랫폼 지원은 버전에 따라 확인할 심화 내용입니다.

## 공식 자료와 확장

- [Programming with Substrate GBuffer Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)
- [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine)
- [Overview of Substrate Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
