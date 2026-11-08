# CH20 Texture Streaming

## 무엇인가

Texture Streaming은 화면에 필요한 텍스처 밉을 추정하고 메모리 예산 안에서 불러오거나 내보내는 관리 시스템입니다. 원본 텍스처를 항상 최고 해상도로 메모리에 두는 방식과 다릅니다.

## 렌더링에서 맡는 역할

많은 에셋을 사용하는 장면에서 메모리와 로딩을 관리합니다. CH19의 밉 선택이 읽을 세부 수준의 문제라면, 스트리밍은 필요한 데이터가 실제로 준비돼 있는지의 문제입니다.

## 입력과 출력

입력은 텍스처와 장면 배치·화면 요구량·메모리 예산입니다. 출력은 로드·해제 요청과 실제로 메모리에 상주하는 밉의 상태입니다.

## 작동 과정

카메라와 물체 크기·거리 등을 이용해 필요한 세부 수준을 추정합니다. 화면에서 원하는 밉과 현재 준비된 밉을 구분합니다.

예산과 우선순위에 맞춰 로드·해제를 결정합니다. 스트리밍 풀은 이 관리에 쓰는 메모리 예산의 한 묶음이며 전체 GPU 메모리와 같은 뜻은 아닙니다.

디스크에서 데이터를 옮겨 요청한 밉을 준비합니다. 이 전송에 시간이 걸리므로 이동 직후 잠시 낮은 밉으로 보이다 선명해질 수 있습니다.

![Epic 공식 통계 화면 · stat streaming의 Memory Counters를 발췌하고 항목과 수치 사이의 여백을 줄였습니다.](../Images/External/streaming-stats-print.png)

Epic 공식 통계 화면 · stat streaming의 Memory Counters를 발췌하고 항목과 수치 사이의 여백을 줄였습니다.

읽을 곳  Memory Counters의 Pool·Required·Visible 등 서로 다른 항목을 구분합니다. 화면의 숫자는 원문 예시이며 권장 예산이 아닙니다. UE 5.5 자료이므로 항목 배치는 현재 빌드에서 확인합니다.

[© Epic Games · 공식 문서 · 출처 54](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-metrics-in-unreal-engine?application_version=5.5)

원본 통계 표 발췌 · 가운데 여백만 축소 · 값과 항목 유지

원저작권과 원문 출처 표시는 유지합니다

## 왜 배경 제작에 필요한가

큰 환경의 텍스처 해상도 배분, 흐린 소품과 팝인, 첫 진입 끊김을 조사할 때 필요합니다. 원본 크기·수요 추정·예산·전송 지연 중 원인을 구분합니다.

## 성능과 제작 비용

높은 밉의 메모리와 데이터 전송이 부담입니다. 풀을 키우면 다른 리소스 여유가 줄 수 있어 경고를 없애는 것만을 목표로 값을 늘리지 않습니다.

## 원리 확인 예제

이 예제는 위에서 설명한 주제의 일부 관계를 확인합니다. 특정 예제가 기술 전체의 정의나 유일한 사용 목적은 아닙니다.

### 예제 학습 목표

첫 진입과 재방문에서 실제 밉 준비 상태와 선명해지는 지연을 대조합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH20_TextureStreaming/Maps/L_CH20_TextureStreaming`

### 실습 절차

고정된 이동 경로를 처음 지나갈 때와 곧바로 재방문할 때 비교합니다. stat streaming에서 필요한 밉, 메모리 예산, 상주·요청 상태를 기록하고 같은 위치의 팝인을 녹화합니다.

### 예상 결과와 이유

처음 데이터가 준비되지 않은 조건에서는 선명해지는 지연이 더 클 수 있습니다. 재방문 때 필요한 밉이 남아 있다면 더 빠르게 선명해질 것입니다.

### 결과를 어떻게 해석할까

두 번 모두 계속 흐리면 예산·수요 추정·최대 해상도를 봅니다. 재방문 개선만으로 원인을 단정하지 말고 실제 밉의 준비 상태와 대조합니다.

## 이 챕터에서 기억할 것

텍스처 스트리밍은 필요한 밉을 메모리에 준비하는 관리입니다. 필요한 양·예산·실제 상주량을 구분해 진단합니다.

## 이해한 뒤 확인할 조건

일반 Texture Streaming은 Virtual Texturing이나 월드 Actor 스트리밍과 같은 기능이 아닙니다. 표의 외부 숫자는 권장 예산이 아닌 항목 설명용입니다.

## 공식 자료와 확장

- [Texture Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine)
- [Texture Streaming Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-overview-for-unreal-engine)
- [Texture Streaming Metrics](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-metrics-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
