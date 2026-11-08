# CH18 Culling과 가시성

## 챕터 학습 목표

화면에 기여하지 않는 작업을 줄이는 가시성 판정과 bounds의 역할을 이해합니다. 건물·실내·변형 에셋의 분할 단위를 정하고, 불필요한 렌더링과 갑작스러운 사라짐을 진단합니다.

### 예제 학습 목표

꺾인 복도의 합체·분할 메시에서 bounds, 가림 판정과 모서리 이동 중의 표시 변화를 비교합니다.

**구현 상태 — 기본 실습 레벨 준비**

바닥, 조명, 카메라와 비교용 기본 도형을 가진 시작 레벨입니다. 아래 항목은 챕터별 예제를 완성할 때 수행할 실습 절차입니다.

레벨 경로 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH18_Culling/Maps/L_CH18_Culling`

## 흐름 개념도

```mermaid
flowchart LR
 N0["거리로 제외"]
 N1["카메라 범위로 제외"]
 N0 --> N1
 N2["가려짐으로 제외"]
 N1 --> N2
```

## 원리

컬링은 최종 화면에 필요하지 않은 렌더링 후보를 제외하는 과정입니다. 멀리 있는 물체, 카메라 밖 물체, 다른 물체 뒤에 완전히 가린 물체를 각각 다른 기준으로 판정합니다. 화면의 가시성을 잘 나누면 이후 단계에서 처리할 메시와 표면 계산을 줄일 수 있습니다.

## 작동 과정

카메라가 볼 수 있는 3D 공간을 뷰 프러스텀 또는 시야 절두체라고 합니다. 엔진은 먼저 범위 밖 후보를 줄이고 깊이 정보 등으로 가려짐을 판정할 수 있습니다. 물체의 모든 삼각형 대신 물체를 감싸는 상자나 구를 사용하는 경우가 많습니다. 이 둘러싼 범위가 bounds입니다.

## 그림으로 연결하기

![Epic 공식 단계별 그림 · 시야 밖 제외와 앞 물체에 가려진 후보의 제외를 보여 줍니다.](../Images/External/culling-print.png)

Epic 공식 단계별 그림 · 시야 밖 제외와 앞 물체에 가려진 후보의 제외를 보여 줍니다.

읽을 곳  오른쪽의 점선으로 남은 물체와 앞쪽의 흰 물체를 비교합니다. 왼쪽은 전체 배치이며, 오른쪽은 시야·가림 판정을 적용한 상태입니다. 최종 화면에서 빠져도 그림자용 작업까지 모두 사라진다고 해석하지 않습니다.

[© Epic Games · 공식 문서 · 출처 53](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine)

원저작권과 원문 출처 표시는 유지합니다

동일 범위의 원본을 나란히 배치 · 표제 추가

## 아트 실무

긴 건물 전체를 하나로 합치면 작은 부분만 보여도 큰 bounds가 가시 판정을 받을 수 있습니다. 반대로 공간 단위로 나누면 벽 뒤 부분을 제외하기 쉬워질 수 있습니다. WPO로 흔들리는 풀은 원래 bounds 밖으로 정점이 나가 갑자기 사라지는지도 봅니다.

## 성능 비용

잘게 나누면 제외 기회가 늘 수 있지만 관리할 오브젝트와 가시성 검사·제출 작업도 늘어납니다. 큰 bounds는 너무 많은 부분을 가시 후보로 남길 수 있습니다. 메인 카메라에서 안 보이는 물체가 화면의 그림자에는 기여할 수 있다는 점도 구분합니다.

## 언리얼 실습

꺾인 복도에 합체 벽과 구획별 벽을 준비합니다. Viewport의 Bounds 표시로 판정 범위를 보고, 지원되는 경로에서 r.VisualizeOccludedPrimitives 1로 가려진 후보를 확인합니다. 카메라를 모서리 너머로 움직여 표시 수치와 갑작스러운 등장·사라짐을 기록합니다.

## 관찰과 판단

가려지는 복도의 건물을 합체·구획 버전으로 비교합니다. Bounds를 표시한 뒤 가림 판정과 메인 카메라 외 그림자 기여를 구분합니다. 모퉁이에서 갑자기 나타나거나 사라지는지도 영상으로 확인합니다.

## 오판을 피하려면

시야 밖 제외와 벽 뒤 가림은 다른 판정입니다. 화면에서 안 보인다는 이유만으로 그림자와 준비 작업까지 전혀 수행하지 않는다고 결론 내리지 않습니다.

## 핵심 요약

작업 모듈의 편의와 가시성 판정의 효율을 함께 고려해 메시를 나눕니다.

## 공식 자료

- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)
- [Visibility and Occlusion Culling](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine)

## 관련 개념

- [CH05 Depth와 Early Z](CH05_DepthEarlyZ.md)
- [CH14 Draw Call과 배칭](CH14_DrawCalls.md)

## 작업 기록

- 제작한 에셋
- 바꾼 변수와 유지한 조건
- 전후 화면과 실행 시간
- 확인한 기기와 설정


[처음 읽는 방법](../ReadingGuide.md) · [용어집](../Glossary.md) · [보충 주석](../SupplementaryNotes.md) · [챕터 목록](../../README.md#학습-순서)
