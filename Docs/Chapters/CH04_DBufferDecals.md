# CH04 DBuffer와 데칼

## 챕터 학습 목표

데칼이 수신 표면을 바꾸는 원리와 적용 시점을 이해합니다. 벽의 오염·손상·표식으로 반복을 줄일 때 투영 범위, 수신 설정, 겹침이 표현과 비용에 미치는 영향을 판단합니다.

### 예제 학습 목표

벽 데칼의 개수와 투영 박스 범위를 바꿔 표면 변화, 잘못 묻는 영역과 관련 패스의 비용을 확인합니다.

**구현 상태 — 기본 실습 레벨 준비**

바닥, 조명, 카메라와 비교용 기본 도형을 가진 시작 레벨입니다. 아래 항목은 챕터별 예제를 완성할 때 수행할 실습 절차입니다.

레벨 경로 `/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH04_DBufferDecals/Maps/L_CH04_DBufferDecals`

## 흐름 개념도

```mermaid
flowchart LR
 N0["투영 범위 확인"]
 N1["표면 변경을 준비"]
 N0 --> N1
 N2["기본 재질에 적용"]
 N1 --> N2
```

## 원리

데칼은 벽의 얼룩이나 표식을 다른 표면 위에 투영하는 표현입니다. DBuffer는 데칼이 바꿀 색·거칠기·표면 방향 등의 값을 잠시 모아 두는 데이터입니다. 이 방식에서는 벽의 기본 재질을 계산하는 Base Pass가 데칼 정보를 읽어 표면에 반영합니다.

## 작동 과정

데칼 Actor의 박스는 투영할 공간 범위를 정합니다. 엔진은 깊이 정보로 그 안의 표면 위치를 찾고 데칼의 어느 부분을 적용할지 계산합니다. 별도 방식인 GBuffer 데칼은 Base Pass 뒤, 조명 전에 기존 표면 데이터에 합성합니다. 두 방식의 적용 시점과 지원 조건이 같다고 가정하지 않습니다.

## 아트 실무

모듈 벽 여러 개가 같은 재질을 쓰더라도 데칼로 빗물 자국과 손상을 다르게 줄 수 있습니다. 뒤의 소품에 얼룩이 함께 묻으면 투영 박스 깊이를 줄입니다. Receives Decals는 물체가 데칼을 받을지, Decal Response는 재질이 어떤 변경을 받을지 정하는 설정입니다.

## 성능 비용

화면을 덮는 면적과 겹치는 데칼 수가 늘면 같은 위치에서 처리할 작업도 늘어납니다. DBuffer가 필요로 하는 깊이 준비 작업의 비용도 확인합니다. 이미 다른 기능 때문에 깊이를 먼저 준비하고 있다면, 그 비용 전체를 데칼 하나의 비용으로 계산하지 않습니다.

## 언리얼 실습

Material Domain을 Deferred Decal로 정한 얼룩 재질을 벽에 투영합니다. Domain은 그 재질을 어떤 용도로 사용할지 정하는 구분입니다. 한 개와 겹친 여덟 개를 비교한 뒤, 보이는 얼룩을 유지하면서 투영 박스만 줄입니다. 데칼 관련 패스와 Base Pass의 시간을 함께 기록합니다.

## 핵심 요약

데칼의 수뿐 아니라 투영 범위와 수신 표면을 관리합니다. DBuffer 값을 재질에서 직접 조합한다면 기본 적용과 중복되지 않는지도 확인합니다.

## 공식 자료

- [Programming with Substrate GBuffer Formats](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)
- [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine)

## 관련 개념

- [CH03 GBuffer와 표면 정보](CH03_GBuffer.md)
- [CH06 Overdraw와 화면 겹침](CH06_Overdraw.md)

## 작업 기록

- 제작한 에셋
- 바꾼 변수와 유지한 조건
- 전후 화면과 실행 시간
- 확인한 기기와 설정


[처음 읽는 방법](../ReadingGuide.md) · [용어집](../Glossary.md) · [보충 주석](../SupplementaryNotes.md) · [챕터 목록](../../README.md#학습-순서)
