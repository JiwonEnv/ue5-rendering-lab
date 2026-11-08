# CH19 Mipmap과 샘플링

## 중심 질문

먼 바닥의 잔무늬는 왜 고해상도 원본만 쓰면 더 흔들릴까?

## 먼저 알아둘 답

작은 화면 픽셀이 많은 텍셀을 대표해야 하므로, 적절히 축소한 정보를 읽어야 안정적입니다.

## 왜 알아야 할까

원거리 패턴과 미세 노멀의 깜빡임을 텍스처 해상도 부족과 구분하기 위해 배웁니다.

### 예제 학습 목표

같은 이동에서 밉의 선명도 손실과 시간적 안정성을 함께 관찰합니다.

**구현 상태 — 기본 레벨 준비, 아래 절차에 따른 특화 예제 제작과 실측 필요**

레벨 `/Game/RenderingLab/Chapters/Part03_GeometryAndTextures/CH19_Mipmaps/Maps/L_CH19_Mipmaps`

## 왜 이런 결과가 생길까

텍스처의 한 데이터 칸을 텍셀이라고 합니다. 멀리 있는 바닥에서는 화면 한 픽셀이 많은 텍셀을 덮습니다. 원본의 한 점만 읽으면 카메라의 작은 이동에도 검은 줄과 흰 줄을 번갈아 고를 수 있습니다. 밉맵은 원본을 단계적으로 축소해 넓은 영역을 대표하는 값을 준비합니다. 필터링은 읽은 값들을 섞어 표본의 불연속을 줄입니다.

## 제작 중에는 이렇게 나타납니다

원본을 더 선명하게 만드는 일과 멀리서 안정적으로 보이게 하는 일은 다릅니다. 너무 촘촘한 패턴은 원본이 선명해도 화면에서 충분히 표현할 수 없습니다.

![외부 실제 렌더 비교 · 왼쪽 No MipMapping, 오른쪽 With MipMapping입니다.](../Images/External/mipmap-print.png)

외부 실제 렌더 비교 · 왼쪽 No MipMapping, 오른쪽 With MipMapping입니다.

읽을 곳  수평선에 가까운 먼 바닥에서 왼쪽의 물결무늬와 오른쪽의 안정된 패턴을 비교합니다. 원본은 Blender 렌더이며 필터링도 관여할 수 있으므로 UE에서 밉만 바꾼 통제 실험으로 해석하지 않습니다.

[BillyBob CornCob · Wikimedia Commons · 출처 43](https://commons.wikimedia.org/wiki/File:Mipmap_Aliasing_Comparison.png)

원본 전체와 비율 유지

[이용 조건 CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)

## 실습 절차

잔무늬 바닥의 일반 밉 버전과 NoMipmaps 버전을 준비합니다. 원하는 밉이 상주한 조건에서 같은 낮은 시선으로 천천히 이동하며 원거리 영역을 녹화합니다.

## 예상 결과와 이유

밉이 없는 버전은 먼 패턴의 모아레와 깜빡임이 커지고, 일반 밉은 일부 선명도를 줄이면서 더 안정될 것으로 예상합니다.

## 결과를 어떻게 해석할까

정지 화면의 선명도만 고르지 않습니다. 비스듬한 바닥에서는 이방성 필터링도 관여하므로 그 설정을 고정한 뒤 밉 차이를 봅니다.

## 실제 제작에서의 선택

플레이 거리에서 읽힐 패턴 크기와 노멀 강도를 먼저 맞추고 밉을 사용합니다. 흐림이 과하면 생성·필터·상주 상태를 순서대로 조사합니다.

## 이해한 뒤 확인할 조건

밉 체인의 데이터 증가와 캐시·대역폭 이득은 성능의 확장 주제입니다. 밉 선택과 실제 메모리 상주는 CH20에서 구분합니다.

## 공식 자료와 확장

- [Texture Asset Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine)
- [Texture Streaming Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-overview-for-unreal-engine)

[읽는 순서](../ReadingGuide.md) · [용어집](../Glossary.md) · [심화와 적용 조건](../SupplementaryNotes.md)
