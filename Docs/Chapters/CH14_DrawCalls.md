# CH14 Draw Call과 제출 작업

## 중심 질문

소품 하나인데 왜 여러 번 그리는 명령이 생길까?

## 먼저 알아둘 답

그리기 명령은 Actor 개수보다 메시의 구역·재질·참여 패스에 따라 나뉩니다.

## 왜 알아야 할까

모듈 배경의 재질 슬롯과 합체 단위를 CPU 제출 부담에 근거해 설계하기 위해 배웁니다.

### 예제 학습 목표

Actor 수를 유지하고 섹션 수에 따른 제출 변화를 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH14_DrawCalls/Maps/L_CH14_DrawCalls`

## 왜 이런 결과가 생길까

Draw Call은 GPU에 정해진 상태로 지오메트리를 그리도록 제출하는 명령입니다. 한 메시가 서로 다른 재질 구역인 섹션으로 나뉘면 별도 그리기 작업이 필요할 수 있습니다. 같은 메시가 깊이·카메라 표면·그림자 작업에 각각 참여하기도 합니다. 그래서 레벨에 배치한 Actor 하나를 명령 하나로 셀 수 없습니다.

## 제작 중에는 이렇게 나타납니다

오브젝트 수만 줄이려고 메시를 합쳐도 재질 구역이 그대로라면 기대만큼 제출이 줄지 않을 수 있습니다. 반대로 너무 크게 합치면 일부만 보일 때도 전체가 가시 후보로 남을 수 있습니다.

![직접 제작 관계도. Actor 수, 메시 섹션, 패스별 그리기 작업을 나누어 보여 줍니다. 명령 수의 고정 공식은 아닙니다.](../Images/Focused/focus-14.png)

직접 제작 관계도. Actor 수, 메시 섹션, 패스별 그리기 작업을 나누어 보여 줍니다. 명령 수의 고정 공식은 아닙니다.

## 실습 절차

자동 묶음의 영향을 통제한 비교 장면에서 외관과 삼각형이 같은 1섹션 메시와 여러 섹션 메시를 준비합니다. 수량·재질 동작·그림자 조건을 맞추고 stat scenerendering 또는 stat rhi의 관련 그리기 수치를 기록합니다.

## 예상 결과와 이유

섹션 분리가 패스별 제출을 늘리는 조건이라면 여러 섹션 버전의 그리기 수치가 높아질 것입니다. GPU 시간이 반드시 같은 비율로 늘어나는 것은 아닙니다.

## 결과를 어떻게 해석할까

stat unit의 Draw는 주로 CPU 렌더 스레드 시간이며 호출 개수가 아닙니다. 호출 수가 줄었는지와 실제 병목 시간이 줄었는지는 따로 기록합니다.

## 실제 제작에서의 선택

읽히지 않는 슬롯 분할을 줄이고 공유 가능한 재질을 검토합니다. 합체 여부는 제출 이득과 가시성 손실을 함께 비교해 결정합니다.

## 이해한 뒤 확인할 조건

호환되는 명령을 묶는 배칭과 Nanite의 제출 방식은 결과를 바꿀 수 있습니다. 먼저 사용한 경로를 고정하고 비교합니다.

## 공식 자료와 확장

- [Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
- [Mesh Drawing Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-drawing-pipeline-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
