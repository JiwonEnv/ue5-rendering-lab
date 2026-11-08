# CH20 Texture Streaming

## 중심 질문

텍스처 원본은 선명한데 게임에서는 왜 잠시 흐리게 보일까?

## 먼저 알아둘 답

화면에 필요한 밉과 현재 메모리에 준비된 밉이 다를 수 있기 때문입니다.

## 왜 알아야 할까

텍스처 자체의 해상도와 메모리·로딩 문제를 구분해 불필요한 고해상도 제작을 피하기 위해 배웁니다.

### 예제 학습 목표

첫 진입과 재방문에서 실제 밉 준비 상태와 선명해지는 지연을 대조합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH20_TextureStreaming/Maps/L_CH20_TextureStreaming`

## 왜 이런 결과가 생길까

스트리머는 화면 크기와 거리 등을 바탕으로 필요한 텍스처 세부 수준을 추정합니다. 이후 메모리 예산과 우선순위 안에서 데이터를 불러오거나 내보냅니다. 디스크에서 메모리로 옮기는 데는 시간이 걸리므로 수요가 생긴 즉시 최고 밉이 준비된다고 보장할 수 없습니다. 수요·예산·실제 상주량은 서로 다른 값입니다.

## 제작 중에는 이렇게 나타납니다

빠른 카메라 이동 후 잠시 흐렸다가 선명해지는 현상은 원본이 작아서 생긴 흐림과 다릅니다. 풀 경고가 있으면 예산 압박도 조사해야 하지만 풀 크기만 늘리면 다른 메모리 여유가 줄 수 있습니다.

![Epic 공식 통계 화면 · stat streaming의 Memory Counters를 발췌하고 항목과 수치 사이의 여백을 줄였습니다.](../Images/External/streaming-stats-print.png)

Epic 공식 통계 화면 · stat streaming의 Memory Counters를 발췌하고 항목과 수치 사이의 여백을 줄였습니다.

읽을 곳  Memory Counters의 Pool·Required·Visible 등 서로 다른 항목을 구분합니다. 화면의 숫자는 원문 예시이며 권장 예산이 아닙니다. UE 5.5 자료이므로 항목 배치는 현재 빌드에서 확인합니다.

[© Epic Games · 공식 문서 · 출처 54](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-metrics-in-unreal-engine?application_version=5.5)

원본 통계 표 발췌 · 가운데 여백만 축소 · 값과 항목 유지

원저작권과 원문 출처 표시는 유지합니다

## 실습 절차

고정된 이동 경로를 처음 지나갈 때와 곧바로 재방문할 때 비교합니다. stat streaming에서 필요한 밉, 메모리 예산, 상주·요청 상태를 기록하고 같은 위치의 팝인을 녹화합니다.

## 예상 결과와 이유

처음 데이터가 준비되지 않은 조건에서는 선명해지는 지연이 더 클 수 있습니다. 재방문 때 필요한 밉이 남아 있다면 더 빠르게 선명해질 것입니다.

## 결과를 어떻게 해석할까

두 번 모두 계속 흐리면 예산·수요 추정·최대 해상도를 봅니다. 재방문 개선만으로 원인을 단정하지 말고 실제 밉의 준비 상태와 대조합니다.

## 실제 제작에서의 선택

가까이 읽히는 소품에 해상도를 배분하고, 먼 소품군의 요구량을 낮춰 예산과 외관을 함께 맞춥니다.

## 이해한 뒤 확인할 조건

일반 Texture Streaming은 Virtual Texturing이나 월드 Actor 스트리밍과 같은 기능이 아닙니다. 표의 외부 숫자는 권장 예산이 아닌 항목 설명용입니다.

## 공식 자료와 확장

- [Texture Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine)
- [Texture Streaming Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-overview-for-unreal-engine)
- [Texture Streaming Metrics](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-metrics-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
