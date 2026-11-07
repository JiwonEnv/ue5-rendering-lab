# CH22 Virtual Shadow Maps와 페이지 캐시

## 챕터 학습 목표

그림자 해상도와 페이지 캐시 재사용이 연결되는 방식을 이해합니다. 넓은 환경과 움직이는 식생에서 라이트 범위·캐스터·변형이 그림자 품질과 갱신 비용에 미치는 영향을 판단합니다.

### 예제 학습 목표

풀밭의 바람과 카메라 이동 조건을 나눠 캐시 페이지 변화와 그림자 생성·투영 비용을 비교합니다.

**구현 상태 — 기본 실습 레벨 준비**

바닥, 조명, 카메라와 비교용 기본 도형을 가진 시작 레벨입니다. 아래 항목은 챕터별 예제를 완성할 때 수행할 실습 절차입니다.

레벨 경로 `/Game/RenderingLab/Chapters/Part04_LightingAndImageQuality/CH22_VirtualShadowMaps/Maps/L_CH22_VirtualShadowMaps`

## 흐름 개념도

```mermaid
flowchart LR
 N0["필요한 그림자 영역"]
 N1["해당 페이지 계산"]
 N0 --> N1
 N2["다음 프레임에 재사용"]
 N1 --> N2
```

## 원리

그림자 맵은 라이트에서 본 표면 깊이를 저장해 빛이 가려지는지 판정하는 자료입니다. VSM은 높은 해상도의 그림자 맵을 작은 페이지 단위로 제공하는 방식입니다. 필요한 부분만 계산하고 메모리에 유지해 넓은 장면의 세밀한 그림자를 다룹니다.

## 작동 과정

카메라 화면에 보이는 표면이 요구하는 그림자 영역을 찾고 해당 페이지를 준비합니다. 방향광에는 카메라 주변의 여러 범위를 계층으로 배치하는 클립맵을 사용합니다. 이전에 계산한 페이지를 다시 쓰는 것이 캐시 재사용입니다. 라이트나 물체가 변하면 과거 결과가 맞지 않아 페이지를 새로 계산할 수 있습니다.

## 아트 실무

그림자를 만드는 물체를 캐스터라고 부릅니다. 바람으로 정점을 움직이는 WPO 식생은 멀리서도 캐시 갱신을 일으킬 수 있습니다. 원거리 바람, 그림자 거리와 라이트 영향 반경을 각각 조정한 버전을 비교합니다. 한 번에 여러 변수를 끄면 무엇이 비용을 줄였는지 알기 어렵습니다.

## 성능 비용

그림자용 깊이를 만드는 작업과, 그 결과를 표면에 적용하는 투영 작업은 별도 비용입니다. 새로 필요한 페이지, 움직이는 캐스터, 큰 bounds와 겹치는 광원은 작업량을 늘릴 수 있습니다. 캐시 무효화는 저장한 결과가 더 이상 맞지 않아 다시 계산해야 하는 상태를 뜻합니다.

## 언리얼 실습

Shadow Map Method에서 Virtual Shadow Maps를 확인합니다. 카메라를 고정하고 VSM Cached Page 시각화로 바람 켜짐·꺼짐을 비교합니다. 다음에는 바람 조건을 고정하고 카메라를 움직입니다. Shadow Depths와 Projection 계열 시간을 나누어 기록합니다.

## 핵심 요약

그림자 선명도와 함께, 이미 계산한 결과를 얼마나 재사용하는지 확인합니다.

## 공식 자료

- [Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)
- [Virtual Shadow Maps](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine)

## 관련 개념

- [CH10 Shader와 순열과 WPO](CH10_ShadersWPO.md)
- [CH21 Lumen과 동적 간접광](CH21_Lumen.md)

## 작업 기록

- 제작한 에셋
- 바꾼 변수와 유지한 조건
- 전후 화면과 실행 시간
- 확인한 기기와 설정


[처음 읽는 방법](../ReadingGuide.md) · [용어집](../Glossary.md) · [보충 주석](../SupplementaryNotes.md) · [챕터 목록](../../README.md#학습-순서)
