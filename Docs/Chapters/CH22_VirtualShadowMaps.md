# CH22 Virtual Shadow Maps

## 중심 질문

바람 부는 풀밭은 왜 카메라가 멈춰도 그림자 작업이 생길까?

## 먼저 알아둘 답

캐시한 그림자는 형상이 변하면 다시 계산해야 하므로, 정점 변형은 그림자 재사용을 줄일 수 있습니다.

## 왜 알아야 할까

식생의 움직임과 그림자 품질을 유지하면서 먼 배경의 갱신 범위를 설계하기 위해 배웁니다.

### 예제 학습 목표

정지 카메라에서 WPO만 바꿔 그림자 페이지 갱신의 원인을 확인합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part04_LightingAndImageQuality/CH22_VirtualShadowMaps/Maps/L_CH22_VirtualShadowMaps`

## 왜 이런 결과가 생길까

VSM은 높은 해상도의 그림자를 필요한 작은 페이지 단위로 관리합니다. 장면과 광원이 변하지 않으면 준비한 페이지를 다시 사용할 수 있습니다. WPO로 잎의 위치가 바뀌면 기존 그림자는 낡은 정보가 됩니다. 영향을 받는 영역의 페이지를 무효화하고 새로 그려야 움직이는 그림자가 맞습니다.

## 제작 중에는 이렇게 나타납니다

카메라가 정지해도 움직이는 식생 때문에 갱신은 계속될 수 있습니다. 그림자 선명도만 낮추기 전에 무엇이 캐시를 깨뜨리는지 보면 더 적절한 수정 대상을 찾을 수 있습니다.

![Epic 공식 진단 비교 · 왼쪽은 캐시 페이지, 오른쪽은 무효화를 유발하는 Bounds도 표시한 화면입니다.](../Images/External/vsm-cache-print.png)

Epic 공식 진단 비교 · 왼쪽은 캐시 페이지, 오른쪽은 무효화를 유발하는 Bounds도 표시한 화면입니다.

읽을 곳  이 시각화에서 초록은 재사용, 빨강은 새로 필요하거나 무효화된 페이지입니다. 오른쪽 경계가 어떤 영역에 영향을 주는지 봅니다. UE 5.4 문서의 표시 예이며 비용 측정은 진단 모드를 끈 뒤 수행합니다.

[© Epic Games · 공식 문서 · 출처 56](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.4)

동일 범위의 원본을 나란히 배치 · 표제 추가

원저작권과 원문 출처 표시는 유지합니다

## 실습 절차

카메라와 광원을 고정한 식생 장면에서 바람 WPO만 켜고 끕니다. VSM의 Cached Page와 무효화 Bounds 시각화를 비교합니다. 이후 진단을 끄고 그림자 생성 시간과 전체 GPU 시간을 기록합니다.

## 예상 결과와 이유

바람이 켜진 상태는 해당 식생 주변에 지속적인 페이지 갱신이 생길 수 있습니다. 바람을 끄면 정적 영역의 재사용 비중이 높아질 것으로 예상합니다.

## 결과를 어떻게 해석할까

새로 보인 영역 때문에 만든 페이지와 변형 때문에 다시 만든 페이지를 구분합니다. 시각화 변화가 실제 실행 시간에 얼마나 영향을 줬는지는 별도로 측정합니다.

## 실제 제작에서의 선택

읽히지 않는 원거리 변형을 줄이거나 Bounds와 그림자 참여를 조정합니다. 움직임을 남긴 채 무효화만 막으면 낡은 그림자가 생길 수 있습니다.

## 이해한 뒤 확인할 조건

페이지 색과 명령은 버전별 표시를 확인합니다. 메모리 예산·투영 비용은 갱신 원리를 이해한 뒤 확장할 항목입니다.

## 공식 자료와 확장

- [Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)
- [Virtual Shadow Maps](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
