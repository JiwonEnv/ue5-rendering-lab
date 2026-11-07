# CH20 Texture Streaming과 메모리 예산

## 챕터 학습 목표

화면의 텍스처 수요와 메모리에 상주하는 데이터의 차이를 이해합니다. 큰 환경을 이동할 때 흐린 재질·팝인·끊김이 예산, 수요 추정, I/O 중 무엇과 연결되는지 판단합니다.

### 예제 학습 목표

시장 씬의 첫 진입과 재방문을 비교하고 일부 소품의 해상도를 낮춰 풀 압박과 외관 변화를 확인합니다.

**구현 상태 — 기본 실습 레벨 준비**

바닥, 조명, 카메라와 비교용 기본 도형을 가진 시작 레벨입니다. 아래 항목은 챕터별 예제를 완성할 때 수행할 실습 절차입니다.

레벨 경로 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH20_TextureStreaming/Maps/L_CH20_TextureStreaming`

## 흐름 개념도

```mermaid
flowchart LR
 N0["필요한 해상도 추정"]
 N1["메모리 예산과 조정"]
 N0 --> N1
 N2["밉 로드와 해제"]
 N1 --> N2
```

## 원리

텍스처 스트리밍은 필요에 따라 텍스처의 해상도 단계를 메모리로 가져오거나 내보내는 관리 방식입니다. 화면에서 원하는 밉과 지금 메모리에 있는 밉은 다를 수 있습니다. 일반 Texture Streaming, 텍스처를 작은 타일로 나누는 Virtual Texturing, 월드의 Actor를 불러오는 방식은 구분해서 읽습니다.

## 작동 과정

스트리머는 카메라와 물체의 거리, 화면에서 필요한 텍셀 밀도 등을 이용해 수요를 추정합니다. 텍셀 밀도는 표면이나 화면 범위에 어느 정도의 텍스처 정보가 필요한지와 관련된 크기 기준입니다. 이후 메모리 예산과 우선순위에 맞춰 로드·해제를 요청합니다. 디스크에서 데이터를 옮기는 작업을 I/O라고 부릅니다.

## 아트 실무

시장 전경의 모든 소품에 큰 텍스처를 쓰면 한 번에 필요한 메모리가 커질 수 있습니다. 가까이 볼 간판과 먼 배경 용기를 나눠 해상도를 정합니다. 흐리게 보이면 텍스처 크기뿐 아니라 UV 스케일, 수요 추정과 로딩 지연도 확인합니다.

## 성능 비용

스트리밍 풀은 이 관리에 사용할 메모리 예산의 한 묶음입니다. 풀을 키우면 높은 밉을 유지하기 쉬울 수 있지만 다른 리소스가 쓸 여유는 줄어듭니다. 큰 상주 데이터와 급격한 카메라 이동은 전송량·로딩 지연을 늘릴 수 있습니다. 경고 하나만 보고 무조건 풀부터 키우지 않습니다.

## 언리얼 실습

stat streaming을 켜고 같은 경로의 첫 진입과 재방문을 비교합니다. 처음 데이터를 읽는 조건을 콜드, 이미 준비된 조건을 웜이라고 부릅니다. 일부 소품의 최대 해상도만 낮추고 풀 사용량·선명도·갑자기 선명해지는 팝인을 기록합니다. 변경한 배치를 반영하도록 텍스처 스트리밍 데이터도 갱신합니다.

## 핵심 요약

메모리 부족, 잘못 추정한 수요와 데이터를 늦게 읽는 문제를 나누어 진단합니다.

## 그림으로 연결하기

![CH20 설명도](../Images/Concepts/explain-20.png)

시점에 필요한 밉을 저장 장치에서 메모리로 가져옵니다. 메모리 예산 부족과 읽기 지연은 다른 문제이므로 함께 기록합니다.

## 공식 자료

- [Texture Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine)
- [Texture Streaming Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-overview-for-unreal-engine)
- [Texture Streaming Metrics](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-metrics-in-unreal-engine)

## 관련 개념

- [CH19 Mipmap과 텍스처 샘플링](CH19_Mipmaps.md)
- [CH25 CPU와 GPU 병목](CH25_CPUGPUBottlenecks.md)

## 작업 기록

- 제작한 에셋
- 바꾼 변수와 유지한 조건
- 전후 화면과 실행 시간
- 확인한 기기와 설정


[처음 읽는 방법](../ReadingGuide.md) · [용어집](../Glossary.md) · [보충 주석](../SupplementaryNotes.md) · [챕터 목록](../../README.md#학습-순서)
